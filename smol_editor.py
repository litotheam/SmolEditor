from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class SmolEditor():
    def __init__(self):
        self.root = Tk()
        self.root.title("Smol Editor")
        self.root.geometry("800x600")

        self.frame = ttk.Frame(self.root)
        self.frame.grid()


# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()

# text_editor = Text(frm)
# text_editor.grid(row=1, column=0)

# scrolled_text = scrolledtext.ScrolledText(frm)
# scrolled_text.grid(row=2, column=0)

# ttk.Label(frm, text="A very Smol Text Editor").grid(row=0, column=0)
# ttk.Button(frm, text="Leave", command=root.destroy).grid(row=0, column=1)
# root.mainloop()

def main():
    editor = SmolEditor()
    editor.root.mainloop()

if __name__ == "__main__": 
    main()

