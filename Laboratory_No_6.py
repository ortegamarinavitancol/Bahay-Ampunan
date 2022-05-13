from tkinter import *

window = Tk()
window.title("Average Grade Calculator")
window.geometry("350x200")




lbl1 = Label(window,text="Student's Grade")
lbl1.grid(row = 1,column = 1)

lbl2 = Label(window,text="Prelim Grade:")
lbl2.grid(row=2,column=0)

lbl3 = Label(window,text="Midterm Grade:")
lbl3.grid(row=3,column=0)

prelimentry = Entry(window)
prelimentry.grid(row=2,column=1,padx=4)

midentry = Entry(window)
midentry.grid(row=3, column=1,padx=4)

lbl4 = Label(window, text="Finals Grade: ")
lbl4.grid(row=4,column=0)

finentry = Entry(window)
finentry.grid(row=4, column=1,padx=4)

def Average():
    Avgentry.delete(0,"end")
    number1=int(prelimentry.get())
    number2=int(midentry.get())
    number3=int(finentry.get())
    answer=(number1+number2+number3)/3
    Avgentry.insert(END,str(answer))

btn1=Button(window,text="Calculate!",width=10,command=Average)
btn1.grid(row=5,column=1)

lbl5 = Label(window,text = "Semestral Grade: ")
lbl5.grid(row=6,column = 0)

Avgentry = Entry(window)
Avgentry.grid(row=6, column = 1)



window.mainloop()
