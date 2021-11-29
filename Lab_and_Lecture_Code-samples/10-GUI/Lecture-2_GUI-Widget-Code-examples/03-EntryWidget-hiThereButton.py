import tkinter as tk

groot = tk.Tk()
groot.geometry("300x200")
groot.configure(background="cyan")

def func_one():
    strVar1 = E1.get()
    strVar2 = "Hi there " + strVar1
    L2.configure(text=strVar2)

def doClear():
    tempstr = E1.get()
    size = len(tempstr)
    E1.delete(0,size)
    #E1.insert(1, " ")

def doDel():
    tempstr = E1.get()
    size = len(tempstr)
    E1.delete(size-1)


L1 = tk.Label(groot, text = "Enter User Name")
L2 = tk.Label(groot, text = "---------------")

E1 = tk.Entry(groot) #<-----
E1.insert(0, "0123456789")

B1 = tk.Button(groot, text="post the entry", command=func_one)
buttClear = tk.Button(groot, text="Clear", command=doClear)
backButt = tk.Button(groot, text="del", command=doDel)

L1.pack()
E1.pack()
L2.pack()
B1.pack()
buttClear.pack()
backButt.pack()

groot.mainloop()