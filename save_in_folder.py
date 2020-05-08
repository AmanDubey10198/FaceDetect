# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:17:46 2020

@author: Aman Dubey
"""
import cv2
# File for saving the image
def save_img(image):
    print("Enter the name of the person")
    name = input().strip()
    
    print("Enter the unique id for the person")
    ID = input().strip()
    
    string = name+"_"+ID
    
    file_path = './database/'+ string +'.jpg'
    
    cv2.imwrite(file_path, image)
    
    print("Image saved!!!")
    
    
    
    
    