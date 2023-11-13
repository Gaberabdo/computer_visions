import cv2
import numpy as np


def erosion(image_path):
    img = cv2.imread(image_path, 0)

    # todo binarize the image
    binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # todo np.ones: A function in the NumPy library that creates an array of units (values of 1).
    #  '(5, 5)': are the specific dimensions of the matrix, in this case it is a square matrix so we have 5 rows and 5 columns.
    #  np.uint8: It is the data type that is used to represent values within an array. In this case, uint8 is used to represent positive integers (unsigned integers) with a range from 0 to 255.
    kernel = np.ones((5, 5), np.uint8)

    # todo invert  image color
    invert = cv2.bitwise_not(binr)

    # todo erosion the image
    erosion_cas = cv2.erode(invert, kernel, iterations=1)

    cv2.imshow('erosion', erosion_cas)
    cv2.imshow('original', img)
    cv2.waitKey(0)
