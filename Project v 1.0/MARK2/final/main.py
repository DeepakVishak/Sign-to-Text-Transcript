import cv2
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox

root = Tk()
root.geometry("1200x640")
root.title("Home Page")
root.resizable(False,False)
root.iconbitmap(r"icon.ico")
root.configure(bg="white")

def confirm_event():
    confirm = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if(confirm):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", confirm_event)


title_frame=tk.Frame(root,width=1200, height=100,bg="white")
img_title = ImageTk.PhotoImage(Image.open("topicon_GO.png"))
topicon = Label(title_frame, image = img_title,bg="white")
topicon.place(x=0,y=0)
title_frame.place(x=0,y=0)

img11 = ImageTk.PhotoImage(Image.open("button_copy-to-clipboard_active.png"))
img21 = ImageTk.PhotoImage(Image.open("button_clear-to-defaults_active.png"))
def active_clipboard(event):
    clipboard.config(image=img11)
def inactive_clipboard(event):
    clipboard.config(image=img1)

def active_clear(event):
    clear.config(image=img21)
def inactive_clear(event):
    clear.config(image=img2)

def active_txt(event):
    txt_display.config(highlightbackground = "blue", highlightcolor= "blue")


content_frame=Frame(root,bg="white")
content_frame.config(highlightthickness=1,highlightbackground = "white", highlightcolor= "white")
txt_label=Label(content_frame,text="Generated Text will appear below...",bg="white",font="Helvetica 9 italic")
txt_label.place(relx=0.08,y=0.01)
txt_display=Text(content_frame,highlightthickness=1)
txt_display.bind("<Button-1>",active_txt)
txt_display.config(highlightthickness=1,highlightbackground = "grey", highlightcolor= "grey")
txt_display.place(relx=0.08,rely=0.06,height=250,width=400)


img1 = ImageTk.PhotoImage(Image.open("button_copy-to-clipboard_inactive.png"))
clipboard = Label(content_frame, image = img1,borderwidth=0,bg="white")
clipboard.bind('<Enter>',active_clipboard)
clipboard.bind('<Leave>',inactive_clipboard)
clipboard.place(relx=0.1,rely=0.04,x=10,y=270,height=66,width=357)


img2 = ImageTk.PhotoImage(Image.open("button_clear-to-defaults_inactive.png"))
clear = Label(content_frame, image = img2,borderwidth=0,bg="white")
clear.bind('<Enter>',active_clear)
clear.bind('<Leave>',inactive_clear)
clear.place(relx=0.1,rely=0.04,x=10,y=350,height=66,width=357)
content_frame.place(x=700,y=110,width=480,height=490)


f1=LabelFrame(root,bg="white")
f1.config(highlightthickness=1,highlightbackground = "white", highlightcolor= "white")
f1.place(x=10,y=110)
L1=Label(f1)
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




