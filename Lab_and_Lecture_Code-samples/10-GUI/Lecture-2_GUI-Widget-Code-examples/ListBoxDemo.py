import tkinter as tk

window_main = tk.Tk(className='Tkinter - TutorialKart')
window_main.minsize(300, 250)

def submitFunction():
    selection = listbox_1.curselection()
    temp_text = 'selection index= ' + str(selection[0]) + " \ selected item= " + listbox_1.get(selection)
    L1.configure(text=temp_text)

listbox_1 = tk.Listbox(window_main, selectmode=tk.SINGLE, height="6")
listbox_1.insert(1, 'Apple')
listbox_1.insert(2, 'Banana')
listbox_1.insert(3, 'Cherry')
listbox_1.insert(4, 'Mango')
listbox_1.insert(5, 'Orange')
listbox_1.pack()
listbox_1.select_set(0)


B1 = tk.Button(window_main, text='Submit', command=submitFunction)
B1.pack()

L1 = tk.Label(window_main, text='your selection')
L1.pack()

window_main.mainloop()