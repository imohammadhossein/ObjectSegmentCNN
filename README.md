<h1 align="center">Object Segment CNN</h1>

<h6 align="center">A Comparison Between Human Visual Perception Under Object Segmentation and Recognition with Current Deep Neural Networks.</h6>

<h3 align="center">Abstract</h1>

> - The idea behind this work is comparing the attention of deep convolutional neural networks and human visual perception system in classifying objects. In proposed research, diagnostic regions for human visual system and famous deep convolutional neural networks have been calculated; these regions are the most salient areas of each image which have led to accurate classification. They persumably have more meanings (than other regions) for each systems respectively. 

> - We computed the diagnostic features of each image in each category with 5 convolutional networks ([VGG16](https://arxiv.org/abs/1409.1556), [ResNet50](https://arxiv.org/abs/1512.03385), [EfficientNetb0](https://arxiv.org/abs/1905.11946),  [AlexNet](https://proceedings.neurips.cc/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) and [DenseNet-169](https://arxiv.org/pdf/1608.06993.pdf)), 5 saliency models ([GBVS](https://proceedings.neurips.cc/paper/2006/file/4db0f8b0fc895da263fd77fc8aecabe4-Paper.pdf), [Itti](https://www.researchgate.net/publication/3192913_A_Model_of_Saliency-based_Visual_Attention_for_Rapid_Scene_Analysis), [Signature](https://cvhci.anthropomatik.kit.edu/~bschauer/pdf/schauerte2012predicting.pdf), [Simpsal](https://arxiv.org/pdf/2010.12913.pdf) and [Spectral](https://www.researchgate.net/publication/221364530_Saliency_Detection_A_Spectral_Residual_Approach)) and finally with human visual perception system under a designed behavioural task.

> - Have a look at following visual results for each section.

<h3 align="center">Results</h1>

 - **On Deep CNNs** 

| VGG16           | ![VGG-16](images/DCNNs/VGG1.jpg)          | ![VGG-16](images/DCNNs/VGG2.jpg)  	      | ![VGG-16](images/DCNNs/VGG3.jpg)  	    | ![VGG-16](images/DCNNs/VGG4.jpg)  	      | ![VGG-16](images/DCNNs/VGG5.jpg)  	      |
|:---------------:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|:-------------------------------------:|
| ResNet-50 	  | ![ResNet-50](images/DCNNs/RES1.jpg)   	| ![ResNet-50](images/DCNNs/RES2.jpg)  	  | ![ResNet-50](images/DCNNs/RES3.jpg)  	    | ![ResNet-50](images/DCNNs/RES4.jpg)  	  | ![ResNet-50](images/DCNNs/RES5.jpg)    	  |
| DenseNet-169    | ![DenseNet-169](images/DCNNs/DNS1.jpg)    | ![DenseNet-169](images/DCNNs/DNS2.jpg)    | ![DenseNet-169](images/DCNNs/DNS3.jpg)    | ![DenseNet-169](images/DCNNs/DNS4.jpg)    | ![DenseNet-169](images/DCNNs/DNS5.jpg)      |
| AlexNet  	      | ![Alex Net](images/DCNNs/ALX1.jpg)        | ![Alex Net](images/DCNNs/ALX2.jpg)  	  | ![Alex Net](images/DCNNs/ALX3.jpg)  	    | ![Alex Net](images/DCNNs/ALX4.jpg)  	  | ![Alex Net](images/DCNNs/ALX5.jpg)  	      |
| EfficientNet-b0 | ![EfficientNet-b0](images/DCNNs/EFF1.jpg) | ![EfficientNet-b0](images/DCNNs/EFF2.jpg) | ![EfficientNet-b0](images/DCNNs/EFF3.jpg) | ![EfficientNet-b0](images/DCNNs/EFF4.jpg) | ![EfficientNet-b0](images/DCNNs/EFF5.jpg)   |

 - **On Saliency Models** (will be added)
 

| GBVS           | ![GBVS](images/Saliencies/GBVS1.jpg)          | ![GBVS](images/Saliencies/GBVS2.jpg)  	      | ![GBVS](images/Saliencies/GBVS3.jpg)  	    | ![GBVS](images/Saliencies/GBVS4.jpg)  	      | ![GBVS](images/Saliencies/GBVS5.jpg)  	      |
|:---------------:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|:-----------------------------------:|:-------------------------------------:|
| Itti-Koch 	  | ![Itti-Koch](images/Saliencies/itti1.jpg)   	| ![Itti-Koch](images/Saliencies/itti2.jpg)  	  | ![Itti-Koch](images/Saliencies/itti3.jpg)  	    | ![Itti-Koch](images/Saliencies/itti4.jpg)  	  | ![Itti-Koch](images/Saliencies/itti5.jpg)    	  |
| Signature    | ![Signature](images/Saliencies/Signature1.jpg)    | ![Signature](images/Saliencies/Signature2.jpg)    | ![Signature](images/Saliencies/Signature3.jpg)    | ![Signature](images/Saliencies/Signature4.jpg)    | ![Signature](images/Saliencies/Signature5.jpg)      |
| Simpsal  	      | ![Simpsal](images/Saliencies/Simpsal1.jpg)        | ![Simpsal](images/Saliencies/Simpsal2.jpg)  	  | ![Simpsal](images/Saliencies/Simpsal3.jpg)  	    | ![Simpsal](images/Saliencies/Simpsal4.jpg)  	  | ![Simpsal](images/Saliencies/Simpsal5.jpg)  	      |
| Spectral | ![EfficientNet-b0](images/Saliencies/EFF1.jpg) | ![EfficientNet-b0](images/Saliencies/EFF2.jpg) | ![EfficientNet-b0](images/Saliencies/EFF3.jpg) | ![EfficientNet-b0](images/Saliencies/EFF4.jpg) | ![EfficientNet-b0](images/Saliencies/EFF5.jpg)   |

> - OSF project.
> - youtube presentation 
> - Abstract articles
> - Code explanation for permutation tests
> - Behavioural task

<details>
<summary>Preview</summary>

{% highlight ruby %}
puts 'Expanded message'
{% endhighlight %}

</details>

## Feedback

If you had any feedback or question, please reach out to me at mh.nikimaleki@gmail.com
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mhnikimaleki/)
