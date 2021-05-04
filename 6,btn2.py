from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

#check box
chkvar = IntVar()
chkbox = Checkbutton(root, text="I will not see this today", variable=chkvar)
chkbox.select()
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="I will not see this for a week", variable=chkvar2)
chkbox2.pack()

#Radio Button
label1 = Label(root, text="choose the food").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()

btn_burger2 = Radiobutton(root, text="Cheseburger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chickenburger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text="choose the drink").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var )
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="sprite", value="sprite", variable=drink_var )

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
  print(chkvar.get()) #0: checked 1:Unchecked
  print(chkvar2.get())

  print(burger_var.get()) #return to selected value
  print(drink_var.get()) #return to selected value

btn = Button(root, text="Click", command=btncmd)
btn.pack()

root.mainloop()