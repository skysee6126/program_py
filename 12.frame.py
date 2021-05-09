import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

Label(root, text="Please choose menu").pack(side="top")
Button(root, text="Order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="cheeseburger").pack()
Button(frame_burger, text="Chickenburger").pack()

frame_drink = LabelFrame(root,text="drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()

root.mainloop()