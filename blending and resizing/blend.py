import cv2
import numpy as np 
im1=cv2.imread(file location,1)
im2=cv2.imread(file location,1)
print(im2.shape)
print(im1.shape)
width=720
height=640
width2=720
height2=640
dim2=(width2,height2)

dim=(width,height)
#resized image
resized=cv2.resize(im1,dim,interpolation=cv2.INTER_AREA)
resized1=cv2.resize(im2,dim2,interpolation=cv2.INTER_AREA)
print(resized.shape)
print(resized1.shape)
dst=cv2.addWeighted(resized,0.7,resized1,0.3,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
