from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title('My photo gallery')
window.geometry('400x370')

title = Label(window, text='My Photo Gallery', fg='white', bg='blue', width=40)
title.pack(pady=10)
img_file = Image.open('img.jpg')
img_file = img_file.resize((300, 200))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

def show_message():
    messagebox.showinfo('Great!', 'You clicked the Photo!!!')
msg_btn = Button(window, text='Click to React', bg='lightblue', fg='black', command=show_message)
msg_btn.pack(pady=5)

def show_details():
    top = Toplevel()
    top.title('Photo Details')
    top.geometry('250x140')
    info = Label(top, text='Taken on: #/#/2021 (PRIVATE)')
    info.pack(pady=10)
    Place = Label(top, text='Location: *PRIVATE!**CANT BE LEAKED*')
    Place.pack()
    top.mainloop()
details_btn = Button(window, text='See Details', bg='#FF8C00', fg='#020617', command=show_details)
details_btn.pack(pady=5)

window.mainloop()