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

