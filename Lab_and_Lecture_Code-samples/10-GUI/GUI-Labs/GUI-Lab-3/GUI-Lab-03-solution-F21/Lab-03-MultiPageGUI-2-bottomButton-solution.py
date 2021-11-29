#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window

import tkinter as tk
from tkinter import scrolledtext

mainwindow = tk.Tk()
mainwindow.title("Multi-window demo code - 3")
mainwindow.geometry("600x500")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(0, weight=1)
#mainwindow.rowconfigure(1, weight=1)

def showRed():
    redFrame.tkraise()

def showGreen():
    greenFrame.tkraise()

def showBlue():
    blueFrame.tkraise()

def showFrame_04():
    frame_04.tkraise()

# Parent widget for the buttons
top_frame = tk.Frame(mainwindow, bg="cyan", highlightbackground="black", highlightthickness=1)

top_frame.grid(row=1, column=0, sticky=(tk.NSEW))

btn_r1 = tk.Button(top_frame, text='red', width='5', command=showRed)
btn_r1.grid(row=0, column=0, padx=(10), pady=10)

btn_g1 = tk.Button(top_frame, text='green', width='5', command=showGreen)
btn_g1.grid(row=0, column=1, padx=(10), pady=10)

btn_b1 = tk.Button(top_frame, text='blue', width='5', command=showBlue)
btn_b1.grid(row=0, column=2, padx=(10), pady=10)

btn_frame_04 = tk.Button(top_frame, text='Frame 04', width='8', command=showFrame_04)
btn_frame_04.grid(row=0, column=3, padx=(10), pady=10)

# bottom Frame ----------------------------------------------------
bottom_frame = tk.Frame(mainwindow, bg="yellow", padx=5, pady=5)
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(1, weight=1)

# -------- red Frame 1 ----------------------------------------------------
redFrame = tk.Frame(bottom_frame, bg="red", padx=5, pady=5)
redFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# redLabel_1 = tk.Label(redFrame, text="this is the Red Frame")
# redLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def func_one():
    str_var1 = E1.get()
    if str_var1 == 'blue':
        redFrame.config(bg='blue')
    if str_var1 == 'red':
        redFrame.config(bg='red')
    if str_var1 == '':
        str_var1="Empty-reset"
        redFrame.config(bg='gray95')
    L2.configure(text=str_var1)

L1 = tk.Label(redFrame, text = "Enter string or color")
L1.pack()

E1 = tk.Entry(redFrame)
E1.pack()

B1 = tk.Button(redFrame, text="post the entry", command=func_one)
B1.pack()

L2 = tk.Label(redFrame, text = "---------------")
L2.pack()

# btn_b2 = tk.Button(redFrame, fg="blue", text='blue', width='5', command=showBlue)
# btn_b2.place(x=0, y=0)

btn_g2 = tk.Button(redFrame, fg="green", text='02 ->', width='5', command=showGreen)
btn_g2.place(relx=1.0, y=0, anchor=(tk.NE))


# green Frame 2 ----------------------------------------------------
greenFrame = tk.Frame(bottom_frame, bg="green", padx=5, pady=5)
greenFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# greenLabel_1 = tk.Label(greenFrame, text="this is the Green Frame")
# greenLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

butt1 = False
butt2 = False

def func_one_frm2():
    label_1.configure(text="you pushed the button 1")
    global butt1
    butt1 = True


def func_two_frm2():
    other_label.configure(text="that was button 2")
    other_label.configure(foreground="blue", background="yellow")
    global butt2
    butt2 = True


def do_reset_frm2():
    global butt1
    global butt2
    if (butt1 == True and butt2 == True):
        label_1.configure(text="I'm reset")
        other_label.configure(text="Also reset")
        butt1 = False
        butt2 = False


label_1 = tk.Label(greenFrame, text="A Label")
label_1.pack()

other_label = tk.Label(greenFrame, text="Label B - other")
other_label.pack()

button_1 = tk.Button(greenFrame, text="Button ONE", command=func_one_frm2)
button_1.pack()

two_button = tk.Button(greenFrame, text="Button TWO", command=func_two_frm2)
two_button.pack()

resetButt = tk.Button(greenFrame, text="do the reset", command=do_reset_frm2)
resetButt.pack()

btn_r3 = tk.Button(greenFrame, fg="red", text='<- 01', width='5', command=showRed)
btn_r3.place(x=0, y=0)

btn_b3 = tk.Button(greenFrame, fg="blue", text='03 ->', width='5', command=showBlue)
btn_b3.place(relx=1.0, y=0, anchor=(tk.NE))



# ----  blue Frame 3 ----------------------------------------------------
blueFrame = tk.Frame(bottom_frame, bg="blue", padx=5, pady=5)
blueFrame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# blueLabel_1 = tk.Label(blueFrame, text="this is the Blue Frame")
# blueLabel_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

my_tkVar = tk.IntVar()

# sets which button will be selected by default
my_tkVar.set(2)


def doButt_frm3():
    temp_var = my_tkVar.get()
    L1_frm3.configure(text=temp_var)

L1_frm3 = tk.Label(blueFrame, text="selection", font=('arial', 20))
L1_frm3.pack()

my_radio_1 = tk.Radiobutton(blueFrame)
my_radio_1.config(text="Radiobutton 1", variable=my_tkVar, value=1)

my_radio_2 = tk.Radiobutton(blueFrame)
my_radio_2.config(text="Radiobutton 2", variable=my_tkVar, value=2)

my_radio_3 = tk.Radiobutton(blueFrame)
my_radio_3.config(text="Radiobutton 3", variable=my_tkVar, value=3)

my_radio_1.pack()
my_radio_2.pack()
my_radio_3.pack()

L2_frm3 = tk.Label(blueFrame, text="---------------------------")
L2_frm3.pack()

B1_frm3 = tk.Button(blueFrame, text="push", command=doButt_frm3)
B1_frm3.pack()

btn_g4 = tk.Button(blueFrame, fg="green", text='<- 02', width='8', command=showGreen)
btn_g4.place(x=0, y=0)

btn_r4 = tk.Button(blueFrame, fg="magenta", text='04 ->', width='5', command=showFrame_04)
btn_r4.place(relx=1.0, y=0, anchor=(tk.NE))

# ------ Frame 4 ----------------------------------------------------
frame_04 = tk.Frame(bottom_frame, bg="magenta", padx=5, pady=5)
frame_04.place(x=0, y=0, relwidth=1.0, relheight=1.0)

# frame_04_Label_1 = tk.Label(frame_04, text="this is Frame_04")
# frame_04_Label_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def doButton1():
    #label_1.config(image=img01_size_2)
    label_1.config(image=img01)
    label_2.config(text="Image One")

def doButton2():
    label_1.config(image=img02)
    label_2.config(text="Image Two")

def doButton3():
    label_1.config(image=img03)
    label_2.config(text="Image Three")

#images have to be .png, .jpg does not work.
img01 = tk.PhotoImage(file="Space_Woman_500.png")
img01_thumb = img01.subsample(4)

img02 = tk.PhotoImage(file="vigo_500.png")
img02_thumb = img02.subsample(4)

img03 = tk.PhotoImage(file="Enterprise_500.png")
img03_thumb = img03.subsample(4)

label_1 = tk.Label(frame_04, text="images")
label_1.grid(row=1, rowspan=3, column=1)

label_2 = tk.Label(frame_04, text="select an image")
label_2.grid(row=0, column=1)

MyButton1 = tk.Button(frame_04, image=img01_thumb, text="b1", bg="blue", width=100, height=100, command = lambda: doButton1())
MyButton1.grid(row=1, column=0)

MyButton1 = tk.Button(frame_04, image=img02_thumb, text="b2", bg="blue",width=100, height=100, command = lambda: doButton2())
MyButton1.grid(row=2, column=0)

MyButton1 = tk.Button(frame_04, image=img03_thumb, text="b3", bg="blue",width=100, height=100, command = lambda: doButton3())
MyButton1.grid(row=3, column=0)

btn_b4 = tk.Button(frame_04, fg="blue", text='<- 03', width='5', command=showBlue)
btn_b4.place(x=0, y=0)

mainwindow.mainloop()
