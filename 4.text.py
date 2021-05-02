from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

txt = Text(root, width=30, height=5) #multiple line
txt.pack()

txt.insert(END, "Please write here")

e = Entry(root, width=30) #A line
e.pack()
e.insert(0, "a line")

def btncmd():
  #Output content
  print(txt.get("1.0", END)) #1= first line, 0: column 0
  print(e.get())

  #delete content
  txt.delete("1.0", END)
  e.delete(0, END)

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()