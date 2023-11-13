import cv2


def connected_components(image_path):
    # Read the image in BGR format
    img = cv2.imread(image_path)

    # Convert the image to YCrCb color space
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Extract the Cr and Cb channels
    cr_channel, cb_channel, _ = cv2.split(img_ycrcb)

    # Set thresholds for Cr and Cb
    cr_threshold = 150
    cb_threshold = 120

    # Create binary masks based on the thresholds
    cr_mask = cv2.threshold(cr_channel, cr_threshold, 255, cv2.THRESH_BINARY)[1]
    cb_mask = cv2.threshold(cb_channel, cb_threshold, 255, cv2.THRESH_BINARY)[1]

    # Combine the masks
    combined_mask = cv2.bitwise_and(cr_mask, cb_mask)

    # Find connected components in the combined mask
    _, labels, stats, centroids = cv2.connectedComponentsWithStats(combined_mask, connectivity=8)

    # Loop over the connected components
    for label in range(1, len(stats)):
        area = stats[label, cv2.CC_STAT_AREA]
        if area > 100:
            x, y, w, h = stats[label, cv2.CC_STAT_LEFT], stats[label, cv2.CC_STAT_TOP], stats[label, cv2.CC_STAT_WIDTH], \
                stats[label, cv2.CC_STAT_HEIGHT]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

    # Display the result
    cv2.imshow('Connected Components', cv2.resize(img, (400, 400)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
