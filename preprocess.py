# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:52:13 2020

@author: Aman Dubey
"""
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.resnet50 import preprocess_input
import numpy as np

#take image path as input
def preprocess_image(image_path):
    # load image from the directory
    img = load_img(image_path, target_size=(224, 224))
    # convert image to array
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

#take image as input
def preprocess_image_n(image):
    img = img_to_array(image)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

    
    
