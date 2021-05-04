from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) #selectmode = "single", height= "지정된 숫자만큼만 보여줌"
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Wathermelon")
listbox.insert(END, "Grape")
listbox.pack()

def btncmd():
  #Delete
  listbox.delete(END) #lastlist
  listbox.delete(0) #firstlist

  #count
  print(listbox.size())

  print("print from frist to third:", listbox.get(0,2))

  #check the seleted list (Return index)
  print("selected one:", listbox.curselection())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()