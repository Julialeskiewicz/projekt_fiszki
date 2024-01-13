#Fiszki
from tkinter import *
from pandas import *
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# csv
try:
    x = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    x = read_csv("./data/english_words.csv")

to_learn = x.to_dict(orient="records")
current_card = {}

def random_word():
    global current_card, flip_timer

    if to_learn:
        window.after_cancel(flip_timer)
        f_card.itemconfig(canvas_image, image=front)
        current_card = random.choice(to_learn)
        english_words = current_card["POLISH"]
        f_card.itemconfig(card_title, text="POLISH", fill="#000000")
        f_card.itemconfig(card_word, text=english_words, fill="#000000")
        flip_timer = window.after(3000, func=random_english)
    else:
        window.destroy()

def random_english():
    f_card.itemconfig(canvas_image, image=back)
    english_word = current_card["ENGLISH"]
    f_card.itemconfig(card_title, text="ENGLISH", fill="#FFFFFF")
    f_card.itemconfig(card_word, text=english_word, fill="#FFFFFF")

def ok_button():
    to_learn.remove(current_card)
    words_to = DataFrame(data=to_learn)
    words_to.to_csv("data/words_to_learn.csv", index=False)
    random_word()

# tkinter GUI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.minsize(width=600, height=400)

flip_timer = window.after(3000, random_word)

X_image = PhotoImage(file="./images/wrong.png")
X_button = Button(image=X_image, highlightthickness=0, command=random_word)
X_button.grid(column=0, row=1)

V_image = PhotoImage(file="./images/right.png")
V_button = Button(image=V_image, highlightthickness=0, command=ok_button)
V_button.grid(column=1, row=1)


front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
f_card = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = f_card.create_image(400, 263, image=front)
f_card.grid(column=0, row=0, columnspan=2)
card_title = f_card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = f_card.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
random_word()

window.mainloop()
