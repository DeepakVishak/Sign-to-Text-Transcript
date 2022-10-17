import tkinter as tk
from tkVideoPlayer import TkinterVideo

def disable_event():
   pass

root = tk.Tk()
root.geometry("1200x640")
root.resizable(False,False)
root.title("Welcome")
root.iconbitmap(r"components/icon.ico")


videoplayer = TkinterVideo(master=root,scaled=False)
videoplayer.load(r"components/GO.mp4")
videoplayer.pack(expand=True,fill="both")
videoplayer.configure(bg="white")
videoplayer.play()

root.protocol("WM_DELETE_WINDOW", disable_event)
root.after(1300,lambda:root.destroy())

root.mainloop()

