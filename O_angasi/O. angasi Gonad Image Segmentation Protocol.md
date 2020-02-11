## _O. angasi_ Gonad Image Segmentation Protocol

For each image:

1. Open the file [segmentation_color.py](https://github.com/H-Ra/h-ra.github.io/blob/master/O_angasi/segmentation_color.py)
2. Set "bar_length" equal to the scale bar length that is seen in the associated image
3. Set "image_name" equal to the name of the image being analyzed
4. Delete the # sign seen on line 34 for "pl.show()" and run the script to produce a graph equivalent to of all of the colors in the image (see example image below):
![HSV scatter plot](https://github.com/H-Ra/h-ra.github.io/blob/master/images/HSV%20scatter%20plot.png?raw=true)
OR
![RGB scatter plot](https://github.com/H-Ra/h-ra.github.io/blob/master/images/RGB%20scatter%20plot.png?raw=true)
5. Take a screenshot of the produced graph
6. Open ImageJ and open the graph image in ImageJ using file --> open 
7. Place mouse over color area of graph that corresponds to the color of the gonad of interest and read corresponding RGB value that is stated in ImageJ
8. Repeat this process until both the light and the dark color ranges for both male and female gonads are found
9. Write the corresponding light and dark color values for the male gonad into "lightpurple" (line 37) and "darkpurple" (line 38), respectively.
10. Write the corresponding light and dark color values for the female gonad into "lightpink" (line 41) and "darkpink" (line 42), respectively.
11. If you would like to see if the color ranges match to what you previously thought:
	* put the corresponding light color in for "lpsquare" (line 45) and the corresponding dark color for "dpsquare" (line 46) 
	* Then, delete the # sign seen on line 53 for "pl.show()" and run the script to see the colors themselves (see example image below):
![color_range_correct.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/color_range_correct.PNG?raw=true)
12. Delete the # sign seen on lines 128 and 129 for "cv2.imshow("Histoimage", histo_image)" and "cv2.waitKey(0)", respectively, and run the script to see the image segmentation output (see example image below):
![identify_scale_bar.PNG](https://github.com/H-Ra/h-ra.github.io/blob/master/images/identify_scale_bar.PNG?raw=true)
13. To see corresponding measurement outputs for the female and male gonads, Put a # next to all of the previously deleted # in the previous steps and run the script again to produce an output such as the one seen below: 
![](https://github.com/H-Ra/h-ra.github.io/blob/master/images/possible_all_measurements.PNG?raw=true)
