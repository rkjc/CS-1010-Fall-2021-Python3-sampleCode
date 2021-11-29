import tkinter

def doBut1():
    label_1.configure(text = "pressed ONE")
    resetBut.configure(bg="red")
    
def doBut2():
    label_1.configure(text = "pressed TWO")
    resetBut.configure(bg="red")

def doBut3():
    label_1.configure(text = "pressed THREE")
    resetBut.configure(bg="red")

def doBut4():
    label_1.configure(text = "pressed FOUR")
    resetBut.configure(bg="red")

def reset():
    label_1.configure(text = "reset")
    resetBut.configure(bg="green")


bob = tkinter.Tk()
#bob.geometry("300x200")

label_1 = tkinter.Label(bob, text="label 1")
label_1.grid(row=0, column=0, columnspan=2)

resetBut = tkinter.Button(bob, text="reset", bg="yellow", height="3", width="8", command=reset)
resetBut.grid(row=1, column=4, rowspan=2)



but1 = tkinter.Button(bob, text="ONE", command=doBut1, width=10)
but1.grid(row=1, column=0)

but2 = tkinter.Button(bob, text="TWO", command=doBut2, width=10)
but2.grid(row=1, column=1)

but3 = tkinter.Button(bob, text="THREE", command=doBut3, width=10)
but3.grid(row=2, column=0)

but4 = tkinter.Button(bob, text="FOUR", command=doBut4, width=10)
but4.grid(row=2, column=1)
          
                    
bob.mainloop()
