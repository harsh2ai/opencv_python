import cv2
import numpy as np

def Create_blank(width,hieght,rgb_color=(0,0,0)):
    image=np.zeros((height,width,3),np.uint8)
    color=tuple(reversed(rgb_color))
    image[:]=color
    
    return image
width,height=1024,720
blue=(0,0,102)
image=Create_blank(width,height,rgb_color=blue)
r=120
r1=60
c1=720,490
d=180
h=(d/2*np.sqrt(3))
red=(0,0,310)
blu=(290,0,0)
ang=60
grn=(0,285,0)
f=(102,0,0)
cv2.circle(image,c1,r,blu,-1) #blue
cv2.circle(image,(520,150),r,red,-1) #red
cv2.circle(image,(320,490),r,grn,-1)
cv2.circle(image,c1,r1,f,-1) #blue
cv2.circle(image,(520,150),r1,f,-1) #red
cv2.circle(image,(320,490),r1,f,-1)
cv2.ellipse(image,(520,150),(r,r),ang,0,ang,125,-1)
cv2.ellipse(image,(720,490),(r,r),240,0,ang,125,-1)
cv2.ellipse(image,(320,490),(r,r),300,0,ang,125,-1)

cv2.imwrite("opencv_logho.jpg", image)
cv2.imshow("tre",image)
cv2.waitKey()
cv2.destroyAllWindows()


