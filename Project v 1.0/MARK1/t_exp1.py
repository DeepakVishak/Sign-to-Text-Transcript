from tkinter import *
from tkinter import messagebox

root=Tk()

def alertme(*args):
    messagebox.showinfo("Message", "you press Enter in textbox")

def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)

textBox=Text(root, height=2, width=10)
textBox.pack()

textBox.bind("<Return>", alertme) #this line calls alertme function whenever you press Enter key

buttonCommit=Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
buttonCommit.pack()
mainloop()
        
