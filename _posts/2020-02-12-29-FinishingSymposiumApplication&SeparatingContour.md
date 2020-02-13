---
layout: post
title: February 12, 2020 - Finishing Undergraduate Research Symposium Application & Continuing to Figure out How to Separate Objects in Image
---

### Lab Work 

__Undergraduate Research Symposium Application__

Today, I reviewed my entire Undergraduate Research Symposium Application to make sure that everything was in order before submitting it. 

__Separating Objects in Contour__

Today, I also continued to try and find ways to separate the multiple objects found in one large contour for the histological images. After looking around, I found these resources that may be useful:

1. [Detecting overlapping circles](https://answers.opencv.org/question/43195/detecting-overlapping-circles/)

2. [OpenCV Splitting Contours](https://stackoverflow.com/questions/41402137/opencv-splitting-contours)

3. [Opencv divide a contour in two sections
](https://stackoverflow.com/questions/36012719/opencv-divide-a-contour-in-two-sections)

4. [Opencv divide contacted circles into single](https://stackoverflow.com/questions/34650697/opencv-divide-contacted-circles-into-single)

5. [Eroding and Dilating](https://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html)

6. [Structural Analysis and Shape Descriptors](https://docs.opencv.org/3.0-last-rst/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=contourarea)

7. [How to divide contours?
](https://stackoverflow.com/questions/53582446/how-to-divide-contours/54829442#54829442)

8. [The best way of separating overlapping objects?
](https://www.researchgate.net/post/The_best_way_of_separating_overlapping_objects)

The main ideas that I got through these resources was to try and use the __angles__ of the contours or use __convexhull and find the maximum local distance__ as ways of splitting the contour. I will have to look at the suggestions made in these posts and apply them to possibly find a solution.

---

### Next Steps

Keep trying to figure out a way to split the contour into the corresponding separate objects