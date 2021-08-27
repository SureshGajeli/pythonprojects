from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator

root = Tk()     # initialized tkinter which means window created
root.geometry('1080x400')   # set width and height of the window
root.resizable(0, 0)        # root is the name which we refer to our window
root.title('Python - Language_Translator')
root.config(bg='sky blue')

Label(root, text='Language_Translator', font='Aerial 15 bold', bg='grey').pack()
Label(root, text='Enter_Text', font='Aerial 13 bold', bg='pale violet red').place(x=200, y=60)
Input_text = Text(root, font='Aerial 12', height=12, wrap=WORD, padx=5, pady=5, width=55)
Input_text.place(x=20, y=100)
# Text() widget is used for multiple text lines
# padx puts an extra bit of space to the left and right of the widget
# pady adds an extra bit of space to the top and bottom
# wrap=WORD will stop the line after the word that will fit
Label(root, text='Output', font='Aerial 13 bold', bg='pale violet red').place(x=780, y=60)
Output_text = Text(root, font='Aerial 12', height=12, wrap=WORD, padx=5, pady=5, width=55)
Output_text.place(x=550, y=100)

language = list(LANGUAGES.values())

select_in_lang = ttk.Combobox(root, values=language, width=22)
select_in_lang.place(x=20, y=60)
select_in_lang.set('Choose Input Language')
# ttk.Combobox() is a class of ttk modules. It is a drop-down list which will hold multiple values.
# Combobox is used to select one option from many options.
select_op_lang = ttk.Combobox(root, values=language, width=22)
select_op_lang.place(x=890, y=60)
select_op_lang.set('Choose Output Language')


def translator():
    translator_ = Translator()
    translated = translator_.translate(text=Input_text.get(1.0, END), src=select_in_lang.get(),
                                       dest=select_op_lang.get())
    # 1.0 means the input should be read from zero characters to line one.
    # END means to read the text until the end is reached.
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)    # this will insert translated text in output text.


translator_button = Button(root, text='Translate', font='Aerial 12 bold', pady=5, command=translator, bg='royal blue1',
                           activebackground='sky blue')
translator_button.place(x=490, y=340)

mainloop()