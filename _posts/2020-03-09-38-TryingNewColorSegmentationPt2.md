---
layout: post
title: March 9, 2020 - Trying out New Color Segmentation Method Part 2
---

### Lab Work

Last week, I began to try and find a different way to segment the histology images by color in order to find a faster and possibly more accurate way to threshold the images instead of the method that I was previously using. The new way that I found which might be useful is seen in the article ["Color spaces in OpenCV (C++ / Python)"](https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/), and I began to follow the steps used in the article to segment images by color on this image:

![20180924-angasi022-10x-tiled.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi022-10x-tiled.PNG?raw=true)

But after looking at the article a little more, I realized that they were using mutiple images in order to compare what the color spaces look like for the same object under different lightings. Thus, I used two more images (seen below) to use as comparisons in this process:

![20180924-angasi121-40x.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi121-40x.jpg?raw=true)

![20180924-angasi162-40x-scale.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi162-40x-scale.png?raw=true)

I compared the 3 images through 4 color spaces: RGB, Lab, YCrCb, and HSV. The results are shown below: 

original: ![original_images.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/original_images.png?raw=true)
R: ![r_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/r_comparison.png?raw=true)
G: ![g_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/g_comparison.png?raw=true)
B: ![b_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/b_comparison.png?raw=true)
L: ![L_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/L_comparison.png?raw=true)
a: ![A_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/A_comparison.png?raw=true)
b: ![B(lab)comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/B(lab)_comparison.png?raw=true)
Y: ![Y_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Y_comparison.png?raw=true)
Cr: ![Cr_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Cr_comparison.png?raw=true)
Cb: ![Cb_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Cb_comparison.png?raw=true)
H: ![h_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/h_comparison.png?raw=true)
S: ![s_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/s_comparison.png?raw=true)
V: ![v_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/v_comparison.png?raw=true)

---

### Next Steps

Compare the color spaces of these images (finding similarities and differences) and continue working through the article tutorial