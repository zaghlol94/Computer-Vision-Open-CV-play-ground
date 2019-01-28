import cv2
import numpy as np
import matplotlib.pyplot as plt

video = cv2.VideoCapture("mouthwash.avi")
ret, first_frame = video.read()

x = 300
y = 305
width = 100
height = 115
roi = first_frame[y:y + height, x:x + width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_cr = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)
while True:
    ret, frame = video.read()
    if ret == False:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    ret, track_window = cv2.meanShift(mask, (x, y, width, height), term_cr)
    x,y,width,height = track_window
    cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),2)
    cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(60)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
