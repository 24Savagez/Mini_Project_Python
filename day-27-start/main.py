import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()  # show label

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicker():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click Me", command=button_clicker)
button.pack()

# Entry
input = Entry(width=15)
input.pack()

# show all time screen
window.mainloop()
