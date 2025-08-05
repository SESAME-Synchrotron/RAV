#!/opt/DAQ/venv/bin/python3.9

import os
import random
import cv2
import numpy as np
from time import sleep
from scipy.spatial.distance import cdist
from ultralytics import YOLO
from epics import PV

BLUE_COLOR = (255, 0, 0)
GREEN_COLOR = (0, 255, 0)
RED_COLOR = (0, 0, 255)

CAM_PREFIX = "ID09EH-DCA-FLIR02:AI-CAM2-SIDE"
ACQUIRE_PV = PV(CAM_PREFIX + ":Acquire")
IMAGE_DATA_PV = PV(CAM_PREFIX.split(':')[0] + ":image1:ArrayData")
SIZE_X_PV = PV(CAM_PREFIX + ":ArraySizeX_RBV")
SIZE_Y_PV = PV(CAM_PREFIX + ":ArraySizeY_RBV")
EXP_TIME_PV = PV(CAM_PREFIX + ":AcquireTime")
SAMPLE_CONTAINER_POS_PV = PV("I09R2-MO-MC1:ES-DIFF-STP-ROTX1")
SAMPLE_CONTAINER_DMOV_PV = PV("I09R2-MO-MC1:ES-DIFF-STP-ROTX1.DMOV")

def read_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return image

def get_bounding_boxes(model, image):
    result = model.predict(image, imgsz=1280)
    boxes = []
    for res in result:
        for box in res.boxes:
            bounding_box = box.xyxy[0].tolist() # [x1, y1, x2, y2]
            confidence = float(box.conf[0])
            cls = float(box.cls[0])
            label = res.names[cls]
            boxes.append({
                            "class_id": cls,
                            "label": label,
                            "confidence": confidence,
                            "bbox": bounding_box
                        })
    boxes = remove_fully_overlapped_boxes(boxes)
    boxes = remove_boxes_below_confidence_level(boxes, confidence_threshold=0.5)
    return boxes

def remove_fully_overlapped_boxes(boxes):
    keep = []
    for a, box_a in enumerate(boxes):
        ax1, ay1, ax2, ay2 = box_a['bbox']
        is_inside = False
        for b, box_b in enumerate(boxes):
            if a == b or box_b['label'] == 'sample':
                continue
            bx1, by1, bx2, by2 = box_b['bbox']
            if ax1 >= bx1 and ay1 >= by1 and ax2 <= bx2 and ay2 <= by2:
                is_inside = True
                break
        if not is_inside:
            keep.append(box_a)
    return keep

def remove_boxes_below_confidence_level(boxes, confidence_threshold=0.9):
    keep = []
    for box in boxes:
        x1, y1, x2, y2 = map(int, box['bbox'])
        confidence = box['confidence']

        if confidence > confidence_threshold:
            keep.append(box)
    return keep

def draw_boxes(image, boxes, confidence_threshold=0.9):
    for box in boxes:
        x1, y1, x2, y2 = map(int, box['bbox'])
        confidence = box['confidence']
        label = box['label']
        label_color = BLUE_COLOR
        if label == "sample":
            label_color = GREEN_COLOR
        cv2.rectangle(image, (x1, y1), (x2, y2), label_color, 2)
        cv2.putText(image, f"{confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, label_color, 2)

def get_no_sample_dimensions(boxes):
    no_sample_width_sum = 0
    no_sample_hight_sum = 0
    no_sample_box_count = 0
    for box in boxes:
        if box['label'] == 'sample':
            continue
        x1, y1, x2, y2 = box['bbox']
        width = x2 - x1
        hight = y2 - y1
        no_sample_width_sum += width
        no_sample_hight_sum += hight
        no_sample_box_count += 1
    no_sample_width_mean = no_sample_width_sum / no_sample_box_count
    no_sample_hight_mean = no_sample_hight_sum / no_sample_box_count
    return no_sample_width_mean, no_sample_hight_mean

def get_holders_centroids(boxes, no_sample_width, no_sample_hight):
    centroids = []
    for box in boxes:
        x1, y1, x2, y2 = box['bbox']
        if box['label'] == 'no-sample':
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
        elif box['label'] == 'sample':
            cx = x1 + 0.5 * no_sample_width
            cy = y2 - 0.5 * no_sample_hight
        centroid = (cx, cy)
        centroids.append(centroid)
    return centroids

def draw_centroids(image, centroids, color=GREEN_COLOR):
    for centroid in centroids:
        cx, cy = map(int, centroid)
        cv2.circle(image, (cx, cy), radius=2, color=color, thickness=-1)

def add_missing_boxes(boxes_0deg, centroids_0deg, centroids_90deg, no_sample_width, no_sample_hight):
    dist_matrix = cdist(centroids_90deg, centroids_0deg)  # shape: (len(centroids_90deg), len(centroids_0deg))
    min_indices = np.array(np.argmin(dist_matrix, axis=1))
    min_dist = dist_matrix.min(axis=1)
    print(min_dist)
    missing_indices = np.where(min_dist > 10)[0]
    missing_centroids = [centroids_90deg[i] for i in missing_indices]
    for centroid in missing_centroids:
        cx, cy = centroid
        x1 = cx - no_sample_width / 2
        x2 = cx + no_sample_width / 2
        y1 = cy - no_sample_hight / 2
        y2 = cy + no_sample_hight / 2
        boxes_0deg.append({
                           "class_id": "0",
                           "label": "no-sample",
                           "confidence": 0.8,
                           "bbox": [x1, y1, x2, y2]
                          })
    return boxes_0deg

def rotate_sample_container(reference_position, index_choices):
    position = reference_position
    while abs(position - reference_position) < 5:
        index = random.choice(index_choices)
        index_choices.remove(index)
        position = index * 9
    print(f"moving to position: {position}")
    move_to_position(position)

def move_to_position(position):
    SAMPLE_CONTAINER_POS_PV.put(position)
    sleep(0.1)
    while not SAMPLE_CONTAINER_DMOV_PV.get():
        sleep(1)

def capture_image(image_path):
    timeout = 5
    ACQUIRE_PV.put(0, wait=True) # stop acquiring
    sleep(1)
    EXP_TIME_PV.put(0.005, wait=True)
    image_data = IMAGE_DATA_PV.get(timeout=timeout, use_monitor=False)
    size_x = SIZE_X_PV.get(timeout=timeout, use_monitor=False)
    size_y = SIZE_Y_PV.get(timeout=timeout, use_monitor=False)
    image = np.reshape(image_data, (size_y, size_x))
    image = np.flipud(image)
    image = image.astype(np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(image_path, image)
    ACQUIRE_PV.put(1)
    return image

def clean_working_dir():
    working_dir = "./work"
    if os.path.isdir(working_dir):
        for filename in os.listdir(working_dir):
            file_path = os.path.join(working_dir, filename)
            os.remove(file_path)
    else:
        os.mkdir(working_dir)

def main(model):
    # optional: move the container to position 0 so the reference position will be zero
    ACQUIRE_PV.put(1)
    image = capture_image("./work/reference_image.jpg")
    boxes = get_bounding_boxes(model, image)
    num_detected_objects = len(boxes)
    print("number of detections at reference position", num_detected_objects)
    ref_image_detections = image.copy()
    draw_boxes(ref_image_detections, boxes)
    cv2.imwrite("./work/reference_image_detections.jpg", ref_image_detections)

    reference_position = SAMPLE_CONTAINER_POS_PV.get()
    index_choices = list(range(1, 39))
    iter_count = 0
    while num_detected_objects < 40 and len(index_choices):
        iter_count += 1
        rotate_sample_container(reference_position, index_choices)
        other_image = capture_image(f"./work/iter#{iter_count}.jpg")
        other_boxes = get_bounding_boxes(model, other_image)
        print("number of detections at new angle", len(other_boxes))
        draw_boxes(other_image, other_boxes)
        cv2.imwrite(f"./work/iter#{iter_count}_detections.jpg", other_image)

        no_sample_width, no_sample_hight = get_no_sample_dimensions(boxes)
        centroids = get_holders_centroids(boxes, no_sample_width, no_sample_hight)
        other_centroids = get_holders_centroids(other_boxes, no_sample_width, no_sample_hight)
        boxes = add_missing_boxes(boxes, centroids, other_centroids,
                                  no_sample_width, no_sample_hight)
        boxes = remove_fully_overlapped_boxes(boxes)
        num_detected_objects = len(boxes)
    move_to_position(reference_position)

    draw_boxes(image, boxes)
    if num_detected_objects == 40:
        print("40 Sample Holders detected successfully")
    else:
        print("Could not detect All the 40 sample holders!")
        print(f"Number of Detected Holders: {num_detected_objects}")
    cv2.imwrite("./work/output.jpg", image)

if __name__ == '__main__':
    model = YOLO("./yolo_model.pt")
    clean_working_dir()
    main(model)

