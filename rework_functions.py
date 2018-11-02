import numpy as np
import cv2 as cv
import face_recognition as f_c


def detect(image_path):
    image = cv.imread(image_path)
    image_f_c = image[:, :, ::-1]
    face_locks = f_c.face_locations(image_f_c)

    for top, right, bottom, left in face_locks:
        cv.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

    cv.imwrite(image_path, image)
