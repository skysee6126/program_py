from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="I will not see this today", variable=chkvar)
chkbox.select()
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="I will not see this for a week", variable=chkvar2)
chkbox2.pack()




def btncmd():
  print(chkvar.get()) #0: checked 1:Unchecked
  print(chkvar2.get())

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()