'''import tkinter

top = tkinter.Tk()

# Code to add widgets will go here...
top.mainloop()'''

'''import tkinter as tk
class App(tk.Tk):
   def __init__(self):
      super().__init__()

app = App()
app.mainloop()'''

from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()

top.geometry("200x200")
def show():
   num = askinteger("Input", "Input an Integer")
   print(num)
   
B = Button(top, text ="Click", command = show)
B.place(x=150,y=150)

#top.mainloop()

from tkinter.simpledialog import askfloat
from tkinter import *
top = Tk()

top.geometry("100x100")
def show():
   num = askfloat("Input", "Input a floating point number")
   print(num)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

#top.mainloop()

from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()

top.geometry("100x100")
def show():
   name = askstring("Input", "Enter you name")
   print(name)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

#top.mainloop()


from tkinter.filedialog import askopenfile
from tkinter import *

top = Tk()

top.geometry("100x100")
def show():
   filename = askopenfile()
   print(filename)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

#top.mainloop()

from tkinter.colorchooser import askcolor
from tkinter import *

top = Tk()

top.geometry("100x100")
def show():
   color = askcolor()
   print(color)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

#top.mainloop()

from tkinter import *
from tkinter import ttk

top = Tk()
top.geometry("200x150")

frame = Frame(top)
frame.pack()

langs = ["C", "C++", "Java",
   "Python", "PHP"]
   
Combo = ttk.Combobox(frame, values = langs)
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)
top.mainloop()


#To override the basic Tk widgets, the import should follow the Tk import −
#from tkinter import *
#from tkinter.ttk import *


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frame= ttk.Frame(root)
def increment():
   progressBar.step(20)
   
def decrement():
   progressBar.step(-20)
   
def display():
   print(progressBar["value"])

progressBar= ttk.Progressbar(frame, mode='determinate')
progressBar.pack(padx = 10, pady = 10)

button= ttk.Button(frame, text= "Increase", command= increment)
button.pack(padx = 10, pady = 10, side = tk.LEFT)

button= ttk.Button(frame, text= "Decrease", command= decrement)
button.pack(padx = 10, pady = 10, side = tk.LEFT)
button= ttk.Button(frame, text= "Display", command= display)
button.pack(padx = 10, pady = 10, side = tk.LEFT)

frame.pack(padx = 5, pady = 5)
#root.mainloop()




import tkinter as tk
from tkinter import ttk

root = tk.Tk()
nb = ttk.Notebook(root)

# Frame 1 and 2
frame1 = ttk.Frame(nb)
frame2 = ttk.Frame(nb)

label1 = ttk.Label(frame1, text = "This is Window One")
label1.pack(pady = 50, padx = 20)
label2 = ttk.Label(frame2, text = "This is Window Two")
label2.pack(pady = 50, padx = 20)

frame1.pack(fill= tk.BOTH, expand=True)
frame2.pack(fill= tk.BOTH, expand=True)
nb.add(frame1, text = "Window 1")
nb.add(frame2, text = "Window 2")

frame3 = ttk.Frame(nb)
label3 = ttk.Label(frame3, text = "This is Window Three")
label3.pack(pady = 50, padx = 20)
frame3.pack(fill= tk.BOTH, expand=True)
nb.insert("end", frame3, text = "Window 3")
nb.pack(padx = 5, pady = 5, expand = True)

#root.mainloop()



import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

root = tk.Tk()
data = [
   ["Bobby",26,20000],
   ["Harrish",31,23000],
   ["Jaya",18,19000],
   ["Mark",22, 20500],
]
index=0
def read_data():
   for index, line in enumerate(data):
      tree.insert('', tk.END, iid = index,
         text = line[0], values = line[1:])
columns = ("age", "salary")

tree= ttk.Treeview(root, columns=columns ,height = 20)
tree.pack(padx = 5, pady = 5)

tree.heading('#0', text='Name')
tree.heading('age', text='Age')
tree.heading('salary', text='Salary')

read_data()
root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("100x100")

frame = ttk.Frame(root)
label = ttk.Label(root, text = "Hello World")
label.pack(padx = 5, pady = 5)
sizegrip = ttk.Sizegrip(frame)
sizegrip.pack(expand = True, fill = tk.BOTH, anchor = tk.SE)
frame.pack(padx = 10, pady = 10, expand = True, fill = tk.BOTH)

root.mainloop()

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.geometry("200x150")

frame = ttk.Frame(root)

label = ttk.Label(frame, text = "Hello World")
label.pack(padx = 5)

separator = ttk.Separator(frame,orient= tk.HORIZONTAL)
separator.pack(expand = True, fill = tk.X)

label = ttk.Label(frame, text = "Welcome To TutorialsPoint")
label.pack(padx = 5)

frame.pack(padx = 10, pady = 50, expand = True, fill = tk.BOTH)

root.mainloop()



from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

'''To illustrate, here is the Tcl/Tk equivalent of the main part of the Tkinter script above.

ttk::frame .frm -padding 10
grid .frm
grid [ttk::label .frm.lbl -text "Hello World!"] -column 0 -row 0
grid [ttk::button .frm.btn -text "Quit" -command "destroy ."] -column 1 -row 0'''



import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()



import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()



def turn_red(self, event):
    event.widget["activeforeground"] = "red"

self.button.bind("<Enter>", self.turn_red)

