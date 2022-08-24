import tkinter as tk
from tkinter import *
import randstr as rs

def w():
    s=rs.randstr()
    txt1.insert(tk.END,s)
    
root=tk.Tk()
root.title("Get String on runtime")

txt1= Text(root)
txt1.pack()

for i in range(20):
    w()
root.mainloop()
