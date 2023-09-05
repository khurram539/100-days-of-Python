# Day 27 - Tkinter, Dynamic Typing and the Pomodoro GUI Application


import tkinter
import turtle
from tkinter import *

#Creating a new window and configurations
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()

#Botton

def action():
    print("Do something")
  
#Entries
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
print(entry.get())

#Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END)) #1.0 means first line, character 0. END means until the end.
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()   

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Print 1 if On button checked, otherwise 0.
    print(check_state.get())
check_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
check_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()


        


