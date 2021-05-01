from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

label1 = Label(root, text="Hello, world")
label1.pack()

photo = PhotoImage(file="photo.png")
label2= Label(root, image=photo)
label2.pack()

def change():
  label1.config(text="See you again")

  global photo2 #전역변수 설정필요
  photo2 = PhotoImage(file="photo2.png")
  label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()