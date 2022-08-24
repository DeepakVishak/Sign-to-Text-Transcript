import tkinter as tk
from tkinter import *
import cv2
from PIL import Image,ImageTk
root=tk.Tk()
root.title("Main page")
root.geometry("1024x640")
root.resizable(False,False)

icon = tk.PhotoImage(file = r"icon.png")
root.iconphoto(False,icon)

title_frame=tk.Frame(root,width=1024, height=100,bg="red")
title_frame.grid(row=1,column=1,columnspan=2,pady=5)

window_frame=tk.LabelFrame(root,width=612, height=540,bg="pink")
L1=Label(window_frame,bg="red")
L1.pack()
cap=cv2.VideoCapture(0)
while(True):
    img = cap.read()[1]
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    L1['image'] =img
    root.update()
window_frame.pack(side=tk.BOTTOM)
window_frame.pack(side=tk.LEFT)

content_frame=tk.Frame(root,width=412, height=540,bg="green")
content_frame.grid(row=2,column=2,pady=5)

root.mainloop()
