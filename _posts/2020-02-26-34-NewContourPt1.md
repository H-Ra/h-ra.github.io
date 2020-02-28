---
layout: post
title: February 26, 2020 - Making New Contours Part 1
---

### Lab Work

I continued to try and separate a large contour into individual eggs in order to try and measure each egg present in the image. I was able to figure out how to draw a line through the separation area of interest, but when analyzing the output of the line further, I saw that the output was an array of 3 sets of values, which confused me since I was anticipating only 2 (representing x and y coordinates). 

So, I looked at more sources and found these to be useful:

1. [OpenCV 3.0 LineIterator](https://stackoverflow.com/questions/32328179/opencv-3-0-lineiterator)

2. [Can cv2.polylines return the coordinates of every point that form the line?
](https://stackoverflow.com/questions/58814818/can-cv2-polylines-return-the-coordinates-of-every-point-that-form-the-line)

Thus, I was able to generate lines that consisted of many different points (seen below):

![convert_lines_to_points.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/convert_lines_to_points.PNG?raw=true)

In order to see where the points of the line and the points of the contour intersect, I created a loop, but it takes a very long time for an output to be generated, so I tried to find a faster way to look for these intersection points, but it did not seem to work. So, I will continue to try and figure out a way to find the intersection points of the contour and the line.

---

### Next Steps

Figure out a way to find intersection between contour points and line