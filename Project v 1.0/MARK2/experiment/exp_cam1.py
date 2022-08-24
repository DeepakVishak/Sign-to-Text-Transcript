import cv2
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk

root = Tk()
root.geometry("1200x640")

title_frame=tk.Frame(root,width=1200, height=100,bg="white")
img_title = ImageTk.PhotoImage(Image.open("topicon_GO.png"))
topicon = Label(title_frame, image = img_title,bg="red")
topicon.place(x=0,y=0)
title_frame.place(x=0,y=0)

content_frame=Frame(root)
content_frame.config(highlightthickness=1,highlightbackground = "red", highlightcolor= "red")
L2=Label(content_frame,text="Hello",bg="green",width=500,height=100)
L2.pack(anchor=tk.CENTER)
content_frame.place(x=700,y=110,width=480,height=490)


f1=LabelFrame(root,bg="red")
f1.config(highlightthickness=1,highlightbackground = "green", highlightcolor= "green")
f1.place(x=10,y=110)
L1=Label(f1,bg="red")
L1.pack()

cap=cv2.VideoCapture(0)
cap.set(1,602)
cap.set(1,530)
cap.set(10,100)

while(True):
    img = cap.read()[1]
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    L1['image'] =img
    root.update()



root.mainloop()
