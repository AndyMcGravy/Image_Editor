from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Apeture Science Image Editor")

frm = ttk.Frame(root, padding=10)
frm.grid()

image_path = StringVar()
output_path = StringVar()
width = IntVar()
height = IntVar()

ttk.Label(frm, text="Fill in the Required Fields, Submit when Completed").grid(column=1, row=0)
ttk.Label(frm, text="Enter Image Path:").grid(column=0, row=1)
ttk.Entry(frm, textvariable = image_path).grid(column=1, row=1) 
ttk.Label(frm, text="Enter Output Path:").grid(column=0, row=2)
ttk.Entry(frm, textvariable = output_path).grid(column=1, row=2)
ttk.Label(frm, text="Enter Width:").grid(column=0, row=3)
ttk.Entry(frm, textvariable = width).grid(column=1, row=3)
ttk.Label(frm, text="Enter Height:").grid(column=0, row=4)
ttk.Entry(frm, textvariable = height).grid(column=1, row=4)
ttk.Button(frm, text="Submit", command=lambda:print("Successfully Submitted")).grid(column=1, row=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=10)

def run_gui(): 
    root.mainloop()


# print(image_path.get()) #uncomment this line to test the image path input 

# run_gui() #uncomment this line to test the GUI