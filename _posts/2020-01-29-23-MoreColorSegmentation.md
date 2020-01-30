---
layout: post
title: January 29, 2020 - Looking more into Color Segmentation
---

### Lab Work

Today, I continued to look into the color segmentation abilities of OpenCV and Python using this article --> [Image Segmentation Using Color Spaces in OpenCV + Python](https://realpython.com/python-opencv-color-spaces/), and tried to troubleshoot some of the issues I had been having with the program yesterday. 

__Troubleshooting Issues from Yesterday__

Issue 1: Slow output time

- Since the computer I was using so far was really slow in terms of the color scatter plots that were created, I used a computer with a higher processing power to see if that would help in terms of speed. 
- Using a different computer actually did help with getting an output faster. One thing to note though is that it still takes a long time to move the plot if I want to see it at different angles. This makes me think that the reason why the output is slow may not only have to do with the computer itself, but it may also have to do with the fact that there is just a lot of data in the output. 

Issue 2: Not being able to get the correct color range values

- Yesterday, I was having difficulty getting the correct color range in order to threshold the image in the way that I wanted to. For this image, I wanted to threshold it so that only the male gonad would be analyzed, and in order to do that I needed to create a color range in purple. But, when I tried doing this by looking at the scatter plot that was created, the resulting color outputs were not purple at all:

![color_range_incorrect.png](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_range_incorrect.png?raw=true)

- I solved this issue by looking at the image of the scatter plot in Image J and looking at the associated RGB value of the color point of interest. After finding the color values through this method, I got the color range that I was looking for:

![color_range_correct.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_range_correct.PNG?raw=true)

__New Updates__

After getting the correct color range that I wanted, I thresholded the image, and this is the result(upper image) compared to the original image(lower image):

resulting image:
![color_threshold_result.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_threshold_result.PNG?raw=true)

original image:
![20180924-angasi121-40x.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi121-40x.jpg?raw=true)

The program did quite a nice job at only highlighting the male gonad, but it still missed some areas where there is male gonad. This may mean that I have to widen the color range for thresholding a bit more. 

---

### Next Steps

1. Look more into how to make the color range for thresholding more accurate