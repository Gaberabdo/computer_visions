import cv2
import numpy as np
import matplotlib.pyplot as plt


def point_detection(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # todo Define a kernel for point detection
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

    # Apply convolution to the image
    result = cv2.filter2D(img, -1, kernel)
    cv2.imshow("Point Detection", result)
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
