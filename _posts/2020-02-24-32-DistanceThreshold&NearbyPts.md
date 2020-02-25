---
layout: post
title: February 24, 2020 - Testing out Distance threshold & Separating contour through nearby points
---

### Lab Work

Today, I continued to try and figure out how to segment the contour around the eggs in this image (green contour on left side of image):

![segmentation_result_162.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/segmentation_result_162.PNG?raw=true)

To figure out how to measure each of the eggs separately. 

Last week, I thought of a possible method to split the contour: 

1. find the convexhull for the contour of interest
2. find the convexity defects for the contour of interest
3. make a distance threshold between  the convexhull and convexity defects points
4. make a distance threshold between the convexity defects themselves
3. make a bounding box/ellipse around the contour of interest 
4. find angle of the bounding box/ellipse 
	* if the angle of two convexity defect points within a certain distance threshold is within a certain range, then connect those points. 
	* for clusters that go all the way around in a circle, find angle range between horizontal and vertical axes

In order to test if this would be a viable way to split the contour, I started by trying to visualize all of the distances between the convexhull points and the convexity defect points, which resulted in this image:

![convex&defect_lines.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/convex&defect_lines.PNG?raw=true)

After looking at this image, I realized that it might be very difficult to create a distance threshold, so I would probably have to try and find different ways to split the contour.

When looking at the image more, I realized that many of the convexity defect points are the innermost point of a contour in a local area, and so if a perpendicular line is made based off of the line that consists of the points that are immediately to the right and the left of the innermost point, then that could be a possible way to split the contour: 

After using these equations and sources below:
 
1. [Finding the index of a numpy array in a list
](https://stackoverflow.com/questions/41271997/finding-the-index-of-a-numpy-array-in-a-list)
2. euclidean distance
3. midpoint formula
4. point slope equation 
5. perpendicular line equation 

This was the output:

![midpoint%20division.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/midpoint%20division.PNG?raw=true)

This seems like a good start to figuring out how to split the contour, so I think that I will try and continue to improve this method and see if a promising result turns out. 

---

### Next Steps

Continue to try and improve current method being used to split the contour
