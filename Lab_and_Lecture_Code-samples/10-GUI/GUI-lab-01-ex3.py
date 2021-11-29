 
import tkinter
import random

def button_1_func():
    label_1.configure(text="first button has been pushed")

def button_2_func():
    label_1.configure(text="here is a random number")
    label_2.configure(text=str(random.randint(1,100)))
    label_2.configure(foreground="blue", background="yellow")




bob = tkinter.Tk()
bob.geometry("300x250")

label_1 = tkinter.Label(bob, text="A Label")
label_1.pack()

label_2 = tkinter.Label(bob, font = ('Comic Sans MS',20), bg="green", fg='orange', text="Label B - other")
label_2.pack()

button_1 = tkinter.Button(bob, text="Button ONE", command=button_1_func)
button_1.pack()

two_button = tkinter.Button(bob, height = 3, width = 20, text="Button TWO", command=button_2_func)
two_button.pack()


bob.mainloop()
