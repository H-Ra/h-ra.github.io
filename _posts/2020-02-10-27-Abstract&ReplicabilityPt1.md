---
layout: post
title: February 10, 2020 - Continuing to Improve Abstract and Seeing Replicability of Image Segmentation
---

### Lab Work

Today, I continued to look through the abstract for the Undegraduate Research Symposium and edited it according to the comments that Laura gave me. Dr. Roberts and Laura approve of it so I will include it in my application and send it in by Wednesday!

Today, I also tested the [script](https://github.com/H-Ra/h-ra.github.io/blob/master/O_angasi/segmentation_color.py) that I have been using on another image today to analyze its replicability, and overall, it did a pretty good job once again (see resulting images below):

Figuring out color ranges on color scatter plot: 

![rgb_scatter_162.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/rgb_scatter_162.PNG?raw=true)

Resulting Threshold Image:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/segmentation_result_162.PNG?raw=true)

Another thing that I figured out along the way was how to make the resulting image in RGB instead of BGR, which is great! In addition, I have created a protocol for how I am currently doing the image segmentation [here](https://github.com/H-Ra/h-ra.github.io/blob/master/O_angasi/O.%20angasi%20Gonad%20Image%20Segmentation%20Protocol.md), and I will improve it over time as I improve the methodology itself. 

But, although the script did a pretty good job, there is still definitely room for improvement. For example, not all of the pink female gonad was marked in the image. So, in order to fix this, I reduced the size threshold, and this is the resulting output:

![segmentation_reduced_threshold.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/segmentation_reduced_threshold.PNG?raw=true)

The size threshold seemed to help a little, but there is still some missing gonad that I would like for the script to recognize. 

An additional problem that I noticed is that there are a lot less objects being identified as eggs than there are actual eggs present in the image:

![gonad_count.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/gonad_count.PNG?raw=true) 

Once I looked into it some more, I realized that the reason for this is because there is one huge group of eggs that are clustered together, and this group is being counted as 1 egg because they are all connected to each other. This would still be a viable way to figure out what sex the organism is (male only, female only, hermaphrodite predominantly male, hermaphrodite predominantly female, etc...), but it is not a viable way to measure each individual egg in the image. Thus, I might have to add circularity as a factor to measure each egg or utilize another function such as a watershed algorithm. The links below may help me figure out how to use the watershed algorithm in OpenCV:

1. [Image Segmentation with Watershed Algorithm](https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html)
2. [Watershed OpenCV](https://www.pyimagesearch.com/2015/11/02/watershed-opencv/)


Something that might be useful in the future - if want to find nucleus size, I could use something like (I found this out through this [link](https://stackoverflow.com/questions/8830619/difference-between-cv-retr-list-cv-retr-tree-cv-retr-external)):

* RETR_TREE 

instead of

* RETR_EXTERNAL

to produce images such as this:

![segmentation_RETR_TREE.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/segmentation_RETR_TREE.PNG?raw=true)

One thing that I realized while rerunning the script on a different image is that setting different color ranges for male and female gonads each time may become a hassle if I have to do that for every single image; so I may want to look into if there are patterns of coloration for male and female gonads throughout the images.

---

### Next Steps

1. See if watershed algorithm method may be a good way to separate and measure individual eggs in image
2. Find a possible pattern of coloration in order to make it easier to quantify gonadal sex and stage with less bias