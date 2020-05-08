import ImageInput as IM
import ImageInputSrc as IMS
import save_in_folder as SIF
import find_image as FI
import find_gender as FG
import cv2
import numpy as np

def saveOrFind(face):
   
    print("S -> Saving the image in database")
    print("F -> Finding the image in database")
    print("Any Key -> For leaving")
    
    percent = 5 # total percentage of error accepted
    
    option = input()
    
    if(option == "S" or option == "s"):
        #call function
        SIF.save_img(face)
    elif(option == "F" or option == "f"):
        # call another function
        print(">>> " + FI.who_is_it(face, percent))
        
    else:
        print(">>> WRONG INPUT")
    
    
def main():

    print("***********FACE RECOGNITION SYSTEM*****************")
    while True:
        print("1. For providing the image using the webcam")
        print("2. For providing the image using the image path")
        print("3. EXIT") 

        choice = int(input())

    
        if choice == 1:
            #call function
            curr = IM.find_face()
            aux = np.copy(curr)
            
            cv2.putText(aux, FG.find(aux), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow("Captured Face", aux)
            cv2.waitKey()
            cv2.destroyAllWindows()
            saveOrFind(curr)
            
        elif choice == 2:
            # call function
            path = input()
            #curr = IMS.find_face("./DemoFaces/celeb"+path+"_b.jpg")
            curr = IMS.find_face(path)
            
            aux = np.copy(curr)
            
            cv2.putText(aux, FG.find(aux), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow("Captured Face", aux)
            cv2.waitKey()
            cv2.destroyAllWindows()
            saveOrFind(curr)
        elif choice == 3:
            print(">>> THANK YOU!!!")
            break
        else:
            print(">>> WRONG INPUT")


if __name__ == "__main__":
    main()  