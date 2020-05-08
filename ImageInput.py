import cv2 

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')

def face_extractor(img):
    faces = face_classifier.detectMultiScale(img,1.3,5)
    
    if faces is ():
        return None
    
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h,x:x+w]
        
    return cropped_face

def find_face():
    cap = cv2.VideoCapture(0)
    face_image = None
    
    string = "No Face Found"
    while True:
        
        ret,frame = cap.read();
        
        res = face_extractor(frame)
        
        if res is not None:
            face_image = cv2.resize(res, (240,240))
            string="face found"
        
        
        cv2.putText(frame,"Press Enter to EXIT", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, string, (150, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 300,300)
        cv2.imshow('image',frame)
        if cv2.waitKey(1) == 13:
            break
        
        
    cap.release()
    cv2.destroyAllWindows()
    
    return face_image
