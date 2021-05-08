import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

def info():
  msgbox.showinfo("Alert", "Sussessfully completed to book")

def warn():
  msgbox.showwarning("Warnning", "Sold out")

def error():
  msgbox.showerror("Error", "There is something wrong")

def okcancel():
  msgbox.askokcancel("Confirm/ cancel", "Are you sure to book this?")

def retrycancel():
  msgbox.askretrycancel("Retry/ cancel", "Do you want to retry?")
  response = msgbox.askyesnocancel(title=None, message="Do you want to exit after the save?")
  print(response)
  if response == 1:
    print("Yes")
  elif response == 0:
    print("No")
  else:
    print("Cancel")
      
def yesno():
  msgbox.askyesno("Yes/ no/ cancel", "Do you want to retry?")

def yesnocancel():
  response = msgbox.askyesnocancel(title=None, message="Do you want to exit after the save?")
  print(response)
  if response == 1:
    print("Yes")
  elif response == 0:
    print("No")
  else:
    print("Cancel")

Button(root, command=info, text="Alert").pack()
Button(root, command=warn, text="Warnning").pack()
Button(root, command=error, text="Error").pack()

Button(root, command=okcancel, text="Confirm/ cancel").pack()
Button(root, command=retrycancel, text="Retry/ cancel").pack()
Button(root, command=yesno, text="Yes/ no").pack()
Button(root, command=yesnocancel, text="Yes/ no/ cancel").pack()

root.mainloop()