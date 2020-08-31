import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

############################################# SET PARAMETERS ###########################################################
# all of the filenames of the images of egg that will be used to composite image of egg
eggs = ['12_10x_e1.png', '12_10x_e2.png','12_10x_e3.png','12_10x_e4.png', '30_10x_e1.png', '30_10x_e2.png',
        '61_10x_e1.png', '61_10x_e2.png', '61_10x_e3.png', '61_10x_e4.png', '66_10x_e1.png', '66_10x_e2.png', '66_10x_e3.png',
        '66_10x_e4.png', '68_10x_e1.png', '68_10x_e2.png', '68_10x_e3.png', '68_10x_e4.png', '103_10x_e1.png', '103_10x_e2.png',
        '127_10x_e1.png', '127_10x_e2.png', '127_10x_e3.png', '127_10x_e4.png', '153_10x_e1.png', '153_10x_e2.png', '153_10x_e3.png',
        '153_10x_e4.png', '163_10x_e1.png', '163_10x_e2.png', '163_10x_e3.png', '163_10x_e4.png']
# all of the filenames of the image of sperm that will be used to create a composite image of sperm
sperm = ['12_10x_s1.png', '12_10x_s2.png', '12_10x_s3.png', '12_10x_s4.png', '61_10x_s1.png', '61_10x_s2.png', '61_10x_s3.png',
         '61_10x_s4.png', '66_10x_s1.png', '66_10x_s2.png', '66_10x_s3.png', '68_10x_s1.png','68_10x_s2.png', '68_10x_s3.png',
         '127_10x_s1.png', '127_10x_s2.png', '127_10x_s3.png', '127_10x_s4.png', '153_10x_s1.png','153_10x_s2.png', '153_10x_s3.png',
         '153_10x_s4.png', '163_10x_s1.png', '163_10x_s2.png', '163_10x_s3.png', '163_10x_s4.png']
# name of the final composite image of egg
image_name_egg = "final_image_egg_new_10x_4.jpg"
# name of the final composite image for sperm
image_name_sperm = "final_image_sperm_new_10x_4.jpg"
images_egg = []
images_sperm = []
what_to_read = image_name_sperm

############################################ CREATE COMPOSITE IMAGES ###################################################
# resize all of the egg images to be the same size to one another
for egg in eggs:
    readimage = cv2.imread(egg)
    images_egg.append(cv2.resize(readimage, (200, 300)))
# resize all of the sperm images to be the same size to one another
for sp in sperm:
    readimage_s = cv2.imread(sp)
    images_sperm.append(cv2.resize(readimage_s, (25, 25)))
# combine all of the egg images together to create composite egg image
final_image_egg = np.vstack(tuple(images_egg))
# combine all of the sperm images together to create a composite sperm image
final_image_sperm = np.vstack(tuple(images_sperm))

#create composite egg image
cv2.imwrite(image_name_egg, final_image_egg)
#create composite sperm image
cv2.imwrite(image_name_sperm, final_image_sperm)

########################################### CREATE DENSITY PLOTS #######################################################
# read composite image that was created
image = cv2.imread(what_to_read)
# change the color space of the composite image to the color space that needs to be analyzed (BGR, HSV, Lab, YCrCb)
image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

B = np.array([])
G = np.array([])
R = np.array([])

# create density plots
b = image[:,:,0]
b = b.reshape(b.shape[0]*b.shape[1])
g = image[:,:,1]
g = g.reshape(g.shape[0]*g.shape[1])
r = image[:,:,2]
r = r.reshape(r.shape[0]*r.shape[1])
B = np.append(B,b)
G = np.append(G,g)
R = np.append(R,r)
nbins = 10
plt.hist2d(G, R, bins = nbins, norm = LogNorm())
# label density plot axes
plt.xlabel('Cr')
plt.ylabel('Cb')
plt.xlim([0,255])
plt.ylim([0,255])
plt.savefig('/Users/hanara/PycharmProjects/o_angasi/10x_colorplots_4/CrCb_10x_s.png')
