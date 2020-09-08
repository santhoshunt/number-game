from tkinter import *
from random import *

window=Tk()
window.config(bg="blue")
#frame1
frame1=Frame(window)
frame1.pack()
frame1.config(bg="blue")
#random number
rand=randint(1,101)
print(rand)
def check():
    if rand==int(ent1.get()):
        lab2.config(text="You're RIGHT !!")
        frame1.config(bg="green")
        lab1.config(bg="green")
        lab2.config(bg="green")
    elif rand>int(ent1.get()):
        lab2.config(text="guess higher!")
    else:
        lab2.config(text="Guess lower!")
    ent1.delete(0,END)
    
lab1=Label(frame1,text="Guess a number between 1-100",bg="blue")
ent1=Entry(frame1)
but1=Button(frame1,text="Check",command=check)
lab2=Label(frame1,text="Guess a number!",bg="blue")

lab1.grid()
ent1.grid()
but1.grid()
lab2.grid()

window.mainloop()