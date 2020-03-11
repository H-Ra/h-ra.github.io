---
layout: post
title: Trying out new color segmentation method part 3
---

### Lab Work

Today, I looked at the color spaces for the three images seen in my [last post](https://h-ra.github.io/38-TryingNewColorSegmentationPt2/) in order to find similarities and differences between the sperm and eggs seen in these images. Here are the main differences that I found:

Differences in sperm coloration:

G: ![g_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/g_comparison.png?raw=true)

Y: ![Y_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Y_comparison.png?raw=true)

Differences in egg coloration:

Cr: ![Cr_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/Cr_comparison.png?raw=true)

H: ![h_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/h_comparison.png?raw=true)

V: ![v_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/v_comparison.png?raw=true)

Differences in both gonad coloration:

S: ![s_comparison.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/s_comparison.png?raw=true)

The next step done in [the article](https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/) seemed to be to generate a color plot based on the specific objects of interest. The article used 10 images of the same object in different lighting, so in order to mimic what was done in the article, I chose 10 random numbers in order to find the numbered images that I wished to use. The numbers that were generated were: 118, 122, 9, 88, 126, 152, 100, 104, 142, 130. Since there were usually multiple images associated to 1 number, I used all of the images associated to the number since it seemed like each image had eggs and sperm in a slightly different color to one another. Here are the images for reference:

9: 
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi009-40x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi009-40x-tiled2.jpg?raw=true)

88:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi088-10x-tiled.jpg?raw=true)

100:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi100-10x-2.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi100-10x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi100-10x-tiled.jpg?raw=true)

104:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi104-10x-tiled.jpg?raw=true)

118:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi118-10x-tiled-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi118-10x-tiled.jpg?raw=true)

122:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi122-10x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi122-10x-tiled-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi122-10x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi122-10x.jpg?raw=true)

126:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi126-10x-tiled-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi126-10x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi126-20x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi126-20x.jpg?raw=true)

130:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi130-10x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi130-10x-tiled-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi130-10x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi130-10x.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi130-60x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi130-60x.jpg?raw=true)

142:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi142-10x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi142-10x-tiled-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi142-10x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi142-10x.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi142-40x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi142-40x.jpg?raw=true)

152:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi152-10x-tiled-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi152-10x-tiled.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi152-40x-2-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi152-40x-2.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi152-40x-scale.jpg?raw=true)
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi152-40x.jpg?raw=true)

Since it seemed like the images for 126 were just filled with parasites, I did not include it when looking for gonad images to screenshot. 

I used these images along with 3 original images and screenshot out segments with only egg and only sperm. 

---

### Next Steps

I will run these screenshot images through a script so that I can find a threshold to use for color segmentation via a color plot. 


