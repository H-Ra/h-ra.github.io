---
layout: post
title: January 22, 2020 - Tensorflow update and Trying out OpenCV
--- 

### Lab Work 

Today, I looked a little more into how to use tensorflow in order to analyze the histology images using Python, but after reading more about tensorflow, it seems like tensorflow would be too complex to use for now, so it may be useful to look at other Python programs as well. 

One program that I saw that could potentially use is blob detection in OpenCV, which can help to detect shapes in images. I used a variety of sources to learn more about blob detection in OpenCV including, but not limited to:
1. [Blob Detection Using OpenCV ( Python, C++ )](https://www.learnopencv.com/blob-detection-using-opencv-python-c/)
2. [https://www.learnopencv.com/blob-detection-using-opencv-python-c/](https://stackoverflow.com/questions/42203898/python-opencv-blob-detection-or-circle-detection)

It seemed like [Blob Detection Using OpenCV ( Python, C++ )](https://www.learnopencv.com/blob-detection-using-opencv-python-c/) did a really great job at explaining how to use blob detection with OpenCV, and thus I tried to do a blob detection with one of histology images by using the script shown in the article as a way to see if it would work, but once I ran it, this error seemed to pop up:  

__error: (-215:Assertion failed) !outImage.empty() in function 'drawKeypoints'__

I am not sure why I got this error, but I think trying to debug it and running it again is a good next step to understand how I could possibly analyze the histology methods using this method. I also saw that you could possibly use matplotlib in order to detect shapes, so I may try using that in the future as well. 

--- 

### Next Steps

1. Debug script for opencv blob detection
2. Possibly use matplotlib blob detection