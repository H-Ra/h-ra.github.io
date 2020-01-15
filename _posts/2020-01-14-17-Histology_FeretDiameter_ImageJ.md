---
layout: post
title: January 14, 2020 - Histology Analysis: Gonad Sex and Stage Determination Practice and Feret's Diameter & Using ImageJ
---

### Lab Work

__Gonad Sex and Stage Determination Practice w/ Laura__

Today, I spoke with Laura about the next steps for the histology image analysis project. During our meeting we: 

* went over how to identify different gonad sex and age 
* I learned more about identifying stages of sperm and eggs:

	* my observations about sperm (color and size) were correct! -- the earlier stages of the male gonad (spermatogonia and spermatocytes) are large and a light purple in color; as spermatogenesis progresses, advanced stages of the sperm cells (spermatids and spermatozoa) are much smaller and much darker in color compared to the earlier stages (they are also clustered together more closely)

	* Additional observations on identifying gonad stage: more early stage eggs and sperm stay closer to the follicle wall, while more developed stages gather towards the center (see image below)
	
	![different_stages_male_gonad_eg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/different_stages_male_gonad_eg.png?raw=true)
	
	* female gonad observations: as eggs become more ripe, they become more grape-like in shape and their germline nucleus cell wall starts to break down (looks more wavy)

* Other things that are in histology images that are not egg or sperm: 
	* 1 - parasites (see image below)
	
	![parasite_eg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/parasite_eg.png?raw=true)

	* 2 - digestive tract
	* 3 - larvae (see image below)

	![larvae_eg](https://github.com/H-Ra/h-ra.github.io/blob/master/images/larvae_eg.png?raw=true)

* there might be a way to possibly quantify the amount of sperm/stage of sperm using ImageJ (separate by size and color)

__Feret's Diameter and Using ImageJ__

Today, I also went through the ImageJ and Fiji software to see what tools we could possibly use in the programs to obtain the goals that we need. Laura mentioned a type of measurement known as "Feret's diameter" that could be really useful when trying to measure eggs. The things that I discovered incude: 

* I found that there is a Feret's diameter feature on imageJ that could be used to measure Feret's diameter of eggs in histology images --> macro plugins can also run if you want it in a more automated fashion

* I used imageJ to apply different kinds of threshold to histology images

Before color change: 
![angasi147_before_color_change](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi147_before_color_change.png?raw=true)

16-bit:
![angasi147_16bit](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi147_16bit.png?raw=true)

All different auto thresholds tested:
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/angasi147_all_auto_threshold.png?raw=true)

* could potentially use thresholding to help determine predominant gonad sex in hermaphroditic individuals
* ultimately, it would be great if we could automate everything because that would eliminate subjectivity and bias as much as possible -- maybe use multiple methods and compare them for accuracy 
* have made a file with important tools, tips, and tricks for how to work with ImageJ here

---

### Next Steps

* look through ImageJ and Fiji more to find a way to threshold images in a way so that eggs can be measured
* maybe look for categorizing different objects by color/hue, shape(circularity), and/or size threshold
* look more into studying gametogenesis and look at more images of invertebrate male gonad in order to understand the phase of development more accurately