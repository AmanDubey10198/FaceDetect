# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:10:08 2020

@author: Aman Dubey
"""

import cv2 

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

def face_extractor(img):
    faces = face_classifier.detectMultiScale(img,1.3,5)
    
    if faces is ():
        return None
    
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]
        
    return cropped_face

def find_face(source):
    string = ""
    try:
        frame = cv2.imread(source)
    except (OSError, IOError) as e:
        print("File Not Found" + e )
        return ""
        
    res = face_extractor(frame)
    face_image = None;
    if res is not None:
        face_image = cv2.resize(res, (240,240))
        string="face found"
    else:
        frame = cv2.imread('./Utils/duck.jpg')
        if not string:
            string="No face found"
    
    """
    frame = cv2.resize(frame, (300,300))
    
    cv2.putText(frame,"Press Enter to EXIT", (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
    cv2.putText(frame, string, (0,90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 300,300)
    cv2.imshow('image',frame)
    cv2.waitKey() #change to none *****************
    cv2.destroyAllWindows()
    """
    return face_image

find_face('./DemoFaces/celeb20_b.jpg')