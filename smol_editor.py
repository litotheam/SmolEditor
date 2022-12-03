from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

class SmolEditor():
    def __init__(self):
        self.root = Tk()
        self.root.title("Smol Editor")
        self.root.geometry("800x600")

        self.frame = ttk.Frame(
            self.root, 
            height=300, 
            width=400, 
            relief="sunken")
        self.frame.grid(
            padx=10, pady=10)

        self.text = scrolledtext.ScrolledText(self.frame)
        self.text.grid(row=1, column=0, padx=10, pady=10)

        self.save_button = ttk.Button(self.frame, text="Save As", command=self.save_as)
        self.save_button.grid(row=0, column=0)

        self.open_button = ttk.Button(self.frame, text="Open", command=self.open_file)
        self.open_button.grid(row=0, column=1)

    
    def save_as(self):
        content = self.text.get("1.0", END)
        with open("sample.txt", "w") as f:
            f.write(content)

    def open_file(self): 
        with open("sample.txt", "r") as f:
            content = f.read()
            self.text.insert(1.0, content)



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

