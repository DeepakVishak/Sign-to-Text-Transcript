import tkinter as tk
from tkVideoPlayer import TkinterVideo

def disable_event():
   pass

root = tk.Tk()
root.geometry("500x500")
root.resizable(False,False)
root.title("Welcome")
root.iconbitmap(r"icon.ico")


videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(r"GO.mp4")
videoplayer.pack(expand=True, fill="both")

videoplayer.play()

root.protocol("WM_DELETE_WINDOW", disable_event)
root.after(1300,lambda:root.destroy())
root.mainloop()

