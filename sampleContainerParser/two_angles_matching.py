#!/opt/DAQ/venv/bin/python3.9

import os
import random
import cv2
import numpy as np
from time import sleep
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

def wait_for_q():
    while True:
        key = cv2.waitKey(0)
        if key == ord('q'):
            break

def read_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return image

def sample_in_operation_model_simulation(image):
    return None

def get_bounding_boxes(model, sample_in_operation_model, image):
    result = model.predict(image, imgsz=1280)
    sample_in_operation_result = sample_in_operation_model_simulation(image)#sample_in_operation_model.predict(image, imgsz=1280)
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
    #for res in sample_in_operation_result:
    #    for box in res.boxes:
    #        bounding_box = box.xyxy[0].tolist() # [x1, y1, x2, y2]
    #        confidence = float(box.conf[0])
    #        cls = float(box.cls[0])
    #        label = res.names[cls]
    #        print(label, confidence)
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
        centroid = (cx, cy, box['label'])
        centroids.append(centroid)
    return centroids

def draw_centroids(image, centroids, color=GREEN_COLOR):
    for counter, centroid in enumerate(centroids):
        text = str(counter)
        cx, cy = np.array(centroid).astype(float).astype(int)
        cv2.circle(image, (cx, cy), radius=2, color=color, thickness=-1)
        if counter % 2:
            txt_color = BLUE_COLOR
        else:
            txt_color = RED_COLOR
        cv2.putText(image, text, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1.5, txt_color, 2, cv2.LINE_AA)

def draw_ind_text(image, centroids):
    for index, centroid in enumerate(centroids):
        cx, cy = int(float(centroid[0])), int(float(centroid[1]))
        text = str(index)
        if index % 2:
            txt_color = BLUE_COLOR
        else:
            txt_color = RED_COLOR
        cv2.putText(image, text, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1.5, txt_color, 2, cv2.LINE_AA)

def ransac_ellipse(points, iterations=200, threshold=0.2, min_inliers_ratio=0.97):
    best_ellipse = None
    max_inliers = 0

    for _ in range(iterations):
        sample_size = max(5, int(len(points) * 0.9))
        if len(points) < sample_size:
            break
        sample = points[np.random.choice(len(points), sample_size, replace=False)]

        try:
            ellipse = cv2.fitEllipse(sample)
        except Exception as err:
            print(err)
            continue

        center, axes, angle = ellipse
        cx, cy =center
        a, b = axes[0] / 2, axes[1] / 2
        theta = np.deg2rad(angle)

        cos_t, sin_t = np.cos(theta), np.sin(theta)

        # Transform points to ellipse coordinates
        x = points[:, 0] - cx
        y = points[:, 1] - cy
        x_rot = x * cos_t + y * sin_t
        y_rot = -x * sin_t + y * cos_t

        dist = np.abs((x_rot**2 / a**2) + (y_rot**2 / b**2) - 1.0)
        inliers = points[dist < threshold]

        if len(inliers) > max_inliers:
            max_inliers = len(inliers)
            best_ellipse = ellipse # cv2.fitEllipse(np.array(inliers))
            if len(inliers) / len(points) > min_inliers_ratio:
                print("Best Ellipse Found. Inliers ratio = ", len(inliers) / len(points))
                break
    print("Best Ellipse Found")
    return best_ellipse

def sort_centroids(centroids):
    centroids_wo_labels = np.array(centroids[:, :2], dtype=np.float32)
    ellipse = ransac_ellipse(centroids_wo_labels)

    (xc, yc), (major, minor), angle = ellipse
    theta = np.deg2rad(angle)

    # Inverse rotation: rotate by -theta
    inv_rotation_matrix = np.array([
        [np.cos(-theta), -np.sin(-theta)],
        [np.sin(-theta),  np.cos(-theta)]
    ])

    # Inverse scaling: divide by semi-axes
    inv_scale_matrix = np.array([
        [2 / major, 0],
        [0, 2 / minor]
    ])

    shifted = centroids_wo_labels - np.array([xc, yc])
    rotated = np.dot(shifted, inv_rotation_matrix)
    scaled = np.dot(rotated, inv_scale_matrix)

    angles = np.atan2(scaled[:, 1], scaled[:, 0])
    angles = (angles - angles[0]) % (2 * np.pi)
    #angles = (-angles) %(2 * np.pi) # flip the direction to CCW

    order = np.argsort(angles)
    sorted_centroids = centroids[order]
    return sorted_centroids

def find_base_centroid(location, centroids):
    min_dist = float('inf')
    base_centroid_index = None
    for index, centroid in enumerate(centroids):
        dist = np.sqrt((location[0] - centroid[0])**2 + (location[1] - centroid[1])**2)
        if dist < min_dist:
            base_centroid_index = index
            min_dist = dist
    return base_centroid_index

def get_based_centroids(centroids, base_index, container_angle):
    num_rotations = int(base_index - container_angle / 9)
    return np.concatenate([centroids[num_rotations:], centroids[:num_rotations]])

def combine_results(labels1, labels2):
    label1_ind = 0
    label2_ind = 0
    labels = []
    while label1_ind < len(labels1) and label2_ind < len(labels2):
        if labels1[label1_ind] == labels2[label2_ind]:
            labels.append(str(labels1[label1_ind]))
            label1_ind += 1
            label2_ind += 1
            continue
        if labels1[label1_ind] == 'no-sample':
            labels.append(str(labels1[label1_ind]))
            label1_ind += 1
        else:
            labels.append(str(labels2[label2_ind]))
            label2_ind += 1
    while label1_ind < len(labels1):
        labels.append(str(labels1[label1_ind]))
        label1_ind += 1
    while label2_ind < len(labels2):
        labels.append(str(labels2[label2_ind]))
        label2_ind += 1
    return labels

def move_to_position(position):
    print(f"moving to position: {position}")
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

def draw_sample_container(labels):
    image = np.zeros((600, 600, 3), dtype=np.uint8)
    radius = 200
    center = (300, 300)
    num_sample_holders = 40
    angle_step = 360.0 / num_sample_holders
    start_angle = 117

    print("num labels: ", len(labels))
    print(labels)
    for i in range(num_sample_holders):
        angle = np.deg2rad(start_angle + i * angle_step)
        x = int(center[0] + radius * np.cos(angle))
        y = int(center[1] + radius * np.sin(angle))
        label = labels[i]
        if label == 'sample':
            color = GREEN_COLOR
        elif label == 'no-sample':
            color = RED_COLOR
        cv2.circle(image, (x, y), radius=10, color=color, thickness=-1)

    cv2.imwrite("./work/sample_container.jpg", image)

def clean_working_dir():
    working_dir = "./work"
    if os.path.isdir(working_dir):
        for filename in os.listdir(working_dir):
            file_path = os.path.join(working_dir, filename)
            os.remove(file_path)
    else:
        os.mkdir(working_dir)

def get_labels(angle, model, sample_in_operation_model):
    move_to_position(angle)
    image = capture_image(f"./work/image_{angle}deg.jpg")
    boxes = get_bounding_boxes(model, sample_in_operation_model, image)
    num_detections = len(boxes)
    print(f"number of detections at {angle} degree", num_detections)
    image_detections = image.copy()
    draw_boxes(image_detections, boxes)
    cv2.imwrite(f"./work/image_{angle}deg_detections.jpg", image_detections)

    no_sample_width, no_sample_hight = get_no_sample_dimensions(boxes)
    centroids = get_holders_centroids(boxes, no_sample_width, no_sample_hight)
    sorted_centroids = sort_centroids(np.array(centroids))

    # Expected location for sample in operation location
    expected_sample_in_operation_location = (1116, 1293)
    cv2.circle(image, expected_sample_in_operation_location, radius=2, color=BLUE_COLOR, thickness=-1)
    base_centroid_index = find_base_centroid(expected_sample_in_operation_location, sorted_centroids[:, :2].astype(float))
    based_centroids = get_based_centroids(sorted_centroids, base_centroid_index, angle)
    draw_ind_text(image, based_centroids)
    labels = based_centroids[:, 2]
    print(labels)
    return labels

def main(model, sample_in_operation_model, reference_angle):
    ACQUIRE_PV.put(1)
    move_to_position(reference_angle)
    reference_position = SAMPLE_CONTAINER_POS_PV.get()

    labels = get_labels(reference_angle, model, sample_in_operation_model)
    if len(labels) == 40:
        draw_sample_container(labels)
        return

    angles = [90, 45, 135]
    for angle_offset in angles:
        angle = reference_angle + angle_offset
        other_labels = get_labels(angle, model, sample_in_operation_model)
        if len(other_labels) == 40:
            labels = other_labels
        else:
            combined_labels = combine_results(labels, other_labels)
            if combined_labels <= 40:
                labels = combined_labels
        if len(labels) == 40:
            break
    if len(labels) == 40:
        draw_sample_container(labels)
    else:
        raise Exception(f"Could not find the 40 labels. Instead found {len(labels)}")
    move_to_position(reference_position)

if __name__ == '__main__':
    model = YOLO("./yolo_model.pt")
    sample_in_operation_model = YOLO("./yolov8s.pt")
    reference_angle = 0
    clean_working_dir()
    main(model, sample_in_operation_model, reference_angle)
