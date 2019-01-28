import cv2
import numpy as np
from matplotlib import pyplot as plt


original_image = cv2.imread('goalkeeper.jpg')
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
roi_image = cv2.imread('pitch_ground.jpg')
hsv_roi = cv2.cvtColor(roi_image, cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])


mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# Filter to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.filter2D(mask, -1, kernel)
_, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)

mask = cv2.merge((mask,mask,mask))
result = cv2.bitwise_and(original_image, mask)

cv2.imshow("mask", mask)
cv2.imshow("result", result)
# plt.imshow(roi_hist)
# plt.show()

cv2.imshow("original_image", original_image)
cv2.imshow("Roi", roi_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
