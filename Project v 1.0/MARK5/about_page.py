import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root=tk.Tk()
root.title("About Page")
app_width = 1200
app_height = 640
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
root.resizable(False,False)

icon = tk.PhotoImage(file = r"components/icon.png")
root.iconphoto(False,icon)

title_frame=tk.Frame(root,width=1200, height=100,bg="white")

img = ImageTk.PhotoImage(Image.open("components/topicon_GO.png"))
topicon = Label(title_frame, image = img,borderwidth=0)
topicon.place(anchor=NW)

title_frame.grid(row=1,column=1,columnspan=2)

content_frame_1=tk.Frame(root,width=600, height=520,bg="red")

about_heading = Label(content_frame_1,fg="blue",text="About Us")
about_heading.configure(font=("Helvetica bold",18),bg="white")
about_heading.place(x=20,y=10)

credits_img = ImageTk.PhotoImage(Image.open("components/credits.png"))
credits_label = Label(content_frame_1, image = credits_img,borderwidth=0)
credits_label.place(x=50,y=50)
content_frame_1.grid(row=2,column=1)


content_frame_2=tk.Frame(root,width=600, height=520,bg="yellow")
tools_img = ImageTk.PhotoImage(Image.open("components/tools_platforms.png"))
tools_label = Label(content_frame_2, image = tools_img,borderwidth=0)
tools_label.place(x=50,y=10)
content_frame_2.grid(row=2,column=2)

content_frame_3=tk.Frame(root,width=1200,height=20,bg="white")
var= StringVar()
content3 = tk.Label(content_frame_3,textvariable=var,fg="black",bg="white")
var.set("© All rights are reserved.")
content3.place(x="540",y="1")
content_frame_3.grid(row=3,column=1,columnspan=2)
root.mainloop()
