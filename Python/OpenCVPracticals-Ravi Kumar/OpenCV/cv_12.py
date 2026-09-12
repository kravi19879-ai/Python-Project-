# Canny Edge Detection
#1 Noise reduction
#2 Intensity of the gradient of the image
#3 Non-maximum suppression
#4 Thresholding

import cv2
import numpy as np
img=cv2.imread("C:/Users/kravi/OneDrive/Desktop/Bird.jpeg")
resize=cv2.resize(img,(500,500))
min_thresh=100
max_thresh=200
edges=cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow('Original',resize)
cv2.imshow('Edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()