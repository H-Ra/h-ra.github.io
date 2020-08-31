import os
import cv2
import csv
import numpy as np

# list the path to the directory that contains histology images
os.chdir('/Users/hanara/PycharmProjects/o_angasi/histo images')

# create a csv file to input necessary data
with open('o_angasi.csv', 'w', newline='') as newfile:
   writer = csv.writer(newfile)

   writer.writerow(['filename', 'scalebar', 'imagesize', 'bgr_pixel_m', 'bgr_pixel_f', 'hsv_pixel_m', 'hsv_pixel_f', 'lab_pixel_m', 'lab_pixel_f', 'ycrcb_pixel_m',  'ycrcb_pixel_f'])

   for filename in os.listdir('/Users/hanara/PycharmProjects/o_angasi/histo images'):
      if filename.endswith('.tif') and filename[19] == "1":
         print(filename)
         ################################################# SET PARAMETERS ####################################################
         image_name = filename

         # Read image
         histo_image = cv2.imread(image_name)
         dimensions = histo_image.shape
         # Change color scheme of image to RGB, HSV, YCrCb, Lab
         histo_image = cv2.cvtColor(histo_image, cv2.COLOR_BGR2RGB)
         BGR = histo_image
         HSV = cv2.cvtColor(histo_image, cv2.COLOR_RGB2HSV)
         YCrCb = cv2.cvtColor(histo_image, cv2.COLOR_RGB2YCrCb)
         Lab = cv2.cvtColor(histo_image, cv2.COLOR_RGB2LAB)
         green = np.uint8([[[0,255,0]]])
         blue = np.uint8([[[255,0,0]]])

         ################################################# EGG SEGMENTATION ####################################################
         pixel_area_threshold = 10

         ## BGR color space threshold egg ##
         minBGR = np.array([140, 0, 80])
         maxBGR = np.array([250, 75, 160])
         maskBGR = cv2.inRange(BGR, minBGR, maxBGR)
         resultBGRegg = cv2.bitwise_and(BGR, BGR, mask=maskBGR)

         # find and draw all PINK BGR contours
         pink_BGR = cv2.findContours(maskBGR, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         pink_BGR = pink_BGR[0] if len(pink_BGR) == 2 else pink_BGR[1]

         total_pink_BGR = 0
         for c in pink_BGR:
            if cv2.contourArea(c) > pixel_area_threshold:
               total_pink_BGR += cv2.contourArea(c)
               cv2.drawContours(BGR, c, -1, (0, 255, 0), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(BGR, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 255, 0), thickness=1)

         ## HSV Color Space Threshold egg ##
         minHSV = np.array([155, 165, 140])
         maxHSV = np.array([175, 250, 250])
         maskHSV = cv2.inRange(HSV, minHSV, maxHSV)
         resultHSVegg = cv2.bitwise_and(HSV, HSV, mask=maskHSV)

         # find and draw all PINK HSV contours
         pink_HSV = cv2.findContours(maskHSV, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         pink_HSV = pink_HSV[0] if len(pink_HSV) == 2 else pink_HSV[1]

         total_pink_HSV = 0
         for c in pink_HSV:
            if cv2.contourArea(c) > pixel_area_threshold:
               total_pink_HSV += cv2.contourArea(c)
               green_HSV = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
               cv2.drawContours(HSV, c, -1, (int(green_HSV[0][0][0]), int(green_HSV[0][0][1]), int(green_HSV[0][0][2])), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(HSV, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 255, 0), thickness=1)

         ## YCrCb Color Space Threshold egg ##
         minYCrCb = np.array([55, 180, 120])
         maxYCrCb = np.array([140, 245, 175])
         maskYCrCb = cv2.inRange(YCrCb, minYCrCb, maxYCrCb)
         resultYCrCbegg = cv2.bitwise_and(YCrCb, YCrCb, mask=maskYCrCb)

         # find and draw all PINK YCrCb contours
         pink_YCrCb = cv2.findContours(maskYCrCb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         pink_YCrCb = pink_YCrCb[0] if len(pink_YCrCb) == 2 else pink_YCrCb[1]

         total_pink_YCrCb = 0
         for c in pink_YCrCb:
            if cv2.contourArea(c) > pixel_area_threshold:
               total_pink_YCrCb += cv2.contourArea(c)
               green_YCrCb = cv2.cvtColor(green, cv2.COLOR_BGR2YCrCb)
               cv2.drawContours(YCrCb, c, -1, (int(green_YCrCb[0][0][0]), int(green_YCrCb[0][0][1]), int(green_YCrCb[0][0][2])), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(YCrCb, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 255, 0), thickness=1)

         ## Lab Color Space Threshold egg ##
         minLab = np.array([80, 175, 105])
         maxLab = np.array([160, 220, 155])
         maskLab = cv2.inRange(Lab, minLab, maxLab)
         resultLabegg = cv2.bitwise_and(Lab, Lab, mask=maskLab)

         # find and draw all PINK Lab contours
         pink_Lab = cv2.findContours(maskLab, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         pink_Lab = pink_Lab[0] if len(pink_Lab) == 2 else pink_Lab[1]

         total_pink_Lab = 0
         for c in pink_Lab:
            if cv2.contourArea(c) > pixel_area_threshold:
               total_pink_Lab += cv2.contourArea(c)
               green_LAB = cv2.cvtColor(green, cv2.COLOR_BGR2LAB)
               cv2.drawContours(Lab, c, -1, (int(green_LAB[0][0][0]), int(green_LAB[0][0][1]), int(green_LAB[0][0][2])), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(Lab, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 255, 0), thickness=1)

         ############################################ SPERM SEGMENTATION ##################################################
         sperm_pixel_threshold = 10

         ## BGR color space threshold sperm ##
         minBGRs = np.array([50, 0, 65])
         maxBGRs = np.array([155, 50, 165])
         maskBGRs = cv2.inRange(BGR, minBGRs, maxBGRs)
         resultBGRs = cv2.bitwise_and(BGR, BGR, mask=maskBGRs)

         # find and draw all PURPLE BGR contours
         purple_BGR = cv2.findContours(maskBGRs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         purple_BGR = purple_BGR[0] if len(purple_BGR) == 2 else purple_BGR[1]

         total_purple_BGR = 0
         for c in purple_BGR:
            if cv2.contourArea(c) > sperm_pixel_threshold:
               total_purple_BGR += cv2.contourArea(c)
               cv2.drawContours(BGR, c, -1, (0, 0, 255), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(BGR, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 0, 255), thickness=1)

         ## HSV Color Space Threshold sperm ##
         minHSVs = np.array([140, 130, 60])
         maxHSVs = np.array([165, 250, 170])
         maskHSVs = cv2.inRange(HSV, minHSVs, maxHSVs)
         resultHSVs = cv2.bitwise_and(HSV, HSV, mask=maskHSVs)

         # find and draw all PURPLE HSV contours
         purple_HSV = cv2.findContours(maskHSVs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         purple_HSV = purple_HSV[0] if len(purple_HSV) == 2 else purple_HSV[1]

         total_purple_HSV = 0
         for c in purple_HSV:
            if cv2.contourArea(c) > sperm_pixel_threshold:
               total_purple_HSV += cv2.contourArea(c)
               blue_HSV = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
               cv2.drawContours(HSV, c, -1, (int(blue_HSV[0][0][0]), int(blue_HSV[0][0][1]), int(blue_HSV[0][0][2])), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(HSV, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 0, 255), thickness=1)

         ## YCrCb Color Space Threshold sperm ##
         minYCrCbs = np.array([25, 145, 130])
         maxYCrCbs = np.array([75, 200, 180])
         maskYCrCbs = cv2.inRange(YCrCb, minYCrCbs, maxYCrCbs)
         resultYCrCbs = cv2.bitwise_and(YCrCb, YCrCb, mask=maskYCrCbs)

         # find and draw all PURPLE YCrCb contours
         purple_YCrCb = cv2.findContours(maskYCrCbs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         purple_YCrCb = purple_YCrCb[0] if len(purple_YCrCb) == 2 else purple_YCrCb[1]

         total_purple_YCrCb = 0
         for c in purple_YCrCb:
            if cv2.contourArea(c) > sperm_pixel_threshold:
               total_purple_YCrCb += cv2.contourArea(c)
               blue_YCrCb = cv2.cvtColor(blue, cv2.COLOR_BGR2YCrCb)
               cv2.drawContours(YCrCb, c, -1, (int(blue_YCrCb[0][0][0]), int(blue_YCrCb[0][0][1]), int(blue_YCrCb[0][0][2])), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(YCrCb, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 0, 255), thickness=1)

         ## Lab Color Space Threshold sperm ##
         minLabs = np.array([35, 155, 65])
         maxLabs = np.array([100, 195, 130])
         maskLabs = cv2.inRange(Lab, minLabs, maxLabs)
         resultLabs = cv2.bitwise_and(Lab, Lab, mask=maskLabs)

         # find and draw all PURPLE Lab contours
         purple_Lab = cv2.findContours(maskLabs, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         purple_Lab = purple_Lab[0] if len(purple_Lab) == 2 else purple_Lab[1]

         total_purple_Lab = 0
         for c in purple_Lab:
            if cv2.contourArea(c) > sperm_pixel_threshold:
               total_purple_Lab += cv2.contourArea(c)
               blue_Lab = cv2.cvtColor(blue, cv2.COLOR_BGR2LAB)
               cv2.drawContours(Lab, c, -1, (int(blue_Lab[0][0][0]), int(blue_Lab[0][0][1]), int(blue_Lab[0][0][2])), thickness=4)
               (x, y, w, h) = cv2.boundingRect(c)
               text = str(cv2.contourArea(c))
               cv2.putText(Lab, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 0, 225), thickness=1)

         # read scale bar
         bar_color = (0, 0, 0)
         mask_bar = cv2.inRange(histo_image, bar_color, bar_color)
         bar_contours = cv2.findContours(mask_bar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         bar_contours = bar_contours[0] if len(bar_contours) == 2 else bar_contours[1]

         # identify and measure scale bar in pixels
         bar_size = []
         for c in bar_contours:
               bar_size.append(cv2.contourArea(c))
         if len(bar_size) > 0:
            writer.writerow([filename, "yes", str(dimensions[0]) + " x " + str(dimensions[1]), total_purple_BGR, total_pink_BGR, total_purple_HSV, total_pink_HSV, total_purple_Lab, total_pink_Lab, total_purple_YCrCb, total_pink_YCrCb])
         if len(bar_size) == 0:
            writer.writerow([filename, "no", str(dimensions[0]) + " x " + str(dimensions[1]), total_purple_BGR, total_pink_BGR, total_purple_HSV, total_pink_HSV, total_purple_Lab, total_pink_Lab, total_purple_YCrCb, total_pink_YCrCb])

         #create images with marked egg and sperm regions based on color spaces BGR, HSV, Lab, YCrCb
         cv2.imwrite(str(filename) + "_BGR.png", cv2.cvtColor(BGR, cv2.COLOR_BGR2RGB))
         cv2.imwrite(str(filename) + "_HSV.png", cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR))
         cv2.imwrite(str(filename) + "_Lab.png", cv2.cvtColor(Lab, cv2.COLOR_LAB2BGR))
         cv2.imwrite(str(filename) + "_YCrCb.png", cv2.cvtColor(YCrCb, cv2.COLOR_YCrCb2BGR))
