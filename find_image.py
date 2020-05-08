# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:39:36 2020

@author: Aman Dubey
"""
import cv2
import os
path = ".\\database\\"

import math_functions as mf
import preprocess 

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import ZeroPadding2D
from keras.layers import Dropout
from keras.layers import Activation
from keras.models import Model



model = Sequential()
model.add(ZeroPadding2D((1,1),input_shape=(224,224, 3)))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
 
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
 
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
 
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
 
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
 
model.add(Convolution2D(4096, (7, 7), activation='relu'))
model.add(Dropout(0.5))
model.add(Convolution2D(4096, (1, 1), activation='relu'))
model.add(Dropout(0.5))
model.add(Convolution2D(2622, (1, 1)))
model.add(Flatten())
model.add(Activation('softmax'))



model.load_weights('./Utils/vgg_face_weights.h5')

# loading weights
vgg_face_descriptor = Model(inputs=model.layers[0].input, outputs=model.layers[-2].output)


# function to find distance
def who_is_it(img, percent):
    img_representation = vgg_face_descriptor.predict(preprocess.preprocess_image_n(cv2.resize(img,(224,224))))[0,:]
    l = img_representation.shape[0]
    
    ans = 'not in database'
    res = [999,999]
    
    for image_path in os.listdir(path):
        input_path = os.path.join(path, image_path)
        curr = vgg_face_descriptor.predict(preprocess.preprocess_image(input_path))[0,:]
        cosine_similarity = mf.findCosineDistance(img_representation, curr)
        euclidean_distance = mf.findEuclideanDistance(img_representation, curr)
        
        if cosine_similarity<(percent/10) and euclidean_distance<(percent/100)*l:
            if cosine_similarity<res[0] and  euclidean_distance<res[1]:                
                ans = image_path.split("_")[0]
        
    return ans


