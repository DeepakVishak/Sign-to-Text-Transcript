import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import cv2

#main window configuration
root=tk.Tk()
root.title("Main page")
root.geometry("1024x640")
root.resizable(False,False)
icon = tk.PhotoImage(file = r"icon.png")
root.iconphoto(False,icon)

#title frame
title_frame=tk.Frame(root,width=1024, height=100,bg="white")
img = ImageTk.PhotoImage(Image.open("topicon_GO.png"))
topicon = Label(title_frame, image = img,borderwidth=0)
topicon.place(anchor=NW)
title_frame.grid(row=1,column=1,columnspan=2,pady=5)

#open cv window frame
window_frame=tk.Frame(root,width=612, height=540)
window_frame.grid(row=2,column=1,pady=5)

#Text box and button frame
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


content_frame=tk.Frame(root,width=412, height=540,bg="white")
txt_label=Label(content_frame,text="Generated Text will appear below...",bg="white",font="Helvetica 9 italic")
txt_label.place(relx=0.01,y=0.01)
txt_display=Text(content_frame,highlightthickness=1)
txt_display.bind("<Button-1>",active_txt)
txt_display.config(highlightthickness=1,highlightbackground = "grey", highlightcolor= "grey")
txt_display.place(relx=0.01,rely=0.06,height=250,width=400)


img1 = ImageTk.PhotoImage(Image.open("button_copy-to-clipboard_inactive.png"))
clipboard = Label(content_frame, image = img1,borderwidth=0,bg="white")
clipboard.bind('<Enter>',active_clipboard)
clipboard.bind('<Leave>',inactive_clipboard)
clipboard.place(relx=0.03,rely=0.04,x=10,y=270,height=66,width=357)


img2 = ImageTk.PhotoImage(Image.open("button_clear-to-defaults_inactive.png"))
clear = Label(content_frame, image = img2,borderwidth=0,bg="white")
clear.bind('<Enter>',active_clear)
clear.bind('<Leave>',inactive_clear)
clear.place(relx=0.03,rely=0.04,x=10,y=350,height=66,width=357)

content_frame.grid(row=2,column=2,pady=5)


root.configure(bg="white")
root.mainloop()
