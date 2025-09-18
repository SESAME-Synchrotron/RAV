#!/opt/DAQ/venv/bin/python3.9

import os
import math
import cv2
import numpy as np
from epics import PV
from utils import capture_image

ROBOT_CURRENT_STATE = PV("ROBOT:CurrentState")

def draw_line_by_points(image, start_point, end_point):
    cv2.line(image, start_point, end_point, (255, 0, 0), 1)

def draw_line_by_angle(image, start_point, angle, length):
    angle_rad = math.radians(angle)
    x1, y1 = start_point
    x2 = int(x1 + length * np.cos(angle_rad))
    y2 = int(y1 - length * np.sin(angle_rad)) # minus because y goes down
    cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 1)

def template_match(image, template):
    template_width, template_hight = template.shape[::-1]
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_hight)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2) # delete
    matched_object = image[top_left[1]: bottom_right[1], top_left[0]: bottom_right[0]]
    return matched_object, max_loc

def find_sample_operation_location(original_image, fingers_image, fingers_loc, template_width):
    fingers_image_width, fingers_image_hight = fingers_image.shape[::-1]
    #fingers_image = fingers_image[:, int(0.2 * fingers_image_width): int(0.8 * fingers_image_width)]
    cv2.imwrite("./work/operation_sample/fingers_image_cropped.jpg", fingers_image)
    tilt_angle = get_tilt_angle(fingers_image)
    draw_line_by_angle(original_image, (fingers_loc[0] + template_width // 2, fingers_loc[1]), tilt_angle, 930)

    samples = [(547,995), (598, 1012), (659, 1027), (728, 1033), (802, 1039),
               (579, 802), (629, 790), (681, 780), (736, 770)]
    for sample in samples:
        cv2.circle(original_image, sample, radius=2, color=(255, 0, 0), thickness=-1)

    cv2.imwrite("./work/operation_sample/result.png", original_image)

def get_tilt_angle(fingers_image):
    blurred = cv2.GaussianBlur(fingers_image, (3, 3), 0.5)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray_clahe = clahe.apply(blurred)
    edges = cv2.Canny(gray_clahe, 50, 100)
    edges[0:10, :] = 0
    edges[-10:, :] = 0
    edges[:, 0:10] = 0
    edges[:, -10:] = 0
    lines = cv2.HoughLinesP(
                edges,
                rho=1, # distance resolution in pixels
                theta=np.pi / 180, # angle resolution in radians (1 degree)
                threshold=100, # minimum number of intersections to detect a line
                minLineLength=30,
                maxLineGap=20 # Maximum allowed gap between points on the same line
            )
    angles = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        dx = x2 - x1
        dy = -(y2 - y1)
        line_angle_rad = math.atan2(dy, dx)
        line_angle_deg = math.degrees(line_angle_rad)
        line_angle_deg = (line_angle_deg + 360) % 360
        if line_angle_deg <= 180:
            line_angle_deg = (line_angle_deg + 180) % 360
        is_horizontal = line_angle_deg < 10 or line_angle_deg > 350 or (line_angle_deg > 170 and line_angle_deg < 190)
        if not is_horizontal:
            cv2.line(fingers_image, (x1, y1), (x2, y2), (255, 255, 255), 2)
            angles.append(line_angle_deg)
    print("angles: ", angles) # remove
    save_images(
      {
          "clahe": gray_clahe,
          "canny": edges,
          "fingers_image": fingers_image
      }  
    )

    mean_angle = np.mean(angles) # so that the line angle points down towards the sample container
    return mean_angle

def save_images(images_dict):
    for label, image in images_dict.items():
        cv2.imwrite(f"./work/operation_sample/{label}.jpg", image)

def clean_working_dir():
    base_dir = "./work"
    if not os.path.isdir(base_dir):
        os.mkdir(base_dir)
    working_dir = f"{base_dir}/operation_sample/"
    if os.path.isdir(working_dir):
        for filename in os.listdir(working_dir):
            file_path = os.path.join(working_dir, filename)
            os.remove(file_path)
    else:
        os.mkdir(working_dir)

def main(method):
    if ROBOT_CURRENT_STATE.get() != "Ready Done":
        raise Exception("Robot Must be in Ready State\n")
    image = capture_image(f"./work/operation_sample/operation_sample.jpg")
    fingers_template = cv2.imread("./templates/fingers_template.jpg", cv2.IMREAD_GRAYSCALE)
    fingers, fingers_loc = template_match(image, fingers_template)
    template_width, template_hight = fingers_template.shape[::-1]
    find_sample_operation_location(image, fingers, fingers_loc, template_width)

if __name__ == '__main__':
    method = "fingers" # laser
    clean_working_dir()
    main(method)

