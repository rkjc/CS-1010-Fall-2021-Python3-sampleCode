#import tkinter as tk
from tkinter import *

window = Tk()
window.geometry("300x300")

myLabel = Label(window, text="wow a Label - that is wider")
myLabel.configure(background="orange")

myLabel.pack( expand=True)

window.mainloop()