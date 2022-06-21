import os
import cv2
source_path = 'accepted/'
dest = 'resized_accepted/'
widths = 0
heights = 0
lmnop = os.listdir(source_path)
for m in lmnop:
	image = cv2.imread(source_path + m)
	widths += image.shape[1]
	heights += image.shape[0]
dims = (int(widths/len(lmnop)),int(heights/len(lmnop)))
for l in lmnop:
	image = cv2.imread(source_path + l)
	resized = cv2.resize(image, dims, interpolation = cv2.INTER_AREA)
	cv2.imwrite(dest + l , resized)
print(dims)