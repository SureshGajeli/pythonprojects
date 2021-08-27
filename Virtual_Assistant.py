import speech_recognition as sr
import pyttsx3
import webbrowser
from tkinter import *
import wikipedia

engine = pyttsx3.init()

# some predefined chats
greetings = ['hello', 'hi', 'hey']
wish = {"morning": "Good Morning", "night": "Good Night", "care": "You too", "bye": "Please don't go"}
silly = {"marry": "No, I have a boyfriend", "love": "I love myself", "hate": "lmao, look at your face",
         "children": "oh please"}


def check():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        order = r.recognize_google(audio, language="en-in")
    e2.insert(END, order)
    x = order.split(" ")
    for word in x:
        if word in greetings:
            answer = "hey, my name is suri, How are you?"
        elif word in wish:
            answer = wish[word]
            engine.say(answer)
            engine.runAndWait()
            e1.insert(END, answer)
        elif "play" in x:
            webbrowser.open_new(f'https://www.youtube.com/results?search_query={x[1]}')
        elif "search" in x:
            webbrowser.open_new(f'https://www.google.com/search?sxsrf={x[1]}')
        elif word in silly:
            answer = silly[word]
            engine.say(answer)
            engine.runAndWait()
            e1.insert(END, answer)
        elif "quit" in x:
            root.destroy()


root = Tk()
root.geometry('200x300')
root.title('Virtual Assistant')
root.config(bg='black')

e1 = Text(root).place(x=10, y=35, height=50, width=180)
Label(root, text='Output').place(x=10, y=5)

e2 = Text(root).place(x=10, y=150, height=30, width=180)
Label(root, text='User Input').place(x=10, y=120)

Button(root, text='Speak', bg='red', fg='white', command=check).place(x=50, y=200, height=50, width=100)

mainloop()

