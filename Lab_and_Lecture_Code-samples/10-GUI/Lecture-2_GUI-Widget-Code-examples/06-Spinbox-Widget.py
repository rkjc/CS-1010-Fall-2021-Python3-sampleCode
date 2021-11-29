import tkinter as tk

groot = tk.Tk()
groot.config("300x700")

def change_geom():
    twidth = spin_w.get()
    theight = spin_h.get()
    geomStr = str(twidth) + 'x' + str(theight)
    groot.geometry(geomStr)


L1 = tk.Label(groot, text="select width")
L2 = tk.Label(groot, text="select height")

B1 = tk.Button(groot, text="change size", command=change_geom)

spin_w = tk.Spinbox(groot, from_ = 100, to = 500, repeatinterval=40, repeatdelay=40)
spin_h = tk.Spinbox(groot, from_ = 120, to = 500)

L1.pack()
spin_w.pack()
L2.pack()
spin_h.pack()
B1.pack()

groot.mainloop()