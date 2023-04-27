import random
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#E9EDC9"


# Generate New Words
def new_word():
    word_data = pandas.read_csv("data/korean_words.csv")
    word_bank = word_data.to_dict(orient="records")

    selected_word = random.choice(word_bank)
    korean_word = selected_word["Korean"]
    english_word = selected_word["English"]

    canvas.itemconfig(language_text, text="Korean")
    canvas.itemconfig(word_text, text=korean_word)


# UI Design
window = Tk()
window.title("Korean - English Flashcards")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width=500, height=330, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(250, 165, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(250, 50, text="", font=("Arial", 20, "italic"))
word_text = canvas.create_text(250, 160, text="", font=("Arial", 35, "bold"))


correct_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat",
                        activebackground=BACKGROUND_COLOR, command=new_word)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat",
                      activebackground=BACKGROUND_COLOR, command=new_word)
correct_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

new_word()

window.mainloop()
