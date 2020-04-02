---
layout: post
title: April 2, 2020 - Continuing New Color Segmentation Method
---

### Lab Work 

Today, I continued to try and find a new method in color segmentation to increase accuracy in individual egg measurements. Last time, I was able to combine multiple images together to form one larger image, which helped me to plot a color space graph that would help in the color segmentation, but was not able to combine all of the images that I wanted to. So, in order to find a way to combine all of the images, I used these sources:

1. [Python: Concatenate 2 irregular sized images by automatically detecting the sizes](https://stackoverflow.com/questions/47328846/python-concatenate-2-irregular-sized-images-by-automatically-detecting-the-size)
2. [Python OpenCV: Concatenating images](https://techtutorialsx.com/2020/02/18/python-opencv-concatenating-images/)
3. [In python, how can I use regex to replace square bracket with parentheses](https://stackoverflow.com/questions/14949090/in-python-how-can-i-use-regex-to-replace-square-bracket-with-parentheses)

From these sources, I was able to produce this image (which consists of all of the egg images that I screenshotted):

![final_image.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/final_image.jpg?raw=true)

and subsequently this graph:

![final_image_color_plot.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/final_image_color_plot.png?raw=true)

---

### Next Steps

Analyze the graphs to find a better color threshold for segmentation