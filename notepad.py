from tkinter import *
from tkinter.filedialog import asksaveasfile

root = Tk()
root.title("Untitied -Windos notepad")
root.geometry("640x480")

def creat_new_file():
  print("Create new file")
menu = Menu(root)

#File Menu
menu_file = Menu(menu, tearoff=0)

menu_file.add_separator()
menu_file.add_command(label="Open file...")


def save():
    files = [('All Files', '*.*'), 
            ('Python Files', '*.py'),
            ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

menu_file.add_separator()
menu_file.add_command(label="Save all", command=lambda:save())


menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

#Edit
menu.add_cascade(label="Edit")
menu.add_cascade(label="Format")
menu.add_cascade(label="View")
menu.add_cascade(label="Help")


# Vertical (y) Scroll Bar
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

# Text Widget
eula = Text(root, wrap=NONE, yscrollcommand=scroll.set)
eula.pack(side="left", fill=Y)

# Configure the scrollbars
scroll.config(command=eula.yview)
root.config(menu=menu)
root.mainloop()