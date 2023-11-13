import cv2
import numpy as np


def thinning_filter(image_path):
    img = cv2.imread(image_path, 0)

    # todo binarize the image
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # todo Invert the binary image (objects should be white)
    binary_img = cv2.bitwise_not(binary_img)

    # todo Create an empty output image
    thinned_img = np.zeros(binary_img.shape, dtype=np.uint8)

    # todo Thinning the image
    kernel = np.ones((3, 3), np.uint8)

    # todo applying different method to get batter result
    while cv2.countNonZero(binary_img) > 0:
        erode = cv2.erode(binary_img, kernel, iterations=1)
        opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
        subtracted = cv2.subtract(binary_img, opening)
        thinned_img = cv2.bitwise_or(thinned_img, subtracted)
        binary_img = erode.copy()

    thinned_img = cv2.bitwise_not(thinned_img)

    cv2.imshow('Thinning', cv2.resize(thinned_img, (400, 400)))
    cv2.imshow('Org', cv2.resize(img, (400, 400)))
    cv2.waitKey(0)
