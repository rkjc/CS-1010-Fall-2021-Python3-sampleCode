# Listbox widget example
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x400')

# ---- functions ------
def print_selection():
    value = myListBox.get(myListBox.curselection())
    outputLabel.config(text=value)

# ---- variables ----
var1 = tk.StringVar()

# ---- widgets ----
outputLabel = tk.Label(window, text="output here")
outputLabel.pack()

b1 = tk.Button(window, text='print selection', command=print_selection)
b1.pack()

# make listbox widget
myListBox = tk.Listbox(window, listvariable=var1)

# put items into listbox widget
list_items = ['first', 'second', 'third', 'orange', 'apple']
for item in list_items:
    myListBox.insert('end', item)
# choose the default selection
myListBox.select_set(0)
myListBox.pack()


window.mainloop()
