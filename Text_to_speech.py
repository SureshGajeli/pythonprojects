# Let's start by importing the libraries: tkinter, gTTs, and playsound.

from tkinter import *               # tkinter is a standard GUI library that is used to build GUI applications.
from gtts import gTTS               # gTTs is a python library that is used to convert text to speech.
from playsound import playsound     # playsound is used to play audio files.


# Initializing Window
root = Tk()                     # to initialize tkinter which will be used for GUI.
root.geometry('350x300')        # used to set the width and height of the window.
root.resizable(0, 0)            # used to resize the width and height.
root.config(bg='ghost white')   # used to access window attributes. bg is used to set the background.
root.title("Python - Text_to_Speech")    # set the title of the window.

# Heading
Label(root, text='Text_to_Speech', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='YourVoice', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

# Label() widget is used to display one or more lines of text that users can't be able to modify.
# root is the name which we refer to our window
# text which we display on the label
# font in which the text is written
# pack organized widget in block

# Label
Label(root, text='Enter_Text', font='Aerial 15 bold', bg='white smoke').place(x=20, y=60)
Msg = StringVar()       # Msg is a string type variable
entry_field = Entry(root, textvariable=Msg, width='50')     # Entry() used to create an input text field
entry_field.place(x=20, y=100)                              # textvariable used to retrieve current text to entry widget
# place() organizes widgets by placing them in a specific position in the parent widget.


def text_to_speech():
    """Function to convert text to speech in python"""
    message = entry_field.get()     # message will store the value of entry_field
    speech = gTTS(text=message, lang='en')     # speech stores the converted voice from the text
    speech.save('YourVoice.mp3')    # will save the converted files as Voice over as mp3 files
    playsound('YourVoice.mp3')      # playsound used to play the sound


def exit_():
    """Function to Exit"""
    root.destroy()      # root.destroy() will quit the program by stopping the mainloop().


def reset():
    """Function to reset"""
    Msg.set("")     # reset function set Msg variable to empty string


# Define Buttons
Button(root, text='Play', font='Aerial 15 bold', command=text_to_speech, width=4).place(x=25, y=140)
Button(root, text='Exit', font='Aerial 15 bold', command=exit_, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='Reset', font='Aerial 15 bold', command=reset).place(x=175, y=140)

mainloop()     # executes when we want to run our program
