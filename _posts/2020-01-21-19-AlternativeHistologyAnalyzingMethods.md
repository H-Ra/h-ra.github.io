---
layout: post
title: January 21, 2020 - Finding Other Potential Ways to Analyze Histology Images and Referencing Papers for Gonad Sex and Stage Determination Practice
---

### Lab Work

__Finding Other Potential Ways to Analyze Histology Images - Python__

Today, I searched for other ways to possibly analyze the histology images, besides using ImageJ and Fiji. After searching around for a while, I realized that we could potentially use some sort of deep learning/machine learning algorithm to help detect objects in an image using Python. 

Fiji has a machine learning plugin for segmentation of images called "Trainable Weka Segmentation". I tried to use Trainable Weka Segmentation plugin, but it seems to take a very long time once classifications are made to get an output (I ran the program for over an hour, and there was still no output). This may be due to the processing power of the computer that I am currently using, so it may be a good idea to try this on a computer with a higher processing power. 

_TensorFlow (One possible tool that could be used to analyze the histology images)_

* different stages of detection
	* image classification: identifying what the image "represents" (more information [here](https://www.tensorflow.org/lite/models/image_classification/overview))
	* object detection: identifying the objects in an image using bounding boxes (more information [here](https://www.tensorflow.org/lite/models/object_detection/overview))
	* segmentation: identifying objects in an image down to the specific shape of the object (more information [here](https://www.tensorflow.org/lite/models/segmentation/overview))

__Papers for Gonad Sex and Stage Determination Practice__

Laura sent me some papers to look at to have more practice on determining gonad sex and stage. These papers include: 

1. [Sexual Rhythm in the California Oyster (Ostrea lurida)](https://www.jstor.org/stable/pdf/1658032.pdf)
2. [Spermatogenesis in the California Oyster (Ostrea lurida)](https://www.journals.uchicago.edu/doi/pdfplus/10.2307/1536950)
3. [Development of the Gonads and the Sequence of the Sexual Phases in the California Oyster (Ostrea lurida)](https://escholarship.org/content/qt83w1h8gr/qt83w1h8gr.pdf)

These papers will be helpful in the future in terms of finding other ways to potentially differentiate between stages of sperm for analyzing the histology images. 

---

### Next Steps

Try testing out Tensorflow and Python to see if those would be viable sources to analyze the histology images

