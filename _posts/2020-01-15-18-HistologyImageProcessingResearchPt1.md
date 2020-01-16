---
layout: post
title: January 15, 2020 - Histology Image Processing Research Part 1
---

### Lab Work 

Today, I looked more into possible ways to threshold and measure the eggs in the histology images in a way that was as unbiased and accurate as possible. Here are some possibly useful tools for ImageJ that could help: 

1. [Computer Assisted Sperm Analyzer (CASA)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1006691)

2. [Color Segmentation](http://bigwww.epfl.ch/sage/soft/colorsegmentation/)

3. [Color Segmentation Tool](http://isoptera.lcsc.edu/~mike/ColorSeparation/)

I learned more about the HSB (hue, saturation, brightness) parameter that can be adjusted when thresholding, and if there was some way to automatically set the HSBto a certain value which correlates to the HSB value of a male or female gonad, then I think we would be one step closer towards quantifying the histology images. But, I think we would also need to take shape (circularity) and size into consideration in order to omit other objects in the image that are not male or female gonads. 

While using ImageJ, I also noticed that the program automatically identifies the RGB value and the hex color code of whatever particular particle you are hovering over, which could also potentially be useful somehow (see image below)?

![RGB&HexColorCode_Fiji](https://github.com/H-Ra/h-ra.github.io/blob/master/images/RGB&HexColorCode_Fiji.png?raw=true)

---

I tried out the different types of auto threshold for the RGB stacks and HSB stacks that are able to be formed from an image in ImageJ, and here are the results:

original:

![colorversion_image](https://github.com/H-Ra/h-ra.github.io/blob/master/images/colorversion_image.png?raw=true)

Red(R):

![Red(R)](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Red(R).png?raw=true)

R Auto Threshold:

![auto_thresholdR](https://github.com/H-Ra/h-ra.github.io/blob/master/images/auto_thresholdR.png?raw=true)

Green(G):

![Green(G)](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Green(G).png?raw=true)

G Auto Threshold:

![auto_thresholdG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/auto_thresholdG.png?raw=true)

Blue(B):

![Blue(B)](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Blue(B).png?raw=true)

B Auto Threshold:

![auto_thresholdB](https://github.com/H-Ra/h-ra.github.io/blob/master/images/auto_thresholdB.png?raw=true)

Hue(H):

![Hue(H)](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Hue(H).png?raw=true)

H Auto Threshold:

![auto_thresholdH](https://github.com/H-Ra/h-ra.github.io/blob/master/images/auto_thresholdH.png?raw=true)

Saturation(S):

![Saturation(S)](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Saturation(S).png?raw=true)

S Auto Threshold:

![auto_thresholdS](https://github.com/H-Ra/h-ra.github.io/blob/master/images/auto_thresholdS.png?raw=true)

Brightness:

![Brightness(B)](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Brightness(B).png?raw=true)

Brightness Auto Threshold: 

![auto_thresholdBrightness](https://github.com/H-Ra/h-ra.github.io/blob/master/images/auto_thresholdBrightness.png?raw=true)

I realized that the some of the images form auto thresholds that have white objects while other images form auto thresholds with black objects. Thus, it may be useful to look into the auto thresholding parameters some more. 

---

### Next Steps

* Keep researching and trying ways to quantify the histology images

