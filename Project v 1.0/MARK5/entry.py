import tkinter as tk
from tkVideoPlayer import TkinterVideo

def disable_event():
   pass

root = tk.Tk()
app_width = 1200
app_height = 640
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
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

