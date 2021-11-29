# 05-frame_two_added_to_main_F21.py
import tkinter as tk
mainwindow = tk.Tk()
mainwindow.geometry("300x400")
 
myFrameA = tk.Frame(mainwindow, bg="green")
#myFrameA.pack()
myFrameA.place(x=0, y=0, relwidth=1, relheight=0.5)
 
myFrameB = tk.Frame(mainwindow, bg="cyan")
#myFrameB.pack()
myFrameB.place(x=0, rely=0.5, relwidth=1, relheight=0.5)
 
myButt_1A = tk.Button(myFrameA, bg='orange', text='button one')
myButt_1A.pack()
 
myButt_2A = tk.Button(myFrameA, bg='pink', text='button one')
myButt_2A.pack()
 
myButt_1B = tk.Button(myFrameB, bg='yellow', text='button two')
#myButt_1B.pack()
myButt_1B.grid(row=0, column=0)
 
myButt_2B = tk.Button(myFrameB, bg='blue', text='button two')
#myButt_2B.pack()
myButt_2B.grid(row=0, column=1)
 
mainwindow.mainloop()
