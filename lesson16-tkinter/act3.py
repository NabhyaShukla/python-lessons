from tkinter import *

window = Tk()
window.title("My profile Crad")
window.geometry('400x380')

# ===== Part 2 - Add a title  label at the top using grid =====

title = Label(window, text='My profile Card', fg='white', bg='darkgreen', width='50', borderwidth=5)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# ===== Part 3 - Add name and Hobby Labels and Entry Boxes =====

name_label = Label(window, text='Name:  ', fg='white', bg='black')
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg="#011800", bg="#D9FF8C", width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)

hobby_label = Label(window, text='Hobby:    ', fg='white', bg='black')
hobby_label.grid(row=2, column=0, padx=10, pady=5)

hobby_entry = Entry(window, fg='#011800', bg='#D9FF8C', width=25)
hobby_entry.grid(row=2, column=1, padx=10, pady=5)

# ===== Part 4 - Add a frame with an 'About Me' text box inside =====

about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text='Profile Card (OutPut)')
about_label.pack()

about_text = Text(about_frame, fg='#6B3B48', bg='#FBF2F4', width=40, height=4)
about_text.pack()

# ALWAYS PUT THE METJOD OF BUTTON ABOVE THE BUTTON / BEFOR EIT

def display():
    name_value = name_entry.get()
    hobby_value = hobby_entry.get()
    about_text.delete("1.0", END)
    about_text.insert(END, f"Name: {name_value},\nHobby: {hobby_value}")

# ===== Part 5 - Add a submit button and run the window =====

submit = Button(window, text='Show My Card', bg='#8E4A56', fg='#FBF2F4', activebackground='#763D47', width=20, command=display)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()