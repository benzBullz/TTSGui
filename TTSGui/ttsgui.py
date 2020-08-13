from tkinter import *
from gtts import gTTS
from playsound import playsound
import random

root = Tk()
root.title("TTSGui")

text = Entry(root, width=20)
text.pack()

def button_func():
    txt = text.get()
    rand = random.randint(1,999999999)

    tts = gTTS(txt)

    path = f"logs\\tts{rand}.mp3"
    tts.save(path)
    playsound(path)

    print(f"'{txt}' played")
    
button = Button(root, text="Speech",command=button_func,width=16)
button.pack()
root.mainloop()
