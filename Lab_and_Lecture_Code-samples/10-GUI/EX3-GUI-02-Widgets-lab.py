import tkinter as tk

my_window = tk.Tk(className='Color Changer')
my_window.minsize(300, 250)

# Define all the Functions
def setColor():
    picked = listbox_1.curselection()
    temp_text = listbox_1.get(picked)
    lb_1.configure(text=temp_text)
    my_window.config(bg=temp_text)

# Make all the Widgets
listbox_1 = tk.Listbox(my_window, selectmode=tk.SINGLE, height="6")
listbox_1.insert(tk.END, 'red')
listbox_1.insert(tk.END, 'blue')
listbox_1.insert(tk.END, 'green')
listbox_1.insert(tk.END, 'orange')
listbox_1.insert(tk.END, 'cyan')
listbox_1.insert(tk.END, 'gray')
listbox_1.select_set(0)

bt_1 = tk.Button(my_window, text='Set Color', command=setColor)

lb_1 = tk.Label(my_window, text='your selection')

# Layout the GUI
listbox_1.pack()
bt_1.pack()
lb_1.pack()

my_window.mainloop()