---
layout: post
title: March 3, 2020 - Seeing Replicability of Script
---

### Lab Work

Today, I tried to see the replicability of what I have in my script so far on a new image:

![20180924-angasi022-10x-tiled.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/20180924-angasi022-10x-tiled.PNG?raw=true)

Yesterday, I was able to produce a color scatter plot for this image:

![angasi022_hsv.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi022_hsv.PNG?raw=true)

But it took a very long time to produce this plot, so I was thinking of possibly finding a different way to threshold the color values in these images overall. Another issue that I came across was once I created the scatter plot, finding the colors that actually corresponded to the eggs and sperm cells seen in the image was a lot more difficult than I had hoped for it to be. Even after I had found these color value thresholds, the output was not promising:

color threshold for eggs:

![angasi022_egg_threshold.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi022_egg_threshold.PNG?raw=true)

![angasi022_RETREXTERNAL.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi022_RETREXTERNAL.PNG?raw=true)

I tried to run the script again using different RETR, which all produced similar results:

RETR_LIST

![angasi022_RETRLIST.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi022_RETRLIST.PNG?raw=true)

RETR_TREE

![angasi022_RETRTREE.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi022_RETRTREE.PNG?raw=true)

RETR_CCOMP

![angasi022_RETRCCOMP.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi022_RETRCCOMP.PNG?raw=true)

I found a source that could possibly help to threshold these color values better:

[Color spaces in OpenCV (C++ / Python)](https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/)

Hopefully, by improving the way I find the color threshold values, I will also be able to improve the counts of the total amount of eggs seen in the image.

---

### Next Steps

Go through the steps seen in the source above to try and find a better way to find color threshold values for egg and sperm cells. 
