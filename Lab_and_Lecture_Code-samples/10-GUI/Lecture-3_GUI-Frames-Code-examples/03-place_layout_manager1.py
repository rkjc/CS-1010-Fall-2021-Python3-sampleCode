 
import tkinter as tk
 
app = tk.Tk()
app.geometry('300x300')
 
#tkraise()

labelA = tk.Label(app, text = "Label (0, 0)", fg="blue", bg="#FF0") #color using Hex values
labelB = tk.Label(app, text = "Label (20, 20)", fg="green", bg="#300")
labelC = tk.Label(app, text = "Label (40, 50)", fg="black", bg="#f03")
labelD = tk.Label(app, text = "Label (0.5, 0.5)", fg="orange", bg="#0ff")
 
labelE = tk.Label(app, text = "Label xrel",  bg="pink")
labelF = tk.Label(app, text = "Label relheight=0.8",  bg="green")


labelA.place(x=0, y=0)
labelB.place(x=20, y=20)
labelA.tkraise()

labelC.place(x=40, y=50)

labelE.place(x=200, relheight=0.8)
labelF.place(rely=0.9, relx=0.5, relwidth=0.7, anchor=tk.CENTER)
#labelF.place(rely=0.9, relx=0.5, relwidth=0.7, anchor=tk.CENTER)
labelD.place(relx=0.5, rely=0.5)
labelD.tkraise()

app.mainloop()
