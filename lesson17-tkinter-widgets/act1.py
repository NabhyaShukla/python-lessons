from tkinter import *
from PIL import Image, ImageTk #image is for finding the image and imagetk is to upload it into the tkinter

window = Tk()
window.title("My first Tkinter image window")
window.geometry('400x400')

img_file = Image.open('img.jpg')
img_file = img_file.resize((320, 360))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

window.mainloop()