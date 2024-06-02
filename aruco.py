import cv2 as cv
import numpy as np


def main():
    cap = cv.VideoCapture(0)
    dictionary = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_5X5_50)
    parameters = cv.aruco.DetectorParameters()
    detector = cv.aruco.ArucoDetector(dictionary, parameters)
    while True:
        ret, frame = cap.read()
        corners, ids, reajected = detector.detectMarkers(frame)
        if len(corners):
            ids = ids.flatten()

            for (marker_corner, marker_id) in zip(corners, ids):
                print(marker_corner)
                print(marker_id)
                print("-----------")
                corner = marker_corner.reshape((4,2))
                (top_left, top_right, bottom_right, bottom_left) = corner

                top_left = (int(top_left[0]),int(top_left[1]))
                top_right = (int(top_right[0]), int(top_right[1]))
                bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
                bottom_left = (int(bottom_left[0]), int(bottom_left[1]))

                cv.line(frame, top_left, top_right, (255,0,255), 4)
                cv.line(frame, top_right, bottom_right, (255,0,255), 4)
                cv.line(frame, bottom_right, bottom_left, (255,0,255), 4)
                cv.line(frame, bottom_left, top_left, (255,0,255), 4)

                center_x = int((top_left[0] + bottom_right[0]) / 2.0)
                center_y = int((top_left[1] + bottom_right[1]) / 2.0)

                cv.circle (frame, (center_x, center_y),5,(0,0,255), -1)
                cv.putText(
                    frame, f'ID: {marker_id} X: {center_x} Y: {center_y}',
                    (center_x + 5, center_y), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0,255,255), 1)

        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xff == ord("q"):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()