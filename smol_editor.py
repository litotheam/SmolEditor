from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="A very Smol Text Editor").grid(column=0, row=0)
ttk.Button(frm, text="Leave", command=root.destroy).grid(column=1, row=0)
root.mainloop()