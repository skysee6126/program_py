from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
listbox = Listbox(frame, selectmode="extended", height=10, yscollcommand=scrollbar.set)

for i in range(1, 32):
  listbox.insert(END, str(i))
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()