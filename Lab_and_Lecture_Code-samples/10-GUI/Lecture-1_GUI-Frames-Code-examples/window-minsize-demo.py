 
import tkinter as tk

groot = tk.Tk()

# using the method .minsize() so the window can still auto expand
groot.minsize(200,100)


def do_one():
    label_1.config(text='made this message really long to demonstrate window resizing')

def do_two():
    label_1.config(text='small again')


label_1 = tk.Label(groot, text="started")
label_1.pack()

button_1 = tk.Button(groot, text="make long", command=do_one)
button_1.pack()

button_2 = tk.Button(groot, text="make small", command=do_two)
button_2.pack()

groot.mainloop()
