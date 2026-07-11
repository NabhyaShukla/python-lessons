from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg="#001B1A")
root.geometry('650x400')

#Adding Img and labels to main wnodow
upload = Image.open("img.jpg")
#Resize the image - resize()
upload = upload.resize((470, 690))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="#002811")
label.place(x=100, y=20)

label1 = Label(root, text="Yello User! Welcome To Your Personal Denomination Counter", bg="#19001F")
label.place(relx=0.5, y=340, anchor=CENTER)

#Func to display a messagebox and proceed if OK is cclicked
def msg():
    MsgBox = messagebox.showinfo("ALERT", "Do you really want to calculate the Denomination Count?")
    if MsgBox == 'ok':
        topwin()

# Adding Btns to main window
Button1 = Button(root, text="Let's get SATRTED!", command=msg, bg="#C2FC95", fg="black")
Button1.place(x=260, y=360)

#Function for opening new\top WINDOWWWW
def topwin():
    top = Toplevel()
    top.title("Denomination Calc.")
    top.configure(bg="#495759")
    top.geometry('600x350+50+50')

    label = Label(top, text="Enter TOTAL amount", bg="#4B6265")
    entry = Entry(top)
    lbl = Label(top, text="Here are NUMBER OF NOTES for each denomination", bg='#495759')

    l1 = Label(top, text="$2000", bg='#4B6265')
    l2 = Label(top, text="$500", bg='#4B6265')
    l3 = Label(top, text="$100", bg='#4B6265')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("ERROR", "Please enter A VALID NUMBER.")

    btn = Button(top, text='Calculator', command=calculator, bg="#310101", fg='white')

    #Centering widgets in the top window
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=100, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()