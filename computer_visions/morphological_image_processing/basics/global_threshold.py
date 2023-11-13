import cv2


def global_threshold(image_path):
    # todo open image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    threshold_value = 128

    #  todo apply global_threshold filter
    _, threshold_image = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

    # todo display the original and edge-detected images
    cv2.imshow('Thresholded Image', cv2.resize(threshold_image, (400, 400)))
    cv2.imshow('original', img)
    cv2.waitKey(0)
