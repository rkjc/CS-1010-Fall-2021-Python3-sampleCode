import tkinter
import random

def doButton():
    rnum = random.randint(0,100)
    tempstring =  "your random number is " + str(rnum)
    label_1.configure(text = tempstring)


bob = tkinter.Tk()
bob.geometry('300x200')

label_1 = tkinter.Label(bob, text="A longer Label text")
label_1.configure(bg="cyan")
label_1.config()
label_1.pack()

button_1 = tkinter.Button(bob, text="A Button", command=doButton)

button_1.configure(bg='green', highlightbackground="green", activebackground='yellow')
button_1.pack()

bob.mainloop()
