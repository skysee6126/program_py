from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")
#root.geometry("640x480+300+100") #가로, 세로, x좌표, y좌표

root.resizable(False,False)

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button2") #flexible size
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button4") #fixed size 
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5") #fixed size 
btn5.pack()

photo = PhotoImage(file="photo.png")
btn6 = Button(root, image=photo, width=100, height=80)
btn6.pack()

def btncmd():
  print("Button is pressed!")
btn7 = Button(root, text="Button7", command=btncmd)
btn7.pack()



root.mainloop()