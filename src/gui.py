from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Apeture Science Image Editor")

frm = ttk.Frame(root, padding=10)
frm.grid()

image_path = StringVar()

ttk.Label(frm, text="Fill in the Required Fields, Submit when Completed").grid(column=1, row=0)
ttk.Label(frm, text="Enter Image Path:").grid(column=0, row=1)
ttk.Entry(frm, textvariable = image_path).grid(column=1, row=1) 
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=10)

root.mainloop()

print(image_path.get())