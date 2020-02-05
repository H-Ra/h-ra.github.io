---
layout: post
title: February 4, 2020 - Creating Abstract and Labeling & Thresholding Gonad by Size
---

### Lab Work

__Creating Abstract__

Today, I finished writing a draft of the abstract for the Undergraduate Research Symposium. I used these resources to help me write the abstract:

1. [National review of Ostrea angasi aquaculture: historical culture, current methods and future priorities](https://www.imas.utas.edu.au/__data/assets/pdf_file/0005/936536/160181-UTAS-Scientific-Report_-Angasi-aquaculture.pdf)
2. [O. angasi heat shock trial](https://laurahspencer.github.io/LabNotebook/O-angasi-heat-shock/)
3. [July 18 2018, O. angasi conditioning](https://laurahspencer.github.io/LabNotebook/O-angasi-conditioning/)
4. [Undergraduate Research Symposium Abstract Writing Workshop Presentation](https://drive.google.com/file/d/1K_9sy9Tm8Zcd5Odcd-b6O4aw7ck7kW3x/view)
5. [2019 Symposium Abstracts](https://expo.uw.edu/expo/apply/534/proceedings)

---

__Labeling and Thresholding Gonad by Size__

Last time, I was able to segment the gonad present in the histology images based off of color, but there were some problems with solely using this mode of segmentation. The biggest problem was when segmenting for female gonad, male gonad was also being included in the output. Thus, my next step in effectively segmenting the images was to mark and label each of the contours and then remove certain contours if they were not within a certain size threshold. I used these sources to help me to draw out the segmented contours of the image, label these contours, and also threshold them by size:

1. [In Python, how can I reduce a list of contours to those of a specified size?](https://answers.opencv.org/question/65005/in-python-how-can-i-reduce-a-list-of-contours-to-those-of-a-specified-size/)
2. [Detecting multiple bright spots in an image with Python and OpenCV](https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/)
3. [Drawing Functions](https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html)

By looking at these sources, I was finally able to segment all of the objects in the image at the same time based off of color, and then remove all of the areas that were not female gonad based off of size, and the final product is shown below: 

female gonad:

![female_gonad_segmentation.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/female_gonad_segmentation.PNG?raw=true)

male gonad:

![male_gonad_segmentation.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/male_gonad_segmentation.PNG?raw=true)

together:

![area_threshold_image.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/area_threshold_image.PNG?raw=true)

The updated female gonad area based on the image is:

Female Gonad Total Area: 4875.5

It seems like the output images are in BGR even though I thought I had turned the images into RGB format, so I will have to look into that more. 

Another thing that I will need to do is to convert the area that was found in these images from pixel area to um. These links might be helpful for figuring this out:

1. [Structural Analysis and Shape Descriptors](https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html#contourarea)
2. [contourArea() unit ??](https://answers.opencv.org/question/68982/contourarea-unit/)

---

### Next Steps

1. Review and revise abstract
2. Convert pixel area of gonad to um 


