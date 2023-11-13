import cv2


def canny_filter(image_path):
    # todo open image
    img = cv2.imread(image_path)

    #  todo apply Canny filter
    edges = cv2.Canny(img, 100, 200, 3, )

    # todo display the original and edge-detected images
    cv2.imshow('canny', edges)
    cv2.imshow('original', img)
    cv2.waitKey(0)
