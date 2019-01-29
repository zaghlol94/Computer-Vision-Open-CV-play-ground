import cv2
import numpy as np

drawing = False
point1 = ()
point2 = ()


def mouse_drawing(event, x, y, flag, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circle.append((x,y))
        if not drawing:
            point1 = (x,y)
            drawing = True
        else:
            drawing = False

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            point2 = (x,y)


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_drawing)

circle = []
while True:
    _, frame = cap.read()

    for c in circle:
        cv2.circle(frame, c, 5, (0, 0, 255), -1)

    if point1 and point2:
        cv2.rectangle(frame,point1,point2,(0,255,0),2)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()