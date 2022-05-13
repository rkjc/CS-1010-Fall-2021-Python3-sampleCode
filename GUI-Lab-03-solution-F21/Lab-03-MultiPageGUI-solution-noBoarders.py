#https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window
import tkinter as tk
from tkinter import scrolledtext

mainwindow = tk.Tk()
mainwindow.title("Multi-window demo code - 3")
mainwindow.geometry("600x500")

mainwindow.columnconfigure(0, weight=1)
mainwindow.rowconfigure(1, weight=1)

def showFrameOne():
    frameOne.tkraise()

def showFrameTwo():
    frameTwo.tkraise()



# Parent widget for the buttons
top_frame = tk.Frame(mainwindow, bg="cyan", highlightbackground="black", highlightthickness=1)

top_frame.grid(row=0, column=0, columnspan=3, sticky=tk.N+tk.W+tk.E)

btn_openOne = tk.Button(top_frame, text='red', width='5', command=showFrameOne)
btn_openOne.grid(row=0, column=0, padx=(10), pady=10)

btn_openTwo = tk.Button(top_frame, text='green', width='5', command=showFrameTwo)
btn_openTwo.grid(row=0, column=1, padx=(10), pady=10)



# bottom Frame ----------------------------------------------------
bottom_frame = tk.Frame(mainwindow, bg="yellow")
bottom_frame.grid_propagate(False)
bottom_frame.grid(row=1, column=0, sticky=(tk.NSEW))

bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

# -------- red Frame 1 ----------------------------------------------------
frameOne = tk.Frame(bottom_frame, bg="red")
frameOne.place(x=0, y=0, relwidth=1.0, relheight=1.0)


btn_openTwo_2 = tk.Button(frameOne, text='Open page two', command=showFrameTwo)
btn_openTwo_2.pack()


# green Frame 2 ----------------------------------------------------
frameTwo = tk.Frame(bottom_frame, bg="green")
frameTwo.place(x=0, y=0, relwidth=1.0, relheight=1.0)


btn_openOne_2 = tk.Button(frameTwo, text='Return', width='5', command=showFrameOne)
btn_openOne_2.pack()

#---------------------------------------------------------------------------------




frameOne.tkraise()
mainwindow.mainloop()
