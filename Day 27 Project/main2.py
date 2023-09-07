from tkinter import *


def botton_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)


#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()


#Botton
botton = Button(text="Click Me", command=botton_clicked)
botton.pack()



#Entry
input = Entry(width=10)
print(input.get())
input.pack()
