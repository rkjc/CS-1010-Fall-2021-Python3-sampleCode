import tkinter

groot = tkinter.Tk()

groot.geometry('450x200')
groot.configure(bg="orange")
groot.title("CS1010 - GUI")

myWidget = tkinter.Label(groot, text="welcome to GUI programming")
myWidget.pack()

groot.mainloop()