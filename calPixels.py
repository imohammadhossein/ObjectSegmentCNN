import os
import cv2


image_name = 'Binary/ILSVRC2012_test_00096192.jpg'
image = cv2.imread(image_name)

height, width, channel = image.shape
counter = 0
for j in range(height):
	for k in range(width):
		color = image[j][k]
		if color[0] == 0 and color[1] == 0 and color[2] == 0:
			counter += 1

print('counter', counter)
print('area', width * height)
print('ratio', counter/(width * height))