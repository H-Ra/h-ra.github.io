---
layout: post
title: January 28, 2020 - Looking More into OpenCV Image Analysis as well as Other Methods 
---

### Lab Work

__OpenCV__

Today, I tried using Blob Detection with OpenCV again, but this time I also used a parameter specification (specifically an area parameter to possibly detect only larger-sized blobs), but it did not seem to affect what blobs were detected (no new blobs were detected from the norm). It may be that the histology images are too complex for the program to detect big shapes in the image.

Apparently, OpenCV also has a [Image Segmentation with Watershed Algorithm](https://docs.opencv.org/3.2.0/d3/db4/tutorial_py_watershed.html) that can be used, which could possibly be much more precise than the blob detector with OpenCV. 

OpenCV also has a way in which you can segment an image based off of color, which actually also may be more useful than the Blob Detection because then we could possibly separate the gonads in the image based on sex (purple is male gonad and pink is female gonad). 

I used this tutorial on [Image Segmentation Using Color Spaces in OpenCV + Python](https://realpython.com/python-opencv-color-spaces/) to guide me through the process on an example image (see image below):

![20180924-angasi121-40x.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi121-40x.jpg?raw=true)

This is the RGB scatter plot that was produced:

![RGB scatter plot](https://github.com/H-Ra/h-ra.github.io/blob/master/images/RGB%20scatter%20plot.png?raw=true)

This is the HSV scatter plot that was produced:

![HSV scatter plot](https://github.com/H-Ra/h-ra.github.io/blob/master/images/HSV%20scatter%20plot.png?raw=true)

One main problem with producing these scatter plots is that they take a really long time to produce, but that may be due to the processing power of my computer. Thus, it may be useful to try this again on another computer with better processing power to see if it takes less time to produce these images. 

I am still also having trouble finding the range of colors to choose when deciding what parts of the image I want to segment. When I try to estimate the color ranges from the scatter plot, I seem to get completely different colors than what I had assumed. For example, this is the colors that I got when I tried to estimate for the light purple (supposed to be left plot) and dark purple (supposed to be right plot) in the image:

![color_range_incorrect.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_range_incorrect.png?raw=true)

As you can see, the colors produced seem to be in the shade of blue/green, instead of shades of purple, which was the intended color. I will have to look more into this in order to choose the correct range of colors for image segmentation. 

__MATLAB__

After researching on alternate methods of image segmentation, I found that MATLAB might actually be a great way to segment the images manually. But, I have no experience in MATLAB, so I would have to learn how to use the program first before implementing the image segmentation app in it. 

Associated links:

1. Image segmentation using the Image Segmenter App - https://www.mathworks.com/help/images/image-segmentation-using-the-image-segmenter-app.html
2. Image Processing Toolbox - https://www.mathworks.com/products/image.html
3. Color-Based Segmentation Using K-Means Clustering - https://www.mathworks.com/help/images/color-based-segmentation-using-k-means-clustering.html
4. Detect Cell Using Edge Detection and Morphology - https://www.mathworks.com/help/images/detecting-a-cell-using-image-segmentation.html

___

### Next Steps

1. Figure out how to choose color ranges as accurately as possible in order to do image segmentation 
2. Possibly try using MATLAB to see if that would also be a viable way to analyze histology images 