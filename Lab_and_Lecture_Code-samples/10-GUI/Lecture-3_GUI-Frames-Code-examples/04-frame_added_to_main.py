# 04-frame_added_to_main_F21.py
import tkinter as tk
mainwindow = tk.Tk()
mainwindow.config(bg='orange')
mainwindow.geometry("300x400")
 
myFrameBob = tk.Frame(mainwindow, bg="green")
myFrameBob.pack()
#myFrameBob.place(x=10, y=5, relwidth=0.9, relheight=0.9) #made smaller than window to see it
 
# myButt1 = tk.Button(myFrameBob, bg='orange', text='button one')
# myButt1.pack()
 
mainwindow.mainloop()
