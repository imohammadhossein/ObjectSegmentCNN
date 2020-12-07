from tensorflow.keras.applications.vgg16 import VGG16
from keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image as image_utils
from tensorflow.keras import activations
import numpy as np
from vis.utils import utils
import os
model = VGG16(weights='imagenet')
model_r = model
model_r.layers[-1].activation = activations.relu
model_r = utils.apply_modifications(model_r)
path = 'out/'
image_list = [ 'n02504458', 'n03483316', 'n03124170', 'n01443537', 'n07753275', 'n02165456', 'n04536866', 'n03991062', 'n03481172', 'n02814533', 'n04179913', 'n03584829', 'n03761084', 'n02676566']

### single image
# image_path = 'stimulus83.tif'
# img = image.load_img(image_path, target_size=(224, 224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# preds = model.predict(x)
# P = decode_predictions(preds)
# for (i, (imagenetID, label, prob)) in enumerate(P[0]):
# 	print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))

""" multi image """
for each_class in os.listdir(path):
	for each_size in os.listdir(path + each_class):
		for each_img in os.listdir(path + each_class + '/' + each_size):

			img_path = path + each_class + '/' + each_size + '/' + each_img
			ex = img_path.split('.')[1]
			if ex == 'jpg':
				flag = False
				f = open(img_path.split('.')[0] + ".txt", "w")
				img = image.load_img(img_path, target_size=(224, 224))
				x = image.img_to_array(img)
				x = np.expand_dims(x, axis=0)
				# image = preprocess_input(x)
				preds = model.predict(x)
				preds_r = model_r.predict(x)
				P_r = decode_predictions(preds_r)
				P = decode_predictions(preds)
				print(each_class, each_size)
				for i in range(5):
					(imagenetID, label, prob) = P[0][i]
					(imagenetID, label, prob_r) = P_r[0][i]
					f.write(label + '_' + str(prob) + '_' + str(prob_r)+ '\n')
					if i == 0 and label =='pot':
						flag = True
				f.close()
				# if flag:
				# 	os.remove(img_path.split('.')[0] + ".txt")
				# 	os.remove(img_path)
				
			# print('image name: ' + each_class + '  probabilities in order--->  ')
			# for (i, (imagenetID, label, prob)) in enumerate(P[0]):
			# 	print("{}. {}: {:.2f}%".format(i + 1, label, prob * 100))
			# if imagenetID in image_list:
			# 	directory = 'out/' + imagenetID
			# 	if not os.path.exists(directory):
			# 		os.makedirs(directory)
			# 	os.rename('test/' + each_class, directory + '/' + each_class)