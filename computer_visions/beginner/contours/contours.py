import cv2

from computer_visions.beginner.canny.canny import canny_filter


def find_contours(image_path):
    # todo load image
    image = cv2.imread(image_path)

    # todo Find Canny edges
    edges = cv2.Canny(image, 100, 200, 3, )

    # todo find contours
    #    cv2.RETR_EXTERNAL  => Search only for the outer edges
    #    CHAIN_APPROX_NONE  => Edge rounding technology
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # todo Apply edges to the original image
    cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

    cv2.imshow('Contours', cv2.resize(image, (400, 400)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


