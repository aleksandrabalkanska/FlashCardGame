from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#E9EDC9"
word = {}
word_bank = {}

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_word_data = pandas.read_csv("data/korean_words.csv")
    word_bank = original_word_data.to_dict(orient="records")
else:
    word_bank = word_data.to_dict(orient="records")


# Generate New Words
def new_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = choice(word_bank)

    canvas.itemconfig(language_text, text="Korean")
    canvas.itemconfig(word_text, text=word["Korean"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = window.after(3000, flip_card)


# Flip the Card
def flip_card():
    global word
    english_word = word["English"]

    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=english_word, fill="#FF6969")
    canvas.itemconfig(canvas_image, image=back_card)


# Learned Words
def save_word():
    word_bank.remove(word)
    data = pandas.DataFrame(word_bank)
    data.to_csv("data/words_to_learn.csv", index=False)

    new_word()


# UI Design
window = Tk()
window.title("Korean - English Flashcards")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=500, height=330, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(250, 165, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(250, 50, text="", font=("Arial", 20, "italic"))
word_text = canvas.create_text(250, 160, text="", font=("Arial", 35, "bold"))


correct_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat",
                        activebackground=BACKGROUND_COLOR, command=save_word)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat",
                      activebackground=BACKGROUND_COLOR, command=new_word)
correct_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

new_word()

window.mainloop()
