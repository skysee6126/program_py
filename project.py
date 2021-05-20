import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("GUI program")

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

def merge_image():
  #print(list_file.get(0,END))
  images = [Image.open(x) for x in list_file.get(0,END)]
  widths = [x.size[0] for x in images]
  heights = [x.size[1] for x in images]

  max_width, total_height = max(widths), sum(heights)
  result_img = Image.new("RGB", (max_width, total_height), (255,255,255))
  y_offset = 0
  # for img in images:
  #   result_img.paste(img, (0,y_offset))
  #   y_offset += img.size[1]
  
  for idx, img in enumerate(images):
    result_img.paste(img, (0, y_offset))
    y_offset += img.size[1]

    progress = (idx +1)/len(images)*100
    p_var.set(progress)
    progress_bar.update()
  
  dest_path = os.path.join(txt_dest_path.get(), "result.jpg")
  result_img.save(dest_path)
  msgbox.showinfo("Alert", "sucessfully complete!")

def add_file():
  files = filedialog.askopenfilenames(title="choose image files", \
    filetypes=(("PNG file", "*.png"), ("All files", "*.*")), \
    initialdir="C:/")
  for file in files:
    list_file.insert(END, file)

def del_file():
  for index in reversed(list_file.curselection()):
    list_file.delete(index)

def browse_dest_path():
  folder_selected = filedialog.askdirectory()
  if folder_selected is None:
    reutrn
  txt_dest_path.delete(0, END)
  txt_dest_path.insert(0, folder_selected)


def start():
  print("width :", cmb_width.get())
  print("space :", cmb_space.get())
  print("format :", cmb_format.get())

  #Check file list
  if list_file.size() == 0:
    msgbox.showwarning("Warning", "Please add an image file")
    return
  
  #Check save path
  if len(txt_dest_path.get()) == 0:
    msgbox.showwarning("Warning", "Choose a save path")
    return

  #Image merge
  merge_image()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add file", command=add_file)
btn_add_file.pack(side="left")
btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete select", command=del_file)
btn_add_file.pack(side="right")

#list frame
list_frame= Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True, padx=5, pady=5)
scrollbar.config(command=list_file.yview)


path_frame = LabelFrame(root, text="Save path")
path_frame.pack(fill="both", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_dest_path = Button(path_frame, text="Find", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

#Option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

lbl_width = Label(frame_option, text="width", width=8)
lbl_width.pack(side="left")

opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)


lbl_space = Label(frame_option, text="space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["None", "narrow", "normal", "wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)


lbl_format = Label(frame_option, text="format", width=8)
lbl_format.pack(side="left")

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left")


#Progress Bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var )
progress_bar.pack(fill="x", padx=5, pady=5)


frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False,False)
root.mainloop()