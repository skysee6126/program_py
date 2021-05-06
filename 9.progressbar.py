import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI program")
root.geometry("640x480")

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(5) #update for sc
progressbar.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(5) #update for sc
progressbar2.pack()

def btncmd():
  progressbar.stop()
  progressbar2.stop()

btn = Button(root, text="STOP", command=btncmd)
btn.pack()

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()

def btncmd2():
  for i in range(1, 101):
    time.sleep(0.01)

    p_var3.set(i)
    progressbar3.update()
    print(p_var3.get())

btn = Button(root, text="START", command=btncmd2)
btn.pack()




root.mainloop()