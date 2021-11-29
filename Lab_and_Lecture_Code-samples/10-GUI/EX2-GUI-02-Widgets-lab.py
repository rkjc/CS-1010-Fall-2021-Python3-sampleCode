import tkinter as tk

groot = tk.Tk()
groot.geometry("300x400")

# -----------setting up variables -----------

# Need to use the special tkinter.StrVar() variable for the radiobuttons to store string values
# and to connect the radio buttons together as a group
rdo_store = tk.StringVar()

# sets which button will be selected by default
rdo_store.set('orange cat')

# variables needed for the checkboxes
# need to use my_bool#.set() and my_bool#.get() to
# set and get the value of these variables for the check boxes
my_box_1 = tk.BooleanVar()
my_box_2 = tk.BooleanVar()
my_box_3 = tk.BooleanVar()
my_box_4 = tk.BooleanVar()

#  --------- defining the functions -----------
def doButt():
    temp_var = rdo_store.get()
    lb_1.configure(text=temp_var)
    temp_str = bts(my_box_1.get()) + ' - ' + bts(my_box_2.get()) + ' - ' + bts(my_box_3.get()) + ' - ' + bts(my_box_4.get())
    lb_2.configure(text=temp_str)

# this function takes a boolean True/False and returns a string with the word Yes/No in it
def bts(boolval): #stands for 'Boolean To String'
    if boolval:
        return "Yes"
    else:
        return "No"


# ----------- Making the Widgets -----------
lb_1 = tk.Label(groot, text="radio selection", font=('arial', 12)) # used for radio button output
lb_2 = tk.Label(groot, text="box selection", font=('arial', 12)) # used for check button output
# ----
bt_1 = tk.Button(groot, text="push", command=doButt)
# ----
my_radio_1 = tk.Radiobutton(groot)
my_radio_1.config(text="cat", variable=rdo_store, value="orange cat")

my_radio_2 = tk.Radiobutton(groot)
my_radio_2.config(text="dog", variable=rdo_store, value="black dog")

my_radio_3 = tk.Radiobutton(groot)
my_radio_3.config(text="cow", variable=rdo_store, value="brown cow")

my_radio_4 = tk.Radiobutton(groot)
my_radio_4.config(text="bird", variable=rdo_store, value="blue bird")
# ----
my_checkbutton_1 = tk.Checkbutton(groot, text="Box 1", var=my_box_1)
my_checkbutton_2 = tk.Checkbutton(groot, text="Box 2", var=my_box_2)
my_checkbutton_3 = tk.Checkbutton(groot, text="Box 3", var=my_box_3)
my_checkbutton_4 = tk.Checkbutton(groot, text="Box 4", var=my_box_4)


# -------- Layout the GUI --------------
my_radio_1.pack()
my_radio_2.pack()
my_radio_3.pack()
my_radio_4.pack()

lb_1.pack()
tk.Label(groot, text="---------------------------").pack() # decorative seperating line

my_checkbutton_1.pack()
my_checkbutton_2.pack()
my_checkbutton_3.pack()
my_checkbutton_4.pack()

lb_2.pack()
tk.Label(groot, text="---------------------------").pack() # decorative seperating line

bt_1.pack()

groot.mainloop()