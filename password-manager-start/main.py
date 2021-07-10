from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    # send password to box
    pass_entry.insert(0, password)
    # auto copy password to clipboard
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get value from entries
    website = web_entry.get()
    email = user_entry.get()
    passwords = pass_entry.get()

    # check fill
    if len(website) == 0 or len(email) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    # confirm box
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \nEmail: {email} "
                                                              f"\nPassword: {passwords} \nIs it ok to save?")
        if is_ok:
            # save in text
            with open("data.text", "a") as data:
                data.write(f"{website} | {email} | {passwords}\n")
            # delete data
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# set window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# set background
canvas = Canvas(width=200, height=200)
# insert picture
key_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1)

# Label
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=50)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
user_entry = Entry(width=50)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "chutayu.adhi@bumail.net")
pass_entry = Entry(width=32)
pass_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# show all times
window.mainloop()
