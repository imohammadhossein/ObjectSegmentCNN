import cv2
import os
import numpy as np
from math import sqrt
from PIL import Image, ImageDraw, ImageFilter
import random

def compute_distance(x1, x2, y1, y2):
	return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )


def check_coords(new_point):
	if radius + offset < new_point[0] < width - radius - offset:
		if radius + offset < new_point[1] < height - radius - offset:
			return True
		else:
			return False
	else:
		return False

def check_validity(new_center, prev_centers, distance_thresh):
	check_coordinates = check_coords(new_center)
	result = True
	if check_coordinates:
		if len(prev_centers) == 0:
			result = True
		else:
			for prev_point in prev_centers:
				distance = compute_distance(new_center[0], prev_point[0], new_center[1], prev_point[1])
				if distance < (distance_thresh * (radius + offset)):
					result = False
					break

	else:
		result = False
	return result


def make_PIL(cv_image):
	img_bgr = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
	im_pil = Image.fromarray(img_bgr)
	return im_pil

def overal_applier(overal_centers, img):
	circle = np.zeros((img.shape[0],img.shape[1],3), np.uint8)
	for m in overal_centers:
		for f in m:
			cv2.circle(circle, (f[0], f[1]), radius, (255,255,255), -1)
	overal_image = cv2.bitwise_and(img, circle)
	return overal_image

def center_maker(number, distance_thresh):
	centers = []
	
	# for 4 parts
	x14 = int(width/2)
	split_areas = 4
	y14 = int(height/2)


	if number<split_areas:
		g_list = random.sample(range(0, split_areas), number)
	else:
		g_list = []
		base_list = list(range(split_areas))
		duplicator = int(number/split_areas)
		for m in range(duplicator):
			g_list += base_list
		secondary = random.sample(range(0, split_areas), int(number%split_areas))
		g_list += secondary

	i = 0
	while i < (number):
		num = g_list[i]
		validity = False
		patience = 0
		while not validity:
			patience +=1
			if patience > 15:
				print('patience maxed out!')
				i = 0
				centers = []

			if num==0:
				x = random.randint(0, x14)
				y = random.randint(0, y14)

			elif num==1:
				x = random.randint(x14, width)
				y = random.randint(0, y14)

			elif num==2:
				x = random.randint(0, x14)
				y = random.randint(y14, height)

			elif num==3:
				x = random.randint(x14, width)
				y = random.randint(y14, height)
			
			validity = check_validity((x,y), centers, distance_thresh)
		# print('Done: ',number)
		centers.append((x,y))
		i += 1

		

	return centers

def crop_circle(r, img, number, distance_thresh):
	
	pil_img_back = Image.new("L", (img.shape[1], img.shape[0]), 0)
	draw_pil = ImageDraw.Draw(pil_img_back)
	pil_img_back_2 = Image.new("RGB", (img.shape[1], img.shape[0]), 0)

	centers = center_maker(number, distance_thresh)
	for s in centers:
		#xmin, ymin, xmax, ymax
		draw_pil.ellipse((s[0] - r, s[1] - r, s[0] + r, s[1] + r), fill=255)

	test = pil_img_back
	pil_img_back = pil_img_back.filter(ImageFilter.GaussianBlur(5))
	final_img = Image.composite(make_PIL(img), pil_img_back_2, pil_img_back)

	return final_img, centers, pil_img_back, test

groups = [5, 7, 9, 11, 13]

offset = 0   #distance from edges of the image
numberOfCircles = 13
distance_thresh = 0  #minimum circles centers distance from each other


#single image
# base_image = cv2.imread('orig/ILSVRC2012_test_00096192.JPEG')
# height, width, channel = base_image.shape
# bubble_image, centers = crop_circle(radius, base_image, numberOfCircles, distance_thresh)
# bubble_image.save('result.jpg')

## directory
in_path = 'orig/'
out_path = 'out/'
# for image in os.listdir(in_path):
# print(image)
image = 'ILSVRC2012_test_00079597.JPEG'
name = image.split('.')[0]
if not os.path.exists(out_path + name):
    os.makedirs(out_path + name)
base_image = cv2.imread(in_path + image)
height, width, channel = base_image.shape
radius = int(width * height / 12000)
# for m in range(0,101,2):
m = 13
if not os.path.exists(out_path + name + '/' + repr(m)):
    os.makedirs(out_path + name + '/' + repr(m))
overal_centers = []
for i in range(100):
    bubble_image, centers, mask, test = crop_circle(35, base_image, 13, distance_thresh)
    overal_centers.append(centers)
    bubble_image.save(out_path+name+'/'+repr(13)+'/'+repr(i)+'.jpg')
    # mask.save(out_path+name+'/'+repr(13)+'/'+repr(i)+'_bubble.jpg')
    test.save(out_path+name+'/'+repr(13)+'/'+repr(i)+'_circle.jpg')
# overal_image = overal_applier(overal_centers, base_image)
# cv2.imwrite(out_path+name+'/'+repr(m)+'/overal.jpg', overal_image)




