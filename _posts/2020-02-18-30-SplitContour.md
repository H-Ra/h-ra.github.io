---
layout: post
title: February 18, 2020 - Continuing to Figure out how to split a single contour
--

### Lab Work

Today, I continued to try and figure out ways to split the large contour in this image:

![angasi162-40x-scale.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi162-40x-scale.png?raw=true)

to its respective egg contours in order to be able to measure each egg in the image separately.

I found these sources that could potentially be useful to helping achieve this goal:

1. [Segmentation - Separating Touching Objects
](https://stackoverflow.com/questions/23895640/segmentation-separating-touching-objects)

2. [OpenCV cvFindContours - how do I separate components of a contour
](https://stackoverflow.com/questions/6044119/opencv-cvfindcontours-how-do-i-separate-components-of-a-contour)

3. [How do I split a contour?](https://answers.opencv.org/question/174546/how-do-i-split-a-contour/)

4. [Detach blobs with a contact point](https://answers.opencv.org/question/87583/detach-blobs-with-a-contact-point/)

5. [Detach two blob](https://answers.opencv.org/question/56042/detach-two-blob/)

6. [Drawing convexHull in openCV2 Python](https://stackoverflow.com/questions/41508775/drawing-convexhull-in-opencv2-python)

7. [Understanding Distance Transform in OpenCV](https://stackoverflow.com/questions/22563838/understanding-distance-transform-in-opencv)

__ImageJ__

I tried implementing the watershed algorithm in imageJ today, and the results were slightly better than the results that I had gotten from using OpenCV, but there were still signs of oversegmentation. 

Original Image:

![angasi162-40x-scale.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi162-40x-scale.png?raw=true)

Turn into Binary:

![binary_imagej.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/binary_imagej.png?raw=true)

Fill in Holes:

![fillholes_imagej.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/fillholes_imagej.png?raw=true)

Watershed Segmentation:

![watershed_imagej.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/watershed_imagej.png?raw=true)

---

### Next Steps

Continue to figure out how to split contour