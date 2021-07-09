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
    new_text = entry.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click Me", command=button_clicker)
button.pack()

# Entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")  # Adds some text to begin with.
print(entry.get())  # Gets text in entry
entry.pack()

# Text
text = Text(height=5, width=30)
text.focus()  # Put cursor in textbox.
text.insert(END, "Example of multi-line text entry.")  # Adds some text to begin with.
print(text.get("1.0", END))  # Get's current value in textbox at line 1, character 0
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())  # Gets the current value in spinbox.


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # print 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state,0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List box
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# show all time screen
window.mainloop()