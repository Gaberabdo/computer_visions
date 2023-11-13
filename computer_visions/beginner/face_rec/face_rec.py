import cv2


def detect_and_draw_faces(image_path):
    img = cv2.imread(image_path)

    # todo using open cv fun to rec face
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # todo The face classifier (face_cascade) is used to detect faces in the image using the detectMultiScale function.
    #   scaleFactor=1.1: Determines how much to zoom the image while searching for faces.
    #   minNeighbors=5: Specifies the number of neighbors required for a face to be accepted.
    #   minSize=(30, 30): Specifies the minimum acceptable size for the face.

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # todo Rectangles are drawn around the detected faces.
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)

    cv2.imshow("Face", cv2.resize(img, (500, 500)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_and_draw_faces(r"D:\Projcets\py\assets\beginner\object_det\object_det.png")
