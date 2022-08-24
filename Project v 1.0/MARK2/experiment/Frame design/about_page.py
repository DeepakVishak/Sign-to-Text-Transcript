import tkinter as tk

root=tk.Tk()
root.title("About Page")
root.geometry("1024x640")
root.resizable(False,False)

icon = tk.PhotoImage(file = r"icon.png")
root.iconphoto(False,icon)

title_frame=tk.Frame(root,width=1024, height=100,bg="red")
title_frame.pack()

content_frame=tk.Frame(root,width=1024, height=540,bg="blue")
content_frame.pack(side = tk.BOTTOM)

root.mainloop()
