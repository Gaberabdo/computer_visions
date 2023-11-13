import cv2


def adaptive_threshold(image_path):
    # todo open image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    min_value = 0
    max_value = 255

    #  todo apply adaptive_threshold filter
    adaptive_threshold_f = cv2.adaptiveThreshold(img, max_value, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # todo display the original and edge-detected images
    cv2.imshow('Adaptive Image', cv2.resize(adaptive_threshold_f, (400, 400)))
    cv2.imshow('original', img)
    cv2.waitKey(0)
