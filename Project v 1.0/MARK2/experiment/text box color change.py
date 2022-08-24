# import tkinter
from tkinter import *

# Create Tk object
window = Tk()

# Set the window title
window.title('GFG')

# Entry Widget
# highlightthickness for thickness of the border
entry = Entry(highlightthickness=1,highlightbackground = "grey", highlightcolor= "grey")
button = Button(window,text="Click")

# highlightbackground and highlightcolor for the border color
def act(event):
    entry.config(highlightbackground = "blue", highlightcolor= "blue")
entry.bind('<FocusIn>',act)




# Place the widgets in window
entry.pack(padx=20, pady=20)
button.pack(padx=20, pady=20)

window.mainloop()
