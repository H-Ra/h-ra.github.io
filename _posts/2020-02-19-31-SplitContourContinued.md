---
layout: post
title: February 19, 2020 - A step closer to figuring out how to split the contour?
---

### Lab Work

Today, I continued to try and split the contour seen in this image: 

![segmentation_reduced_threshold.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/segmentation_reduced_threshold.PNG?raw=true)

in order to measure each of the eggs separately. 

Sources that I used that were helpful: 

1. [Contours : More Functions](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_more_functions/py_contours_more_functions.html)

2. [Contour Features](https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html)

I think I got a better understanding of how convexhull and convexity defects work in OpenCV, and was able to produce these points (red is the convexhull points and teal is the convexity defect points):

![hull&defect.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/hull&defect.PNG?raw=true)

and I was also able to find the best-fit ellipse around it:

![ellipse.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/ellipse.PNG?raw=true)

I think a possible way to separate the contour would be to: 

1. find the convexhull for the contour of interest
2. find the convexity defects for the contour of interest
3. make a distance threshold between  the convexhull and convexity defects points
4. make a distance threshold between the convexity defects themselves
3. make a bounding box/ellipse around the contour of interest 
4. find angle of the bounding box/ellipse 
	* if the angle of two convexity defect points within a certain distance threshold is within a certain range, then connect those points. 
	* for clusters that go all the way around in a circle, find angle range between horizontal and vertical axes

I will have to test this method to see if it is a viable way to separate the contour.

---

### Next Steps

Continue to figure out how to separate the contour 