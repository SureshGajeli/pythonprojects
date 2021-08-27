import os
from tkinter import *


def rename():
    folder_path = r''+path.get()
    counter = 1
    for file_name in os.listdir(folder_path):
        os.rename(folder_path + '\\' + file_name, folder_path + '\\' + word.get() + str(counter) + exe.get())
        counter += 1
    Ent.delete(0, END)
    Ent2.delete(0, END)
    exe.delete(0, END)


root = Tk()
root.title('RENAMER')
root.geometry('300x300')

path = StringVar()
Label(root, text='Paste File Path', font='Aerial 15').pack()
Ent = Entry(root, textvariable=path, font='Aerial 15')
Ent.pack()

word = StringVar()
Label(root, text='Give One Word', font='Aerial 15').pack()
Ent2 = Entry(root, textvariable=word, font='Aerial 15')
Ent2.pack()

exe = StringVar()
Label(root, text='ENTER EXTENSION', font='Aerial 15').pack()
exe = Entry(root, textvariable=exe, font='Aerial 15')
exe.pack()

Button(root, text='change', command=rename).pack()

mainloop()