import cv2
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
from tensorflow import keras
import numpy as np
import tensorflow as tf


exec(open('entry.py').read())
root = Tk()
app_width = 1200
app_height = 640
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

root.title("Home Page")
root.resizable(False,False)
root.iconbitmap(r"components/icon.ico")
root.configure(bg="white")
result=""

def confirm_event():
    confirm = messagebox.askyesno("Quit", "Are you sure you want to quit?")
    if(confirm):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", confirm_event)

def about_page(event):
    exec(open('about_page.py').read())

title_frame=tk.Frame(root,width=1200, height=100,bg="white")
img_title = ImageTk.PhotoImage(Image.open("components/topicon_GO.png"))
topicon = Label(title_frame, image = img_title,bg="white")
topicon.bind('<Button-1>',about_page)
topicon.place(x=0,y=0)
title_frame.place(x=0,y=0)

img11 = ImageTk.PhotoImage(Image.open("components/button_copy-to-clipboard_active.png"))
img21 = ImageTk.PhotoImage(Image.open("components/button_clear-to-defaults_active.png"))

def active_clipboard(event):
    clipboard.config(image=img11)
def inactive_clipboard(event):
    clipboard.config(image=img1)
def copy_clipboard(event):
    res = txt_display.get("1.0", "end-1c")
    root.clipboard_append(res)

def active_clear(event):
    clear.config(image=img21)
def inactive_clear(event):
    clear.config(image=img2)
def clear_to_defaults(event):
    txt_display.delete("1.0",tk.END)
    result=""


def active_txt(event):
    txt_display.config(highlightbackground = "blue", highlightcolor= "blue")

def insert_txt_display(result):
    # result = [x.lower() for x in result]
    # final = ""
    # for i in result:
    #     final+=i
    #res = txt_display.get("1.0", "end-1c") + final
    res = txt_display.get("1.0", "end-1c") + result
    txt_display.delete("1.0", tk.END)
    txt_display.insert(tk.END, res)
    root.update()



content_frame=Frame(root,bg="white")
content_frame.config(highlightthickness=1,highlightbackground = "white", highlightcolor= "white")
txt_label=Label(content_frame,text="Generated Text will appear below...",bg="white",font="Helvetica 9 italic")
txt_label.place(relx=0.08,y=0.01)
txt_display=Text(content_frame,highlightthickness=1)
txt_display.bind("<Button-1>",active_txt)
txt_display.config(highlightthickness=1,highlightbackground = "grey", highlightcolor= "grey")
txt_display.place(relx=0.08,rely=0.06,height=250,width=400)


img1 = ImageTk.PhotoImage(Image.open("components/button_copy-to-clipboard_inactive.png"))
clipboard = Label(content_frame, image = img1,borderwidth=0,bg="white")
clipboard.bind('<Button-1>',copy_clipboard)
clipboard.bind('<Enter>',active_clipboard)
clipboard.bind('<Leave>',inactive_clipboard)
clipboard.place(relx=0.1,rely=0.04,x=10,y=270,height=66,width=357)


img2 = ImageTk.PhotoImage(Image.open("components/button_clear-to-defaults_inactive.png"))
clear = Label(content_frame, image = img2,borderwidth=0,bg="white")
clear.bind('<Button-1>',clear_to_defaults)
clear.bind('<Enter>',active_clear)
clear.bind('<Leave>',inactive_clear)
clear.place(relx=0.1,rely=0.04,x=10,y=350,height=66,width=357)
content_frame.place(x=700,y=110,width=480,height=490)


f1=LabelFrame(root,bg="white")
f1.config(highlightthickness=1,highlightbackground = "white", highlightcolor= "white")
f1.place(x=10,y=110)
L1=Label(f1)
L1.pack()

cap=cv2.VideoCapture(0)
cap.set(1,602)
cap.set(1,530)
cap.set(10,100)

model = keras.models.load_model("my_model.h5")
class_labels=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'BLANK', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
flag=0
while(True):

    ret , frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    roi = cv2.rectangle(frame, (320, 10), (610, 290), (0, 0, 255), 2)


    #Extract grayscale image image of roi and removing noise using Gaussian blur
    extract= frame[10:290,320:610]
    gray = cv2.cvtColor(extract, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, test_image = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    test_img = cv2.resize(test_image,(28,28),interpolation = cv2.INTER_CUBIC)
    test_img = cv2.cvtColor(test_img,cv2.COLOR_GRAY2RGB)
    test_arr = np.asarray(test_img)
    #print(test_arr.shape)
    test_arr = tf.expand_dims(test_arr, 0)
    #print(test_arr)
    #print(test_arr.shape)
    #test_arr = tf.reshape(test_arr,list(test_arr.shape) + [1])

    predictions = model.predict(test_arr)
    score = tf.nn.softmax(predictions[0])

    start_point = (410,290)
    end_point = (530,320)
    color = (0,0,255)
    thickness = -1
    cv2.rectangle(frame,start_point,end_point,color,thickness)
    cv2.putText(frame,'{} : {:.2f}'.format(class_labels[np.argmax(score)], 100 * np.max(score)),(410,310),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    """
    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_labels[np.argmax(score)], 100 * np.max(score))
    )
    """
    predict_final = class_labels[np.argmax(score)]
    score_final = 100 * np.max(score)


    if(predict_final != 'BLANK' and score_final >= 99):
        result = class_labels[np.argmax(score)]
        result = result.lower()
        flag = 0
    if(predict_final == 'BLANK' and score_final >= 99 and flag == 0):
        insert_txt_display(result)
        flag = 1




    """
    if(score_final>=99):
        if(len(sentence)>0 and predict_final!="BLANK"):
            if(predict_final!=sentence[-1]):
                sentence.append(predict_final)
        else:
            if(predict_final!="BLANK"):
                sentence.append(predict_final)

    if(len(sentence)>5):
        sentence = sentence[-5:]

    print(sentence)
    #insert_txt_display(sentence)
    """

    # Display the resulting frame
    #cv2.imshow('Gray',gray)
    #cv2.imshow('frame', frame)
    #cv2.imshow("test", test_image)
    #cv2.imshow("test img",test_img)
    img_res = ImageTk.PhotoImage(Image.fromarray(frame))
    L1['image'] =img_res
    root.update()







