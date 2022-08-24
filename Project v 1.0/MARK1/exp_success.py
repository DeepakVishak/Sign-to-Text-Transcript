import tkinter as tk
from tkinter import *

def eve(event):
    res=txt1.get("1.0", "end-1c")
    txt2.delete("1.0",tk.END)
    txt2.insert(tk.END,res)

def cb():
    root.clipboard_clear()
    res1=txt2.get("1.0", "end-1c")
    root.clipboard_append(res1)
    root.update() 
    
    
    
root=tk.Tk()
root.title("Get String on runtime")

txt1= Text(root)
txt1.pack()

txt2= Text(root)
txt2.pack()

butt= Button(root,text="COPY TO CLIPBOARD",command=cb)
butt.pack()

txt1.bind('<KeyRelease>',eve)


root.mainloop()
