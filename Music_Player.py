from pygame import mixer
from tkinter import *
import os


def play_song():
    current_song = play_list.get(ACTIVE)
    print(current_song)
    mixer.music.load(current_song)
    song_status.set('Playing')
    mixer.music.play()


def pause_song():
    song_status.set('Paused')
    mixer.music.pause()


def stop_song():
    song_status.set('Stopped')
    mixer.music.stop()


def resume_song():
    song_status.set('Resuming')
    mixer.music.unpause()


root = Tk()
root.title('Music Player')
root.geometry('640x480')
mixer.init()
song_status = StringVar()
song_status.set('choosing')

# ----Playlist----
play_list = Listbox(root, selectmode=SINGLE, bg='olive', fg='white', font='Aerial 15', width=50)
play_list.grid(columnspan=5)

os.chdir(r'F:\songs\suri')
songs = os.listdir()
for s in songs:
    play_list.insert(END, s)


play_button = Button(root, text='PLAY', command=play_song)
play_button.config(font='Aerial 20', bg='DodgerBlue2', fg='white', padx=7, pady=7)
play_button.grid(row=1, column=0)

pause_button = Button(root, text='PAUSE', command=pause_song)
pause_button.config(font='Aerial 20', bg='DodgerBlue2', fg='white', padx=7, pady=7)
pause_button.grid(row=1, column=1)

stop_button = Button(root, text='STOP', command=stop_song)
stop_button.config(font='Aerial 20', bg='DodgerBlue2', fg='white', padx=7, pady=7)
stop_button.grid(row=1, column=2)

resume_button = Button(root, text='RESUME', command=resume_song)
resume_button.config(font='Aerial 20', bg='DodgerBlue2', fg='white', padx=7, pady=7)
resume_button.grid(row=1, column=3)

mainloop()