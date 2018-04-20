# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:15:12 2018

@author: zaghlollight
"""

import cv2
import numpy as np

# Grayscale and Canny Edges extracted
image = cv2.imread('soduku.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 170, apertureSize = 3)

# Again we use the same rho and theta accuracies
# However, we specific a minimum vote (pts along line) of 100
# and Min line length of 5 pixels and max gap between lines of 10 pixels
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 200, 5, 10)
print (lines.shape)

for i in range(0,lines.shape[0]):
    for x1, y1, x2, y2 in lines[i]:
            cv2.line(image, (x1, y1), (x2, y2),(0, 255, 0), 3)


cv2.imshow('Probabilistic Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Run HoughLines using a rho accuracy of 1 pixel
# theta accuracy of np.pi / 180 which is 1 degree
# Our line threshold is set to 240 (number of points on line)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 240)

# We iterate through each line and convert it to the format
# required by cv.lines (i.e. requiring end points)
for i in range(0,lines.shape[0]):
     for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    

cv2.imshow('Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blob detection 

image = cv2.imread("Sunflowers.jpg")
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs.
keypoints = detector.detect(image)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
# the circle corresponds to the size of blob
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,255),
                                      cv2.DRAW_MATCHES_FLAGS_DEFAULT)
 
# Show keypoints
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


#cv2.DRAW_MATCHES_FLAGS_DEFAULT
#cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
#cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
#cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS


