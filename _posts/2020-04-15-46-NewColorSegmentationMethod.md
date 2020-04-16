---
layout: post
title: April 15, 2020 - Looking at more Images using New Color Segmentation Method
---

### Lab Work

Today, I used the color thresholds found in [my last post](https://h-ra.github.io/45-NewColorSegmentationMethod/) for female gonad identification on a few more images to see the overall best color space to use in order to segment these images via color segmentation. In order to find the most accurate color space in an unbiased way, I used a random number generator to pick out 10 random images to segment. The numbers that were chosen were 153, 77, 10, 27, 94, 38, 154, 134, 179, 104. These numbers were then associated to the sample number of each image. The segmented results are shown below:

__image: 20180924-angasi179-10x-scale__

__original__

![angasi179-10x-scale](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi179-10x-scale.jpg?raw=true)

__BGR__

![angasi179_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179_bgr.png?raw=true)

__HSV__

![angasi179_hsv.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179_hsv.png?raw=true)

__YCrCb__

![angasi179_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179_ycrcb.png?raw=true)

__Lab__

![angasi179_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179_lab.png?raw=true)

__image: 20180924-angasi154-10x-tiled-scale__

__original__

![angasi154-10x-tiled-scale](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi154-10x-tiled-scale.jpg?raw=true)

__BGR__

![angasi154_bgr](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi154_bgr.png?raw=true)

__HSV__

![angasi154_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi154_hsv.png?raw=true)

__YCrCb__

![angasi154_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi154_ycrcb.png?raw=true)

__Lab__

![angasi154_lab](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi154_lab.png?raw=true)

__image: 20180924-angasi134-10x__

__original__

![angasi134-10x.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi134-10x.jpg?raw=true)

__BGR__

![angasi134_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi134_bgr.png?raw=true)

__HSV__

![angasi134_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi134_hsv.png?raw=true)

__YCrCb__

![angasi134_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi134_ycrcb.png?raw=true)

__Lab__

![angasi134_lab](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi134_lab.png?raw=true)

__image: 20180924-angasi153-10x-tiled-scale__

__original__

![angasi153-10x-tiled-scale](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi153-10x-tiled-scale.jpg?raw=true)

__BGR__

![angasi153_bgr](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi153_bgr.png?raw=true)

__HSV__

![angasi153_hsv.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi153_hsv.png?raw=true)

__YCrCb__

![angasi153_ycrcb.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi153_ycrcb.png?raw=true)

__Lab__

![angasi153_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi153_lab.png?raw=true)

__image: 20180924-angasi104-10x-tiled__

__original__

![angasi104-10x-tiled](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi104-10x-tiled.jpg?raw=true)

__BGR__

![angasi104_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi104_bgr.png?raw=true)

__HSV__

![angasi104_hsv.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi104_hsv.png?raw=true)

__YCrCb__

![angasi104_ycrcb.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi104_ycrcb.png?raw=true)

__Lab__

![angasi104_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi104_lab.png?raw=true)

__image: 20180924-angasi094-10x-tiled__

__original__

![angasi094-10x-tiled](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi094-10x-tiled.jpg?raw=true)

__BGR__

![angasi94_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94_bgr.png?raw=true)

__HSV__

![angasi94_hsv.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94_hsv.png?raw=true)

__YCrCb__

![angasi94_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94_ycrcb.png?raw=true)

__Lab__

![angasi94_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94_lab.png?raw=true)

__image: 20180924-angasi077-10x-tiled__

__original__

![angasi077-10x-tiled](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi077-10x-tiled.jpg?raw=true)

__BGR__

![angasi77_bgr](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi77_bgr.png?raw=true)

__HSV__

![angasi77_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi77_hsv.png?raw=true)

__YCrCb__

![angasi77_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi77_ycrcb.png?raw=true)

__Lab__

![angasi77_lab](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi77_lab.png?raw=true)

__image: 20180924-angasi038-10x-tiled__

__original__

![angasi038-10x-tiled.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi038-10x-tiled.jpg?raw=true)

__BGR__

![angasi38_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi38_bgr.png?raw=true)

__HSV__

![angasi38_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi38_hsv.png?raw=true)

__YCrCb__

![angasi38_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi38_ycrcb.png?raw=true)

__Lab__

![angasi38_lab](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi38_lab.png?raw=true)

__image: 20180924-angasi027-10x-tiled__

__original__

![angasi027-10x-tiled.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi027-10x-tiled.jpg?raw=true)

__BGR__

![angasi27_bgr](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi27_bgr.png?raw=true)

__HSV__

![angasi27_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi27_hsv.png?raw=true)

__YCrCb__

![angasi27_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi27_ycrcb.png?raw=true)

__Lab__

![angasi27_lab](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi27_lab.png?raw=true)

__image: 20180924-angasi010-40x-tiled__

__original__

![angasi010-40x-tiled.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi010-40x-tiled.jpg?raw=true)

__BGR__

![angasi10_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi10_bgr.png?raw=true)

__HSV__

![angasi10_hsv.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi10_hsv.png?raw=true)

__YCrCb__

![angasi10_ycrcb.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi10_ycrcb.png?raw=true)

__Lab__

![angasi10_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi10_lab.png?raw=true)

After segmenting those images, I thought it would be helpful to also see how well the color segmentations were for male gonad identification as well. So, I looked at the density plots that were made for male gonad identification and these were the resulting thresholds that I produced for all 4 color spaces:

__BGR__: min = [55, 0, 60] & max = [180, 115, 225]

__HSV__: min = [90, 15, 75] & max = [170, 250, 225]

__YCrCb__: min = [25, 115, 125] & max = [130, 225, 180]

__Lab__: min = [30, 120, 75] & max = [140, 210, 140]

Using these threshold values, these segmented images were produced:

__image: 20180924-angasi179-10x-scale__

__BGR__

![angasi179s_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179s_bgr.png?raw=true)

__HSV__

![angasi179s_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179s_hsv.png?raw=true)

__YCrCb__

![angasi179s_ycrcb](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179s_ycrcb.png?raw=true)

__Lab__

![angasi179s_lab](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi179s_lab.png?raw=true)

__image: 20180924-angasi094-10x-tiled__

__BGR__

![angasi94s_bgr.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94s_bgr.png?raw=true)

__HSV__

![angasi94s_hsv.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94s_hsv.png?raw=true)

__YCrCb__

![angasi94s_ycrcb.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94s_ycrcb.png?raw=true)

__Lab__

![angasi94s_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94s_lab.png?raw=true)

As is probably apparent, it seems like the color thresholds were not as accurate for the male gonad as it was for identifying the presence of female gonad, and thus, I tried to screenshot each sperm cell that was present in an image rather than a cluster of sperm cells, which produced this combined image:

![final_image_s_new](https://github.com/H-Ra/h-ra.github.io/blob/master/images/final_image_s_new.jpg?raw=true)

Using this new image, I found new color thresholds for the color spaces that were very different from the original color thresholds found:

__BGR__: min = [50, 0, 65] & max = [155, 50, 165]

__HSV__: min = [140, 130, 60] & max = [165, 250, 170]

__YCrCb__: min = [25,145,130] & max = [75,200,180]

__Lab__: min = [35, 155, 65] & max = [100, 195, 130]

I then tried to segment one image as a test, and the results were much better than what was originally produced:

__image: 20180924-angasi094-10x-tiled__

__BGR__

![angasi94snew_bgr](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94snew_bgr.png?raw=true)

__HSV__

![angasi94snew_hsv](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94snew_hsv.png?raw=true)

__YCrCb__

![angasi94snew_ycrcb.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94snew_ycrcb.png?raw=true)

__Lab__

![angasi94snew_lab.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi94snew_lab.png?raw=true)

---

### Next Steps

Analyze which color space is best to segment both male and female gonad in images 
