import numpy as np
import os
import matplotlib.pyplot as plt 
from PIL import Image

def get_num_pixels(filepath):
    width, height = Image.open(filepath).size
    return width*height

labels_dict = {'iron':'ILSVRC2012_test_00006710', 'hammer':'ILSVRC2012_test_00012696', 'violin':'ILSVRC2012_test_00021672', 'hand_blower':'ILSVRC2012_test_00054121', 'pineapple':'ILSVRC2012_test_00038504', 'sewing_machine':'ILSVRC2012_test_00056725', 'goldfish':'ILSVRC2012_test_00018468', 'ladybug':'ILSVRC2012_test_00059952', 'beach_wagon':'ILSVRC2012_test_00040760', 'pot':'ILSVRC2012_test_00079597', 'African_elephant':'ILSVRC2012_test_00096192', 'cowboy_hat':'ILSVRC2012_test_00095564'}
area_dict = {'iron':180222, 'hammer':46834, 'violin':34978, 'hand_blower':44126, 'pineapple':43920, 'sewing_machine':116151, 'goldfish':22211, 'ladybug':15907, 'beach_wagon':72525, 'pot':67239, 'African_elephant':95492, 'cowboy_hat':42280}

# function to return key for any value 
def get_key(val): 
    for key, value in labels_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"


path = 'out_ds/'
out_path = 'plots/'
all_top_ones = []
x_axis_normalized_pic_all_top_ones = []
x_axis_normalized_obj_all_top_ones = []
all_top_ones_labels = []
for each_class in os.listdir(path):
	print(each_class)
	all_top_ones_labels.append(get_key(each_class))
	flag = False
	x_axis = []
	x_axis_normalized_obj = []
	x_axis_normalized_pic = []
	y1_axis = []
	y2_axis = []
	y3_axis = []
	y4_axis = []
	y5_axis = []
	y1_axis_conf_relu = []
	y1_axis_conf_softmax = []
	y2_axis_conf_relu = []
	y2_axis_conf_softmax = []
	y3_axis_conf_relu = []
	y3_axis_conf_softmax = []
	y4_axis_conf_relu = []
	y4_axis_conf_softmax = []
	y5_axis_conf_relu = []
	y5_axis_conf_softmax = []
	all_labels = []
	all_confs_softmax = []
	all_confs_relu = []
	if not os.path.exists(out_path + each_class):
	    os.makedirs(out_path + each_class)
	size_list = os.listdir(path + each_class)
	size_list.sort(key=int)
	for each_size in size_list:
		conf1_softmax = 0
		conf2_softmax = 0
		conf3_softmax = 0
		conf4_softmax = 0
		conf5_softmax = 0
		conf1_relu = 0
		conf2_relu = 0
		conf3_relu = 0
		conf4_relu = 0
		conf5_relu = 0
		counter1 = 0
		counter2 = 0
		counter3 = 0
		counter4 = 0
		counter5 = 0
		for each_file in os.listdir(path + each_class + '/' +each_size):
			if each_file.split('.')[-1] == 'txt':
				f = open(path + each_class + '/' + each_size + '/' +each_file, "r")
				lines = f.readlines()
				line1 = lines[0]
				line2 = lines[1]
				line3 = lines[2]
				line4 = lines[3]
				line5 = lines[4]
				if line1.split('_')[0] == get_key(each_class) or line1.split('_')[0] +'_'+ line1.split('_')[1] == get_key(each_class) :
					conf1_relu += float(line1.split('_')[-1])
					conf1_softmax += float(line1.split('_')[-2])
					counter1 += 1
					counter2 += 1
					counter3 += 1
					counter4 += 1
					counter5 += 1
				elif line2.split('_')[0] == get_key(each_class) or line2.split('_')[0] +'_'+ line2.split('_')[1] == get_key(each_class):
					conf2_relu += float(line1.split('_')[-1])
					conf2_softmax += float(line1.split('_')[-2])
					counter2 += 1
					counter3 += 1
					counter4 += 1
					counter5 += 1
				elif line3.split('_')[0] == get_key(each_class) or line3.split('_')[0] +'_'+ line3.split('_')[1] == get_key(each_class):
					conf3_relu += float(line1.split('_')[-1])
					conf3_softmax += float(line1.split('_')[-2])
					counter3 += 1
					counter4 += 1
					counter5 += 1
				elif line4.split('_')[0] == get_key(each_class) or line4.split('_')[0] +'_'+ line4.split('_')[1] == get_key(each_class):
					conf4_relu += float(line1.split('_')[-1])
					conf4_softmax += float(line1.split('_')[-2])
					counter4 += 1
					counter5 += 1
				elif line5.split('_')[0] == get_key(each_class) or line5.split('_')[0] +'_'+ line5.split('_')[1] == get_key(each_class):
					conf5_relu += float(line1.split('_')[-1])
					conf5_softmax += float(line1.split('_')[-2])
					counter5 += 1
		numOfObjPixels = area_dict[get_key(each_class)]
		numOfPicPixels = get_num_pixels('orig/' + each_class + '.JPEG')
		x_axis.append(each_size)
		x_axis_normalized_obj.append(int(each_size)/numOfObjPixels)
		x_axis_normalized_pic.append(int(each_size)/numOfPicPixels)
		y1_axis.append(counter1)
		y2_axis.append(counter2)
		y3_axis.append(counter3)
		y4_axis.append(counter4)
		y5_axis.append(counter5)
		y1_axis_conf_softmax.append(conf1_softmax / 100)
		y1_axis_conf_relu.append(conf1_relu / 100)
		y2_axis_conf_softmax.append(conf2_softmax / 100)
		y2_axis_conf_relu.append(conf2_relu / 100)
		y3_axis_conf_softmax.append(conf3_softmax / 100)
		y3_axis_conf_relu.append(conf3_relu / 100)
		y4_axis_conf_softmax.append(conf4_softmax / 100)
		y4_axis_conf_relu.append(conf4_relu / 100)
		y5_axis_conf_softmax.append(conf5_softmax / 100)
		y5_axis_conf_relu.append(conf5_relu / 100)
	all_labels.append(y1_axis)
	all_top_ones.append(y1_axis)
	x_axis_normalized_obj_all_top_ones.append(x_axis_normalized_obj)
	x_axis_normalized_pic_all_top_ones.append(x_axis_normalized_pic)
	all_labels.append(y2_axis)
	all_labels.append(y3_axis)
	all_labels.append(y4_axis)
	all_labels.append(y5_axis)
	all_confs_softmax.append(y1_axis_conf_softmax)
	all_confs_softmax.append(y2_axis_conf_softmax)
	all_confs_softmax.append(y3_axis_conf_softmax)
	all_confs_softmax.append(y4_axis_conf_softmax)
	all_confs_softmax.append(y5_axis_conf_softmax)
	all_confs_relu.append(y1_axis_conf_relu)
	all_confs_relu.append(y2_axis_conf_relu)
	all_confs_relu.append(y3_axis_conf_relu)
	all_confs_relu.append(y4_axis_conf_relu)
	all_confs_relu.append(y5_axis_conf_relu)

	# plotting the points  NOT NORMALIZED
	plt.figure(figsize=(25,10))
	for acc in range(5):
		plt.plot(x_axis, all_labels[acc], linestyle='solid', linewidth = 3, 
		         marker='o', markerfacecolor='blue', markersize=5) 
	# naming the x axis 
	plt.xlabel('number of bubbles.') 
	# naming the y axis 
	plt.ylabel('number of correct samples from 100 samples') 
	# giving a title to my graph 
	plt.title(' accuracy per bubbles range for ' + get_key(each_class) +' class.') 
	plt.legend(['top-1', 'top-2', 'top-3', 'top-4', 'top-5'], loc='upper left')
	plt.savefig(out_path + each_class + '/' + get_key(each_class) + '_Accuracy_per_bubblesAmount_non_normalized.jpg')
	plt.close()


	# plotting the points NORMALIZED by obj pixels
	plt.figure(figsize=(25,10))
	for acc in range(5):
		plt.plot(x_axis_normalized_obj, all_labels[acc], linestyle='dashed', linewidth = 3, 
		         marker='o', markerfacecolor='blue', markersize=7) 
	# naming the x axis 
	plt.xlabel('ratio of bubbles in number per object pixels.') 
	# naming the y axis 
	plt.ylabel('number of correct samples from 100 samples') 
	# giving a title to my graph 
	plt.title(' accuracy per bubbles range for ' + get_key(each_class) +' class.') 
	plt.legend(['top-1', 'top-2', 'top-3', 'top-4', 'top-5'], loc='upper left')
	plt.savefig(out_path + each_class + '/' + get_key(each_class) + '_Accuracy_per_bubblesAmount_normalized_by_object_pixels.jpg')
	plt.close()

	# plotting the points NORMALIZED by picture pixels
	plt.figure(figsize=(25,10))
	for acc in range(5):
		plt.plot(x_axis_normalized_pic, all_labels[acc], linestyle='dashed', linewidth = 3, 
		         marker='o', markerfacecolor='blue', markersize=7) 
	# naming the x axis 
	plt.xlabel('ratio of bubbles in number per picture pixels.') 
	# naming the y axis 
	plt.ylabel('number of correct samples from 100 samples') 
	# giving a title to my graph 
	plt.title(' accuracy per bubbles range for ' + get_key(each_class) +' class.') 
	plt.legend(['top-1', 'top-2', 'top-3', 'top-4', 'top-5'], loc='upper left')
	plt.savefig(out_path + each_class + '/' + get_key(each_class) + '_Accuracy_per_bubblesAmount_normalized_by_picture_pixels.jpg')
	plt.close()


	# plotting the confs softmax and relu
	colors = ['blue', 'green', 'red', 'black', 'orange']

	plt.figure(figsize=(25,10))
	for acc in range(5):
		plt.plot(x_axis, all_confs_softmax[acc], color=colors[acc], linestyle='dashed', linewidth = 3, 
		         marker='o', markerfacecolor='blue', markersize=7) 
	# naming the x axis 
	plt.xlabel('number of bubbles in pixels.') 
	# naming the y axis 
	plt.ylabel('mean of Softmax confidences from 100 samples') 
	# giving a title to my graph 
	plt.title(' mean of confidences per number of bubbles for ' + get_key(each_class) +' class; Softmax.') 
	plt.legend(['top-1', 'top-2', 'top-3', 'top-4', 'top-5'], loc='upper left')
	plt.savefig(out_path + each_class + '/' + get_key(each_class) + '_mean_confidence_Softmax.jpg')
	plt.close()

	plt.figure(figsize=(25,10))
	for acc in range(5):
		plt.plot(x_axis, all_confs_relu[acc], color=colors[acc], linestyle='dashed', linewidth = 3, 
			         marker='o', markerfacecolor='blue', markersize=7) 
	# naming the x axis 
	plt.xlabel('number of bubbles in pixels.') 
	# naming the y axis 
	plt.ylabel('mean of Relu confidences from 100 samples') 
	# giving a title to my graph 
	plt.title(' mean of confidences per number of bubbles for ' + get_key(each_class) +' class; Relu.') 
	plt.legend(['top-1', 'top-2', 'top-3', 'top-4', 'top-5'], loc='upper left')
	plt.savefig(out_path + each_class + '/' + get_key(each_class) + '_mean_confidence_Relu.jpg')
	plt.close()

# plotting all top-1 non normalized
plt.figure(figsize=(25,10))
for lmnop in range(len(labels_dict)):
	plt.plot(x_axis, all_top_ones[lmnop], linestyle='solid', linewidth = 3, 
		         marker='', markerfacecolor='blue', markersize=7) 
# naming the x axis 
plt.xlabel('ratio of number of bubbles in pixel.') 
# naming the y axis 
plt.ylabel('number of correct samples from 100 samples for just top-1') 
# giving a title to my graph 
plt.title(' comparing accuracy of top-1s of each classes non normalized.') 
plt.legend(all_top_ones_labels)
# plt.legend([all_top_ones_labels[0], all_top_ones_labels[1], all_top_ones_labels[2], all_top_ones_labels[3], all_top_ones_labels[4], all_top_ones_labels[5], all_top_ones_labels[6], all_top_ones_labels[7], all_top_ones_labels[8], all_top_ones_labels[9], all_top_ones_labels[10], all_top_ones_labels[11]], loc='upper left')
plt.savefig(out_path + 'overal_top-1_non_normalized.jpg')
plt.close()


# plotting all top-1 normalized by object pixels 
plt.figure(figsize=(25,10))
for lmnop in range(len(labels_dict)):
	plt.plot(x_axis_normalized_obj_all_top_ones[lmnop], all_top_ones[lmnop], linestyle='solid', linewidth = 3, 
		         marker='', markerfacecolor='blue', markersize=7) 
# naming the x axis 
plt.xlabel('ratio of radius of bubbles in pixel.') 
# naming the y axis 
plt.ylabel('number of correct samples from 100 samples for just top-1') 
# giving a title to my graph 
plt.title(' comparing accuracy of top-1s of each classes normalized per object pixels.') 
plt.legend(all_top_ones_labels)
# plt.legend([get_key(all_top_ones_labels[0]), all_top_ones_labels[1], all_top_ones_labels[2], all_top_ones_labels[3], all_top_ones_labels[4], all_top_ones_labels[5], all_top_ones_labels[6], all_top_ones_labels[7], all_top_ones_labels[8], all_top_ones_labels[9], all_top_ones_labels[10], all_top_ones_labels[11]], loc='upper left')
plt.savefig(out_path + 'overal_top-1_normalized_obj.jpg')
plt.close()

# plotting all top-1 normalized by picture pixels 
plt.figure(figsize=(25,10))
for lmnop in range(len(labels_dict)):
	plt.plot(x_axis_normalized_pic_all_top_ones[lmnop], all_top_ones[lmnop], linestyle='solid', linewidth = 3, 
		         marker='', markerfacecolor='blue', markersize=7) 
# naming the x axis 
plt.xlabel('ratio of radius of bubbles in pixel.') 
# naming the y axis 
plt.ylabel('number of correct samples from 100 samples for just top-1') 
# giving a title to my graph 
plt.title(' comparing accuracy of top-1s of each classes normalized per picture pixels.') 
plt.legend(all_top_ones_labels)
# plt.legend([get_key(all_top_ones_labels[0]), all_top_ones_labels[1], all_top_ones_labels[2], all_top_ones_labels[3], all_top_ones_labels[4], all_top_ones_labels[5], all_top_ones_labels[6], all_top_ones_labels[7], all_top_ones_labels[8], all_top_ones_labels[9], all_top_ones_labels[10], all_top_ones_labels[11]], loc='upper left')
plt.savefig(out_path + 'overal_top-1_normalized_pic.jpg')
plt.close()