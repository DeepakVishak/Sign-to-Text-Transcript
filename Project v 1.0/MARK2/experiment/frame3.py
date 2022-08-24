from tkinter import *
import tkinter as tk

root = Tk()
root.geometry("1200x640")

content_frame=Frame(root)
L2=Label(content_frame,text="Hello",bg="green",width=500,height=100)
L2.pack(anchor=tk.CENTER)
content_frame.place(x=700,y=110,width=480,height=500)

root.mainloop()