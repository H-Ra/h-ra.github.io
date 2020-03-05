---
layout: post
title: March 4, 2020 - Trying out different Color Segmentation Method
---

### Lab Work

Today, I started going through the tutorial seen in this post:

[Color spaces in OpenCV (C++ / Python)](https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/)

in order to try and possibly find a more effective way to segment the images by color. 

The first thing that the post mentioned doing was splitting the image of interest into separate color channels of three types of color spaces: RGB, Lab, and YCrCb. So, I split this image:

![20180924-angasi022-10x-tiled.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi022-10x-tiled.PNG?raw=true)

into those different color channels using the help of these sources:

[Splitting Image using OpenCV in python](https://stackoverflow.com/questions/19181485/splitting-image-using-opencv-in-python)

[How to get a-channel from LAB (l*a*b) color space in python
](https://stackoverflow.com/questions/46674833/how-to-get-a-channel-from-lab-lab-color-space-in-python)

to produce these results:

_**RGB**_:

R:
![r.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/r.PNG?raw=true)

G:
![g.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/g.PNG?raw=true)

B:
![b.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/b.PNG?raw=true)

_**Lab**_:

L:
![L.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/L.PNG?raw=true)

a:
![A.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/A.PNG?raw=true)

b:
![B(lab).PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/B(lab).PNG?raw=true)

_**YCrCb**_:

Y:
![Y.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Y.PNG?raw=true)

Cr:
![Cr.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Cr.PNG?raw=true)

Cb:
![Cb.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Cb.PNG?raw=true)

---

### Next Steps

Continue to go through the tutorial 


