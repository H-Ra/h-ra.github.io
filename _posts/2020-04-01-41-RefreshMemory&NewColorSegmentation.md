---
layout: post
title: April 1, 2020 - Refreshing Memory on Lab Work so far and Continuing New Image Segmentation Method 
---

### Lab Work

After coming back from spring break, today I looked back at the work that I did last quarter to refresh my memory and then began to continue working on the new method of color segmentation that I was doing. 

In my [last post](https://h-ra.github.io/40-TryingNewColorSegmentationMethodPt4/), I discovered that I could visualize the color space of the image by the specific gonad (egg or sperm) that I wanted to analyze to produce graphs like this:

![color_plot1.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_plot1.png)

But, I was only able to do this with one image of a gonad at a time, instead of seeing all of the gonads at once. So, I combined __*most*__ of the images together using the help of [this source](https://stackoverflow.com/questions/47254294/how-to-concatenate-images-of-different-shapes-using-python-and-opencv) to produce a graph that looks like this:

![new_color_plot.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/new_color_plot.png?raw=true)

I emphasize "most" because for some reason, I was not able to combine all of the images together... This is something I will have to look into moving forward.

---

### Next Steps

1. Figure out how to combine __*all*__ of the images together