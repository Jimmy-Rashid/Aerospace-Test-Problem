import os
import cv2
import numpy as np
from PIL import Image

data_path = "data/"

for pokemon in os.listdir(data_path):
    pokemon = cv2.imread("data/" + pokemon)
    hsv = cv2.cvtColor(pokemon, cv2.COLOR_BGR2HSV)

    low_hugh_lower = np.array([0, 100, 20])
    low_hugh_upper = np.array([10, 255, 255])
    high_hugh_lower = np.array([160, 100, 20])
    high_hugh_upper = np.array([179, 255, 255])

    lower_mask = cv2.inRange(hsv, low_hugh_lower, low_hugh_upper)
    upper_mask = cv2.inRange(hsv, high_hugh_lower, high_hugh_upper)

    mask = lower_mask | upper_mask

    result = cv2.bitwise_and(pokemon, pokemon, mask=mask)
    red_pixel_count = cv2.countNonZero(mask)
    print(red_pixel_count)

