import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import webbrowser

def callback_email(event):
   url = "mailto:deepak474700@gmail.com"
   webbrowser.open_new_tab(url)
def callback_github(event):
   url = "https://github.com/DeepakVishak"
   webbrowser.open_new_tab(url)
def callback_linkedin(event):
   url = "https://www.linkedin.com/in/deepak-vishak-0417b9201/"
   webbrowser.open_new_tab(url)
def user_manual_redirect(event):
   pass
def active_user_manual(event):
   user_manual.config(image=img11)
def inactive_user_manual(event):
   user_manual.config(image=img1)

def about_window():
   root = tk.Tk()
   root.title("About Page")
   app_width = 1200
   app_height = 640
   screen_width = root.winfo_screenwidth()
   screen_height = root.winfo_screenheight()
   x = (screen_width/2) - (app_width/2)
   y = (screen_height/2) - (app_height/2)

   root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
   root.resizable(False,False)

   root.iconbitmap(r"components/icon.ico")
   title_frame=tk.Frame(root,width=1200, height=100,bg="white")

   img = ImageTk.PhotoImage(Image.open("components/topicon_GO.png"),master=root)
   topicon = Label(title_frame, image = img,borderwidth=0)
   topicon.place(anchor=NW)

   title_frame.grid(row=1,column=1,columnspan=2)

   content_frame_1=tk.Frame(root,width=600, height=520,bg="white")

   about_heading = Label(content_frame_1,fg="blue",text="About Us")
   about_heading.configure(font=("Helvetica bold",18),bg="white")
   about_heading.place(x=20,y=10)

   credits_img = ImageTk.PhotoImage(Image.open("components/credits.png"),master=root)
   credits_label = Label(content_frame_1, image = credits_img,borderwidth=0)
   credits_label.place(x=50,y=50)
   contact_heading = Label(content_frame_1,fg="blue",text="Contact")
   contact_heading.configure(font=("Helvetica bold",18),bg="white")
   contact_heading.place(x=20,y=460)
   contact_img = ImageTk.PhotoImage(Image.open("components/email.png"),master=root)
   contact_email = Label(content_frame_1, image = contact_img,borderwidth=0,bg="white")
   contact_email.bind("<Button-1>",callback_email)
   contact_email.place(x=120,y=460)
   contact_img1 = ImageTk.PhotoImage(Image.open("components/github.png"),master=root)
   contact_github = Label(content_frame_1, image = contact_img1,borderwidth=0,bg="white")
   contact_github.bind("<Button-1>", callback_github)
   contact_github.place(x=160,y=460)
   contact_img2 = ImageTk.PhotoImage(Image.open("components/linkedin.png"),master=root)
   contact_linkedin = Label(content_frame_1, image = contact_img2,borderwidth=0,bg="white")
   contact_linkedin.bind("<Button-1>",callback_linkedin)
   contact_linkedin.place(x=200,y=460)
   content_frame_1.grid(row=2,column=1)

   global img11
   img11 = ImageTk.PhotoImage(Image.open("components/button_user-manual_active.png"),master=root)
   content_frame_2=tk.Frame(root,width=600, height=520,bg="white")
   tools_img = ImageTk.PhotoImage(Image.open("components/tools_platforms.png"),master=root)
   tools_label = Label(content_frame_2, image = tools_img,borderwidth=0)
   tools_label.place(x=50,y=10)
   global img1
   img1 = ImageTk.PhotoImage(Image.open("components/button_user-manual_inactive.png"),master=root)
   global user_manual
   user_manual = Label(content_frame_2, image = img1,borderwidth=0,bg="white")
   user_manual.bind('<Button-1>',user_manual_redirect)
   user_manual.bind('<Enter>',active_user_manual)
   user_manual.bind('<Leave>',inactive_user_manual)
   user_manual.place(relx=0.01,rely=0.04,x=190,y=400,height=66,width=240)
   content_frame_2.grid(row=2,column=2)

   content_frame_3=tk.Frame(root,width=1200,height=20,bg="white")
   var= StringVar()
   content3 = tk.Label(content_frame_3,textvariable=var,fg="black",bg="white")
   var.set("© All rights are reserved.")
   content3.place(x="540",y="1")
   content_frame_3.grid(row=3,column=1,columnspan=2)
   root.mainloop()


