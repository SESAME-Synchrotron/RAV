import numpy as np
import cv2
from time import sleep
from epics import PV

CAM_PREFIX = "ID09EH-DCA-FLIR02:AI-CAM2-SIDE"
ACQUIRE_PV = PV(CAM_PREFIX + ":Acquire")
EXP_TIME_PV = PV(CAM_PREFIX + ":AcquireTime")
IMAGE_DATA_PV = PV(CAM_PREFIX.split(':')[0] + ":image1:ArrayData")
SIZE_X_PV = PV(CAM_PREFIX + ":ArraySizeX_RBV")
SIZE_Y_PV = PV(CAM_PREFIX + ":ArraySizeY_RBV")

def capture_image(image_path, exposure_time= 0.005, colored=False):
    timeout = 5
    ACQUIRE_PV.put(0, wait=True) # stop acquiring
    sleep(1)
    EXP_TIME_PV.put(exposure_time, wait=True)
    image_data = IMAGE_DATA_PV.get(timeout=timeout, use_monitor=False)
    size_x = SIZE_X_PV.get(timeout=timeout, use_monitor=False)
    size_y = SIZE_Y_PV.get(timeout=timeout, use_monitor=False)
    image = np.reshape(image_data, (size_y, size_x))
    image = np.flipud(image)
    image = image.astype(np.uint8)
    if colored:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    if image_path:
        cv2.imwrite(image_path, image)
    ACQUIRE_PV.put(1)
    return image
