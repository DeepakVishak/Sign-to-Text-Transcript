import cv2
from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.geometry("700x540")
f1=LabelFrame(root,bg="red")
f1.pack()
L1=Label(f1,bg="red")
L1.pack()
cap=cv2.VideoCapture(0)
handCascade = cv2.CascadeClassifier(r'hand.xml')

while(True):
    img = cap.read()[1]
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hand = handCascade.detectMultiScale(imgGray,1.3,5)
    for (x,y,w,h) in hand :
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    L1['image'] =img
    root.update()
