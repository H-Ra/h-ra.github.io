---
layout: post
title: January 27, 2020 - Debugging Blob Detection with OpenCV and trying out Manual Thresholding with ImageJ
---

### Working Remotely

__OpenCV Blob Detection__

Today, I tried to solve the problem that I had last time with using Blob Detection with OpenCV in order to detect shapes on the histology images. I solved the problem, which was that the images that I wanted to use for the blob detection were not in the right directory. Once I fixed that, then results such the image seen below were produced:

![blob_detection.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/blob_detection.png?raw=true)

There are two main problems with the output:

1. The output itself was too big, but there was no way to reduce the size of the screen, and thus I was not able to see the full picture. 
2.  The detector did not detect all of the blobs in the image

If I would like to continue to use this as a possible method for analyzing the histology images in the future, then I need to improve the accuracy of the detector somehow. Setting parameters for certain characteristics of the blobs may be a good place to start...

__Manual Thresholding with ImageJ__

I also tried to work with ImageJ some more today to see if manual thresholding would be a possibly effective and accurate tool to use. Here is the output that I got for one of the images:

![manual_threshold.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/manual_threshold.png?raw=true)

There are a few problems with this output: 

1. For this particular image, I was trying to threshold it so that it would only highlight the male gametes in the image, but some of the parts of the female gametes were also highlighted. This means that it may be difficult to analyze by gonad sex if I were to use this method of manual thresholding
2. Each number is supposed to represent one separate object identified in the image, but the placement of the numbers seems to be very arbitrary. 

---

### Next Steps

1. Look at Blob Detection with OpenCV more with parameter specifications
2. Look at other methods of image segmentation/object detection to help in analyzing the histology images