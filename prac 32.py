import numpy as np 
import cv2 
  
# creating array using np.zeroes() 
array = np.zeros([500, 500, 3], 
                 dtype = np.uint8) 
  
# setting RGB color values as 255,255,255 
array[:, :] = [255, 255, 255]  
  
# displaying the image 
cv2.imshow("image", array) 
