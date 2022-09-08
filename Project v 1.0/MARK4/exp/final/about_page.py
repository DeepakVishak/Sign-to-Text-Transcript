import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Tk()
root.title("About Page")
root.geometry("1024x640")
root.resizable(False,False)

icon = tk.PhotoImage(file = r"icon.png")
root.iconphoto(False,icon)

title_frame=tk.Frame(root,width=1024, height=100,bg="white")

img = ImageTk.PhotoImage(Image.open("topicon_GO.png"))
topicon = Label(title_frame, image = img,borderwidth=0)
topicon.place(anchor=NW)

title_frame.grid(row=1,column=1,columnspan=2)

content_frame=tk.Frame(root,width=1024, height=540,bg="blue")
content_frame.grid(row=2,column=1,columnspan=2)

root.mainloop()
