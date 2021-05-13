import os
from tkinter import *
# from tkinter.filedialog import asksaveasfile, askopenfilename

root = Tk()
root.title("Untitied -Windos notepad")
root.geometry("640x480")


filename= "my test.txt"

def open_file():
  if os.path.isfile(filename):
    with open(filename, "r", encoding="utf8") as file:
      txt.delete("1.0", END)
      txt.insert(END, file.read())

  # filename = askopenfilename(parent=root)
  # f = open(filename)
  # f.read()

def save_file():
  with open(filename, "w", encoding="utf8") as file:
      file.write(txt.get("1.0", END))

    # files = [('All Files', '*.*'), 
    #         ('Python Files', '*.py'),
    #         ('Text Document', '*.txt')]
    # file = asksaveasfile(filetypes = files, defaultextension = files)


def creat_new_file():
  print("Create new file")
menu = Menu(root)

#File Menu
menu_file = Menu(menu, tearoff=0)

menu_file.add_separator()
menu_file.add_command(label="Open file...", command=open_file)

menu_file.add_separator()
menu_file.add_command(label="Save all", command=save_file)


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
txt = Text(root, yscrollcommand=scroll.set)
txt.pack(side="left", fill="both", expand=True)

# Configure the scrollbars
scroll.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()