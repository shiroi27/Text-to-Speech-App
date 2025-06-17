import tkinter as tk
from tkinter import * 
from gtts import gTTS
import os
import time

# Function To Speak Text
def speak_text():
    entered_text = text.get()
    if entered_text.strip() == "" :
        return
    tts = gTTS(text=entered_text, lang='en', slow=False)
    tts.save("output.mp3")
    os.system("afplay output.mp3")
    time.sleep(3)
    os.remove("output.mp3")

# GUI Set Up
root=Tk()
root.title("TEXT TO SPEECH")  # Window bar title (not stylable)
root.geometry("800x400+200+100")
root.resizable(False, False)
root.config(bg="#E3F6F5")

# Header Frame Box
frame = Frame(root, width=800, height=75, bg="#1EBDCF")
frame.place(x=0, y=0) 

# Header Title
title_bar = Label(root,text="💬  TEXT TO SPEECH  🗣️",font=("Times New Roman", 45, "bold"),fg="#000000",bg="#1EBDCF")
title_bar.place(x=130, y=10) 

# Decorative Line
divider = Frame(root, bg="#102542", height=10, width=800)
divider.place(x= 0, y = 75)

# Subheading
subheading = Label(root,text=" ~ENTER YOUR TEXT~ ",font=("Times New Roman", 35, "bold"),fg="#000000",bg="#E3F6F5")
subheading.place(x=200, y=130)

# Entry Field
text = Entry(root,font=("Times New Roman", 30, "bold"),width=40,bg="#F5F5F5",fg="#102542",insertbackground="#102542"
,highlightthickness=2,highlightbackground="#1EBDCF",highlightcolor="#14A098")
text.place(x=100, y=200)

# Speak Button
speak_button = Button(root,text="  SPEAK  ",font=("Times New Roman", 40, "bold"),bg="#7DCFB6",fg="#000000",
activebackground="#09FEC9", activeforeground="#000000" , command= speak_text)
speak_button.place(x = 300 , y = 280  )

root.mainloop()