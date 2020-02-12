---
layout: post
title: February 11, 2020 - Figuring Out How to Segment out Individual Objects in a Large Contour
---

### Lab Work

Today, I tried to figure out a way of segmenting the images in a more accurate way so that I could measure the individual eggs in an image. As seen in the [last post](https://h-ra.github.io/27-Abstract&ReplicabilityPt1/), even though the script does a pretty good job at parsing out the individual objects in an image, if there are multiple objects connected to each other, then these objects are counted as one large object. 

__cv2.watershed__

Thus, one of the first things that I thought might be helpful to use in order to solve this issue was a watershed algorithm. I tried running this, but the result was not very promising.

It seemed like there were areas of the image that were undersegmented and also parts of the image that were oversegmented. 

Thus, I started to find a way to segment the image without using a watershed algorithm. I realized that since there are definitive edges in each object that is contoured, then there must be a way to identify the presence of these edges. If there is way to say that when certain edges are in a certain formation, form a line between each edge, then "circles" of each object would be formed, hypothetically. 

In order to see if this plan would actually work, the first step is to see if we can actually identify the edges of the contour.

__cv2.goodFeaturesToTrack__

After looking around, I found that the command cv2.goodFeaturesToTrack might be a possible way to find the edges of the contour that I want. But after trying it out on the image, the results were not promising:

![goodFeaturesToTrack.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/goodFeaturesToTrack.png?raw=true)

I think this can be attributed to the fact that the command takes into consideration the whole image rather than the specific contour that you would like to be segmented. 

__cv2.convexHull and cv2.convexityDefects__

While looking around, I also saw that the commands cv2.convexHull and cv2.convexityDefects may be a viable way to find the edges of the contour. After running the script with these commands, the results were more promising, but there is still definitely room for improvement: 

![convex_concave.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/convex_concave.PNG?raw=true)

__cv2.approxPolyDP__

Finally, I saw that the command cv2.approxPolyDP may be a viable way of obtaining the points needed. After running the script under a variety of parameter ranges, I saw that the results may be more promising than the other commands that were used:

Larger epsilon value:
![approxPoly_image.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/approxPoly_image.PNG?raw=true)

Smaller epsilon value:

![approxPoly_image_better.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/approxPoly_image_better.PNG?raw=true)

These were the sources that I used to help me find and figure out how to use the commands stated above: 

1. [Image Segmentation in openCV
](https://stackoverflow.com/questions/50945444/image-segmentation-in-opencv)

2. [Single blob, multiple objects (Ideas on how to separate objects)](https://answers.opencv.org/question/71691/single-blob-multiple-objects-ideas-on-how-to-separate-objects/)

3. [Feature Detection](https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html?highlight=goodfeaturestotrack)

4. [Structural Analysis and Shape Descriptors](https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html)

5. [Determine concave point
](https://stackoverflow.com/questions/52453040/determine-concave-point)

6. [OpenCV - using cv2.approxPolyDP() correctly
](https://stackoverflow.com/questions/41879315/opencv-using-cv2-approxpolydp-correctly)

---

### Next Steps

1. Continue to try and improve the accuracy of segmentation (possibly using a combination of cv2.convexHull, cv2.convexityDefects, and cv2.approxPolyDP. 

