# David Avallone & Kelly Reynolds Computer Vision


import cv2
from matplotlib import pyplot as plt
import math
import numpy as np
import os



img = cv2.imread("archive/000/S6000S00.jpg", cv2.IMREAD_COLOR) # 0 3 6 7 8 work
  
# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,100, param1 = 50, param2 = 50, minRadius = 10, maxRadius = 115) 
# Draw circles that are detected. 

# This is used to make the background of the image black
mask = np.zeros_like(img) # create empty black image with img size

white_color    = (255, 255, 255)
line_color     = (255,   0, 255) 
filled_circle  = -1
line_thickness = 1

if detected_circles is not None: # found a circle or more than one circle
    detected_circles = np.uint16(np.around(detected_circles))  # <-- turn float to integer
    max_radius_index = np.argmax(detected_circles[0, :, 2])
    a, b, r = detected_circles[0, max_radius_index]
    
    cv2.circle(img, (a, b), r, line_color, line_thickness)
    # draw filled circle in white on black background as mask:
    mask = cv2.circle(mask, (a, b), r, white_color, filled_circle)

    # Apply mask to image
    result = cv2.bitwise_and(img, mask)

    plt.imshow(result)
    plt.show()
else:
    print("Nothing Detected")

# if detected_circles is not None:
# # Convert the circle parameters a, b and r to integers. 
#     detected_circles = np.uint16(np.around(detected_circles)) 
#     max_radius_index = np.argmax(detected_circles[0, :, 2])

#     # Draw the circumference of the largest circle
#     cv2.circle(img, (a, b), r, (0, 255, 0), 2)
#     cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

#     plt.imshow(img)
#     plt.show()

# else:
#     print("Nothing detected")