import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageStat
source_path = 'orig/'
dest = 'contrasted/'

# for awaying from overflow floats infs
def round_int(x):
    if x == float("inf") or x == float("-inf"):
        return float('nan') # or x or return whatever makes sense
    return int(round(x))


lmnop = os.listdir(source_path)

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)

def compute_cv2(image):
	Y = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)[:,:,0]
	print(Y)

	# compute min and max of Y
	min = np.min(Y)
	max = np.max(Y)

	# compute contrast
	contrast = (max-min)/(max+min)
	return contrast

def compute_cv2_2(image):
	img_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	contrast = img_grey.std()
	return contrast

def compute_PIL(path):
	im = Image.open(path)
	stats = ImageStat.Stat(im)  
	mean = 0 
	for band,name in enumerate(im.getbands()):                                                            
		contrast = stats.stddev[band]
		mean += contrast

	return int(mean/3)

cont_cv2 = 0
cont_cv2_2 = 0
cont_PIL = 0
print(lmnop)
for m in lmnop:
	print(m)
	image = cv2.imread(source_path + m)
	print(m)
	# cont_cv2 += compute_cv2(image)  # if gave "overflow" error, comment it.
	cont_cv2_2 += compute_cv2_2(image)
	cont_PIL += compute_PIL(source_path + m)

# print('1:  ',int(cont_cv2/len(lmnop))) 
print('2:  ',int(cont_cv2_2/len(lmnop)))
print('3:  ', int(cont_PIL/len(lmnop)))
final_contrast = int((int(cont_cv2/len(lmnop)) + int(cont_cv2_2/len(lmnop)) + int(cont_PIL/len(lmnop)))/3)


for l in lmnop:
	image = Image.open(source_path + l)
	contrasted = change_contrast(image, final_contrast)
	contrasted.save(dest + l)
