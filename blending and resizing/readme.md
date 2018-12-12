# General info for first timers

- Two images are required for blending of images firstly we need to make sure that two images must have same height,width for performing this operation


-The image can be resized by by inbuilt functions of opencv library first the size of image is Known using image.shape function upon passing the function we will get three parameters 
these parameters tell us width,height and number of features of image that is blue,green,red values.The third value should not be altered.


# points to be done
-
-we pass the function cv2.resize(im1,dim,interpolation=cv2.INTER_AREA) to resize the image 1 the interpolation in the given arguments is a technicque out of many possible things that can be tried
the dime function here stores two value i.e, width and height in same sequence and im1 tells us the image on which the operation is to be performed.

# we should keep in mind that

-This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. Images are added as per the equation below:

-g(x) = (1 - \alpha)f_{0}(x) + \alpha f_{1}(x)

-By varying \alpha from 0 \rightarrow 1, you can perform a cool transition between one image to another.

-Here I took two images to blend them together. First image is given a weight of 0.7 and second image is given 0.3. cv2.addWeighted() applies following equation on the image.
-
-dst = \alpha \cdot img1 + \beta \cdot img2 + \gamma

-Here \gamma is taken as zero.
