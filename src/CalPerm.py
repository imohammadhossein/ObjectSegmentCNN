import os
import cv2
import time
import pickle

Pixel_dict = {}

path = 'permutation/'

correct = cv2.imread(path + 'correct/correct.jpg')
overal = cv2.imread(path + 'all/overal.jpg')
orig = cv2.imread('pot.JPEG')
height, width, channel = orig.shape
print(height * width)
ratio_correct = correct / overal
normalized_correct = cv2.normalize(ratio_correct, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('normalcor.jpg', normalized_correct)
counter = 0
for r in os.listdir(path + 'random'):
	counter += 1
	t1 = time.time()
	random_perm = cv2.imread(path + 'random/' + r)
	random_perm_ratio = random_perm / overal
	normalized_random = cv2.normalize(random_perm_ratio, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

	for j in range(height):
		for k in range(width):
			pix_c = normalized_correct[j][k]
			pix_r = normalized_random[j][k]
			if pix_c.mean() > pix_r.mean():
				key = repr(j) + '_' + repr(k)
				if key in Pixel_dict.keys():
					Pixel_dict[key] += 1
				else:
					new_key = {key:1}
					Pixel_dict.update(new_key)
	print( counter, time.time() - t1)

# for p in Pixel_dict:
# 	if Pixel_dict[p] > 949:
# 		j1 = p.split('_')[0]
# 		k1 = p.split('_')[1]
# 		orig[int(j1)][int(k1)] = [255, 0, 0]

# cv2.imwrite('out.jpg', orig)

a_file = open("pot.pkl", "wb")

pickle.dump(Pixel_dict, a_file)

a_file.close()