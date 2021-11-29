import tkinter as tk
groot = tk.Tk()
groot.geometry("200x200")

# Need to use the special tkinter.IntVar() variable
# to connect the radio buttons together as a group
myIntThing = tk.StringVar()

# sets which button will be selected by default
myIntThing.set( "A" )


def doButt():
    temp_var = myIntThing.get()
    L1.configure(text=temp_var)

L1 = tk.Label(groot, text="selection", font=('arial', 20))
L1.pack()

my_radio_1 = tk.Radiobutton(groot)
my_radio_1.config(text="Radiobutton 1", variable=myIntThing, value="A")

my_radio_2 = tk.Radiobutton(groot)
my_radio_2.config(text="Radiobutton 2", variable=myIntThing, value="B")

my_radio_3 = tk.Radiobutton(groot)
my_radio_3.config(text="Radiobutton 3", variable=myIntThing, value="Z")


my_radio_1.pack()
my_radio_2.pack()
my_radio_3.pack()

L2 = tk.Label(groot, text="---------------------------")
L2.pack()

B1 = tk.Button(groot, text="push", command=doButt)
B1.pack()

groot.mainloop()