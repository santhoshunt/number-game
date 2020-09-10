from tkinter import *
from tkinter import messagebox
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
    global rand
    if rand==int(ent1.get()):
        lab2.config(text="You're RIGHT !!",font=("bold",16))
        frame1.config(bg="green")
        lab1.config(bg="green")
        lab2.config(bg="green")
        s=messagebox.askyesno("You're Right as always !!","Do you want to win again?")
        if not s:
            exit()
        else:
            frame1.config(bg="blue")
            lab1.config(bg="blue")
            lab2.config(bg="blue")
            lab2.config(text="You can do it again!")
            rand=randint(1,101)
            print(rand)
    elif rand>int(ent1.get()):
        lab2.config(text="guess higher!")
    else:
        lab2.config(text="Guess lower!")
    ent1.delete(0,END)
    
lab1=Label(frame1,text="Guess a number between 1-100",bg="blue",font=("bold",16))
ent1=Entry(frame1,borderwidth=7)
but1=Button(frame1,text="Check",command=check,bg="light blue")
lab2=Label(frame1,text="Guess a number!",bg="blue",font=("bold",16))

lab1.grid(padx=10,pady=10)
ent1.grid(padx=10,pady=10)
but1.grid(padx=10,pady=10)
lab2.grid(padx=10,pady=10)

window.mainloop()