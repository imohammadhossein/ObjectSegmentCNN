import os
import cv2
import time
import pickle
import numpy as np
from PIL import Image
import imutils

numOfSample = 20

def make_PIL(cv_image):
	img_bgr = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
	im_pil = Image.fromarray(img_bgr)
	return im_pil

load_data = open("pot.pkl", "rb")
points = pickle.load(load_data)

orig = cv2.imread('pot.JPEG')
copy_image = orig.copy()
height, width, channel = orig.shape

pil_img_back_2 = Image.new("RGB", (orig.shape[1], orig.shape[0]), 0)
pil_img_back = Image.open('normalcor.jpg').convert("L")

keys = points.keys()
for j in range(height):
	for k in range(width):
		label = repr(j) + '_' + repr(k)
		if label in keys and points[label] > int(0.95*numOfSample):
			copy_image[j][k] = [255, 255, 255]
		else:
			copy_image[j][k] = [0, 0, 0]

kernel = np.ones((5,5), np.uint8)
# dilation = cv2.dilate(copy_image, kernel, iterations = 1)

thresh = cv2.threshold(copy_image, 60, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

final_img = Image.composite(make_PIL(orig), pil_img_back_2, pil_img_back)
final_img_cv = cv2.cvtColor(np.array(final_img), cv2.COLOR_RGB2BGR)

for c in cnts:
	c = c.astype("int")
	cv2.drawContours(final_img_cv, [c], -1, (0, 255, 0), 2)
cv2.imwrite('out.jpg', final_img_cv)