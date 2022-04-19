#Label Window
from tkinter import *
window = Tk()

window.title("Label")
window.geometry("350x100")

label = Label(window,text="Laboratory Activity 5")
label.place(x=110, y=30)

label2 = Label(window,text="Submitted to: Mam Sayo")
label2.place(x=100,y=50)

window.mainloop()


#Text Field Window
from tkinter import *

window = Tk()

window.title("Text Field")
window.geometry("350x150")

txtfld = Entry(window,bd=1, font=("Arial",11))
txtfld.place(x=75,y=40,width=200,height=75)


window.mainloop()


#Father of Computer Window
from tkinter import *
import tkinter.font as font

window = Tk()


window.title("Father of computer")
window.geometry("700x500")

label = Label(window, text="Charles Babbage", bg = "#09ebee",fg = "black", font= "Arial 50")
label.place(x=100, y=200)

window.mainloop()


#Major Subjects Window
from tkinter import *

window = Tk()

window.title("Major Subjects")
window.geometry("350x150")


Lb1 = Listbox(window, width=25, height=6)
Lb1.insert(1, "reading")
Lb1.insert(2, "writing")
Lb1.insert(3, "arithmetic")
Lb1.insert(4, "coding")


Lb1.pack()
window.mainloop()


#Button Window
from tkinter import *

class MyButton:
    def __init__(self,window):
        self.btn1 = Button(window, text='Color', fg="Red", bg='Blue')
        self.btn1.place(x=50, y=100)
        self.btn2 = Button(window,text='<---Click to change the color of the button',command=self.colorChange)
        self.btn2.place(x=100, y=100)

    def colorChange(self):
        self.btn1.configure(bg="Yellow")

window = Tk()
mywin = MyButton(window)
window.title("Button")
window.geometry("350x150")
window.mainloop()
