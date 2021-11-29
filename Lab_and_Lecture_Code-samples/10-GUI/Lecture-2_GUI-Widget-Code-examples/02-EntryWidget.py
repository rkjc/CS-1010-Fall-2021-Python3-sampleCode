import tkinter as tk

groot = tk.Tk()
groot.geometry("300x100")

L1 = tk.Label(groot, text = "Enter User Name")
L1.pack()

E1 = tk.Entry(groot)
E1.pack()

groot.mainloop()