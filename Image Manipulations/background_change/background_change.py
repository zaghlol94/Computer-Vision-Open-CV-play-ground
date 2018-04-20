# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:49:32 2018

@author: zaghlollight
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('index.png')

image_copy = np.copy(img)

img.shape
# Change color to RGB (from BGR)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

# Display the image copy
plt.imshow(image_copy)

lower_green = np.array([0,200,0]) 
upper_green = np.array([250,255,250])

mask = cv2.inRange(image_copy, lower_green, upper_green)

mask.shape
# Vizualize the mask
plt.imshow(mask, cmap='gray')

masked_image = np.copy(image_copy)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)


# Load in a background image, and convert it to RGB 
background_image = cv2.imread('2.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:252, 0:362]

# Mask the cropped background so that the pizza area is blocked
crop_background[mask == 0] = [0, 0, 0]

# Display the background
plt.imshow(crop_background)

complete_image = masked_image + crop_background

# Display the result
plt.imshow(complete_image)