import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

values = [str(i)+"day" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("pay day")

readyOnly_combobox = ttk.Combobox(root, height=5, values=values,state="readonly")
readyOnly_combobox.current(0)
readyOnly_combobox.pack()


def btncmd():
  print(combobox.get())

btn = Button(root, text="Select", command=btncmd)
btn.pack()

root.mainloop()