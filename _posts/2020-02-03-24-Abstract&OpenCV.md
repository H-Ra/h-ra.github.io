---
layout: post
title: February 3, 2020 - Preliminary Stages of Abstract for Undergraduate Research Symposium and Increasing Accuracy of Color Segmentation using OpenCV
---

### Lab Work

__Undergraduate Research Symposium Abstract__

In order to improve my science communications skills, I plan on presenting the work I have done on the O. angasi project at the UW Undergraduate Research Symposium this May. In order to present at the symposium, I need to submit an abstract summarizing the project that I am working on. Thus, I have started to look at abstracts from past symposia and looking at tips on writing abstracts in order to create a successfully written abstract. Below are the links to these resources:

1. [Symposium Abstract Writing Workshop Presentation](https://drive.google.com/file/d/1K_9sy9Tm8Zcd5Odcd-b6O4aw7ck7kW3x/view)
2. [2019 Symposium Abstract Examples](https://expo.uw.edu/expo/apply/534/proceedings)

I will start creating a draft for the abstract tomorrow. 

__Improving Accuracy of Color Segmentation using OpenCV__

Last time, I was able to create an threshold output that segmented the male gonad in the image by color, but one issue with this was that it was not able to identify all of the male gonad in the image (original image above, threshold result below):

original:

![20180924-angasi121-40x.jpg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi121-40x.jpg?raw=true)

Male gonad color segmentation result:

![color_threshold_result.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_threshold_result.PNG?raw=true)

I tried this thresholding method again with the female gonad to see if there would be a possibly improved result, but trying to only threshold for the female gonad turned out to be more difficult because some of the male gonad was also included in the output (see image below). 

female gonad color segmentation result: 

![female_gonad_color_segmentation.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/female_gonad_color_segmentation.PNG?raw=true)

Thus, I thought a good next step would be to find the areas of the segmented objects in order to find a way to improve the thresholding technique. I used these sources to learn how to find and label areas of male and female gonad:

1. [How to detect area of pixels with the same color using OpenCV](https://stackoverflow.com/questions/12143504/contours-counting-and-labeling)
2. [OpenCV: How to find the area of a specific contour
](https://stackoverflow.com/questions/57264916/opencv-how-to-find-the-area-of-a-specific-contour)

I was able to find the total area of the segmented areas, which turned out to be:

"Female Gonad" Total Area: 6018.0
"Male Gonad" Total Area: 47318.0

I am assuming that the values are in terms of pixels, but I will have to research more into that just to make sure. 

---

### Next Steps

1. Begin writing abstract for undergraduate research symposium
2. Figure out how to label and calculate area of different contours _separately_

