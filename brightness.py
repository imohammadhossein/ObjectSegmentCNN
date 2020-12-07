import cv2
import os
import numpy as np

path = 'orig/'
out_path = 'brighted/'
import sys
from PIL import Image, ImageEnhance, ImageStat

def calculate_brightness(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale

aol = 0
for p in os.listdir(path):
    image = Image.open(path + p)
    brightness = calculate_brightness(image)
    aol += brightness
    print(brightness)

aol = (aol/len(os.listdir(path)) )
print('mean: ',aol)

# apply

for t in os.listdir(path):
	#read the image
	im = Image.open(path + t)

	now = calculate_brightness(im)
	diff = aol - now
	#image brightness enhancer
	enhancer = ImageEnhance.Brightness(im)

	if diff< 0:
		print(t, now)
		im_output = enhancer.enhance((1 + diff))
	else:
		im_output = enhancer.enhance((1 + diff))
	im_output.save(out_path + t)