# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:46:03 2020

@author: Aman Dubey
"""

import cv2

from keras.models import load_model

model = load_model("./Utils/gender_model.h5")
model.load_weights("./Utils/gender_weights4.h5")

def find(img):
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (112,112)).reshape(1,112,112,1)
    
    pre = int(model.predict(img)[0][0])
    
    if pre == 1: 
        return "Male" 
    return "Female"
    
    
    
