#!/opt/DAQ/venv/bin/python3.9


#####!/usr/bin/python3.8

import os
import math
import cv2
import numpy as np
from epics import PV
from utils import capture_image
#import matplotlib.pyplot as plt

def clean_working_dir():
    base_dir = "./work"
    if not os.path.isdir(base_dir):
        os.mkdir(base_dir)
    working_dir = f"{base_dir}/operation_sample_laser/"
    if os.path.isdir(working_dir):
        for filename in os.listdir(working_dir):
            file_path = os.path.join(working_dir, filename)
            os.remove(file_path)
    else:
        os.mkdir(working_dir)

def main():
    image = capture_image(f"./work/operation_sample_laser/operation_sample.jpg", exposure_time=0.0005)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(image_gray, 250, 255, cv2.THRESH_BINARY)
    cv2.imwrite(f"./work/operation_sample_laser/threshold.jpg", thresholded)

    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(thresholded, kernel)
    cv2.imwrite(f"./work/operation_sample_laser/dilated.jpg", dilated)

    num_labels, labels, stats, centroids = connected_components = cv2.connectedComponentsWithStats(dilated)
    sample_in_operation_location = tuple(map(int, centroids[1]))
    cv2.circle(image, sample_in_operation_location, radius=2, color=(0, 0, 255), thickness=-1)
    cv2.imwrite(f"./work/operation_sample_laser/result.jpg", image)
    #print("num_labels: ", num_labels)
    #print("labels: ", labels)
    #print("stats: ", stats)
    #print("centroids: ", centroids)

    #hist = cv2.calcHist([image], [0], None, [56], [200, 256])
    #plt.plot(hist)
    #plt.title("Grayscale Image Intensity Histogram")
    #plt.xlabel("Intensity Value")
    #plt.ylabel("Pixel Count")
    #plt.savefig('./work/operation_sample_laser/hist.jpg')
    #plt.show()

if __name__ == '__main__':
    clean_working_dir()
    main()

