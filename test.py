# # import cv2
# # import numpy
# # import os

# # # # def fd(input_img):
# # # #     gray_img=cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
# # # #     face_harr=cv2.CascadeClassifier('/home/zaidqam/Desktop/final_project_sqlite/haarcascade_frontalface_default.xml')e
# # # #     faces=face_harr.detectMultiScale(gray_img,scaleFactor=1.3,minNeighbors=3)
# # # #     return faces,gray_img

# # face_cap=cv2.CascadeClassifier('/home/zaidqam/Desktop/final_project_sqlite/haarcascade_frontalface_default.xml')
# # cap=cv2.VideoCapture(0)
# # while True:
# #     ret, frame=cap.read()
# #     col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# #     faces=face_cap.detectMultiScale(
# #         col,
# #         scaleFactor=1.1,
# #         minNeighbors=5,
# #         minSize=(30,30),
# #         flags=cv2.CASCADE_SCALE_IMAGE
# #     )
# #     cv2.imshow('frame',frame)
# #     # cv2.imshow('faces',faces)
# #     print(frame)
# #     for (x,y,w,h) in faces:
# #         # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
# #         face_cropped=frame[y:y+h,x:x+w]

# #     cv2.imshow('frame',frame)
# #     if  cv2.waitKey(10)== ord('q'):
# #         break
# # cap.release()
# # cv2.destroyAllWindows()
# # # import cv2
# # # cas=cv2.CascadeClassifier("/home/zaidqam/Desktop/final_project_sqlite/haarcascade_frontalface_default.xml")
# # # cap=cv2.VideoCapture(0)
# # # while True:
# # #     ret,frame=cap.read()
# # #     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# # #     faces=cas.detectMultiScale(
# # #         gray,1.1,5
# # #     )
# # #     # cv2.imshow('frame',frame)
# # #     # cv2.imshow('faces',faces)
# # #     for (x,y,w,h) in faces:
# # #             face_cropped=frame[y:y+h,x:x+w]
# # #     cv2.imshow('crop',frame)
# # importing the required modules  
# from tkinter import *                   # importing all the widgets and modules from tkinter  
# from tkinter import messagebox as mb    # importing the messagebox module from tkinter  
# from tkinter import filedialog as fd    # importing the filedialog module from tkinter  
# import os                               # importing the os module  
# import shutil 
# # import os
# import webbrowser
# # def func():
# #     # webbrowser.open("/home/zaidqam/Desktop/final_project_sqlite/data")//
# #     os.system('open "%s" '"/home/zaidqam/Desktop/final_project_sqlite/data")
# # os.system(r'xdg-open /home/zaidqam/Desktop/final_project_sqlite/data')
# # defining a function to open a folder  
#    # using the filedialog's askdirectory() method to select the folder  
# the_folder = fd.askdirectory(title = "Select Folder to open")  
# # using the startfile() of the os module to open the selected folder  
# os.system(r'xdg-open /home/zaidqam/Desktop/final_project_sqlite/data')
# os.li
import cv2
import os
import numpy as np
from PIL import Image, ImageTk
data_dir=('/home/zaidqam/Desktop/final_project_sqlite/data')
path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

faces=[]
ids=[]
for image in path:
        img=Image.open(image).convert('L')
        imageNp=np.array(img,'uint8')
        id=int(os.path.split(image)[1].split('.')[1])

        faces.append(imageNp)
        ids.append(id)
        cv2.imshow('Training',imageNp)
        cv2.waitKey(1)==13
# print(ids)
ids=np.array(ids)

lbph=cv2.face.LBPHFaceRecognizer_create()




# cv2.imshow("img",gray)