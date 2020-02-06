# sources that I used to help me make this script are linked in my posts on my lab notebook --> https://h-ra.github.io/
import cv2
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import numpy as np

#set parameters
bar_length = 50
image_name = '20180924-angasi121-40x-scale.tif'

#Read image and convert color scheme from BGR to RGB/HSV
histo_image = cv2.imread(image_name)
histo_image = cv2.cvtColor(histo_image, cv2.COLOR_BGR2RGB)
hsv_histo_image = cv2.cvtColor(histo_image, cv2.COLOR_RGB2HSV)

# setting up scatter plot of all colors present in image
h, s, v = cv2.split(hsv_histo_image)
fig = pl.figure()
axis = fig.add_subplot(1, 1, 1, projection='3d')

# "normalizing" colors
pixel_colors = histo_image.reshape((np.shape(histo_image)[0]*np.shape(histo_image)[1], 3))
norm = colors.Normalize(vmin=-1., vmax=1.)
norm.autoscale(pixel_colors)
pixel_colors = norm(pixel_colors).tolist()

# plotting points onto the graph
axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
axis.set_xlabel("Hue")
axis.set_ylabel("Saturation")
axis.set_zlabel("Value")
#pl.show()

# testing color range values for PURPLE
light_purple = (124, 35, 169)
dark_purple = (71, 0, 87)

# testing color range values for PINK
light_pink = (251, 51, 168)
dark_pink = (150, 0, 96)

# putting colors onto squares
lp_square = np.full((10, 10, 3), light_pink, dtype=np.uint8) / 255
dp_square = np.full((10, 10, 3), dark_pink, dtype=np.uint8) / 255

# visualizing colors on plot
pl.subplot(1, 2, 1)
pl.imshow(lp_square)
pl.subplot(1, 2, 2)
pl.imshow(dp_square)
#pl.show()

# threshold image using color range values for PURPLE
mask_purple = cv2.inRange(histo_image, dark_purple, light_purple)
result_purple = cv2.bitwise_and(histo_image, histo_image, mask=mask_purple)

# threshold image using color range values for PINK
mask_pink = cv2.inRange(histo_image, dark_pink, light_pink)
result_pink = cv2.bitwise_and(histo_image, histo_image, mask=mask_pink)

#view threshold result
pl.subplot(1, 2, 1)
pl.imshow(mask_pink, cmap='gray')
pl.subplot(1, 2, 2)
pl.imshow(result_pink)
#pl.show()

# read scale bar
bar_color = (0, 0, 0)
mask_bar = cv2.inRange(histo_image, bar_color, bar_color)
bar_contours=cv2.findContours(mask_bar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
bar_contours=bar_contours[0] if len(bar_contours) == 2 else bar_contours[1]

#identify and measure scale bar in pixels
bar_size = []
for c in bar_contours:
   bar_size.append(cv2.contourArea(c))

conversion_length = 0
for d in bar_contours:
    if cv2.contourArea(d) == max(bar_size):
        (x, y, w, h) = cv2.boundingRect(d)
        cv2.rectangle(histo_image, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
        print("Length of scale bar in um: " + str(bar_length) + " um")
        print("Height of bar in pixels: " + str(h))
        print("Width of bar in pixels: " + str(w))
        print("Scale of bar (conversion from pixels to um): " + str(bar_length/w))
        conversion_length += (bar_length/w)

# find and draw all PURPLE contours
purple_contours=cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
purple_contours=purple_contours[0] if len(purple_contours) == 2 else purple_contours[1]
#draw_purple_contours=cv2.drawContours(histo_image, purple_contours, -1, (0, 0, 255), thickness=2)

# find area of threshold for PURPLE and draw respective contours
total_purple_area=0
for c in purple_contours:
    total_purple_area += cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)
    text = str(cv2.contourArea(c))
    #cv2.drawContours(histo_image, c, -1, (0, 0, 255), thickness=2)
    #cv2.putText(histo_image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 0, 255), thickness=1)

# find and draw all PINK contours
pink_contours=cv2.findContours(mask_pink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pink_contours=pink_contours[0] if len(pink_contours) == 2 else pink_contours[1]
#draw_pink_contours=cv2.drawContours(histo_image, pink_contours, -1, (0, 255, 0), thickness=2)

# find area of threshold for PINK (individual and total) and draw respective contours
pixel_area_threshold = 1000
total_pink_area = 0
pixel_pink_area = []
pink_area = []
for c in pink_contours:
    if cv2.contourArea(c) > pixel_area_threshold:
        total_pink_area += cv2.contourArea(c)
        pixel_pink_area.append(cv2.contourArea(c))
        pink_area.append(cv2.contourArea(c) * (conversion_length**2))
        (x, y, w, h) = cv2.boundingRect(c)
        #text = str(cv2.contourArea(c))
        um_text = str(cv2.contourArea(c) * (conversion_length**2))
        cv2.drawContours(histo_image, c, -1, (0, 255, 0), thickness=2)
        cv2.putText(histo_image, um_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.3, color=(0, 255, 0), thickness=1)
pixel_pink_area.sort(reverse=True)

#cv2.imshow("Histo_image", histo_image)
#cv2.waitKey(0)

print("Female Gonad Total Area in pixels: ", str(total_pink_area))
print("Female Gonad Each Egg Area in pixels: ", str(pixel_pink_area))
print("Male Gonad Total Area in pixels: ", str(total_purple_area))

print("Female Gonad Total Area in um: ", str(total_pink_area * (conversion_length**2)))
print("Female Gonad Each Egg Area in um: ", str(pink_area))
print("Male Gonad Total Area in um: ", str(total_purple_area * (conversion_length**2)))