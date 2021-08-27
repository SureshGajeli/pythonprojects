from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Video Downloader')
root.config(bg='ghost white')

Label(root, text="YouTube_Video_Downloader", font='Aerial 15', bg='white smoke').pack()

link = StringVar()

Label(root, text='Paste the link here: ', font='Aerial 15 bold').place(x=160, y=60)
link_enter = Entry(root, textvariable=link, width='70').place(x=32, y=90)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution().download()
    print(video)
    Label(root, text='Downloaded', font='Aerial 15 bold').place(x=180, y=120)


Button(root, text='Download', font='Aerial 15 bold', bg='pale violet red', command=downloader, padx=2).place(x=180,
                                                                                                             y=150)

root.mainloop()
