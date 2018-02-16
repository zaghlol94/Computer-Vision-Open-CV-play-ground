# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:03:11 2018

@author: zaghlollight
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt 
input = cv2.imread('1.jpg')
#garyscale
cv2.imshow('hello world',input)

cv2.waitKey()

cv2.destroyAllWindows()

gray=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)

cv2.imshow('gray',gray)

cv2.imwrite('out.jpg',gray)
cv2.waitKey()

cv2.destroyAllWindows()
#histogram
histogram =cv2.calcHist([input],[0],None,[256],[0,256])
plt.hist(input.ravel(),256,[0,256])
plt.show()

color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([input], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])
    
plt.show()

#draw image 
# Create a black image
image = np.zeros((512,512,3), np.uint8)

# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Black Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a diagonal blue line of thickness of 5 pixels
cv2.line(image, (0,0), (511,511), (255,127,0), 5)
cv2.imshow("Blue Line", image)
cv2.imwrite('line.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a Rectangle in
image = np.zeros((512,512,3), np.uint8)

cv2.rectangle(image, (100,100), (300,250), (127,50,127), 5)
cv2.imshow("Rectangle", image)
cv2.imwrite('rect.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a circle in
image = np.zeros((512,512,3), np.uint8)
cv2.circle(image, (350, 350), 100, (15,75,50), -1) 
cv2.imshow("Circle", image)
cv2.imwrite('circle.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw a polygon

image = np.zeros((512,512,3), np.uint8)


# Let's define four points
pts = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32)

# Let's now reshape our points in form  required by polylines
pts = pts.reshape((-1,1,2))

pts.shape

cv2.polylines(image, [pts], True, (0,0,255), 3)
cv2.imshow("Polygon", image)
cv2.imwrite('polygon.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#write on image 
image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.imwrite('write.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

