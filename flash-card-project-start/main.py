import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/The_oxford_3000_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, fill="black", text="English")
    canvas.itemconfig(card_word, fill="black", text=current_card["English"])
    canvas.itemconfig(card_background, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, fill="white", text="Thai")
    canvas.itemconfig(card_word, fill="white", text=current_card["Thai"])
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI SETUP
# set window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# set background
canvas = Canvas(width=800, height=526)

# insert picture
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_image)
# set label
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# set button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
