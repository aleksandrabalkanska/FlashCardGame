from tkinter import *

BACKGROUND_COLOR = "#E9EDC9"


# UI Design
window = Tk()
window.title("Korean - English Flashcards")
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

canvas = Canvas(width=500, height=330, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(250, 165, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language_text = canvas.create_text(250, 50, text="Title", font=("Arial", 20, "italic"))
word_text = canvas.create_text(250, 160, text="Language", font=("Arial", 35, "bold"))


correct_button_img = PhotoImage(file="images/right.png")
wrong_button_img = PhotoImage(file="images/wrong.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat",
                        activebackground=BACKGROUND_COLOR)
wrong_button = Button(image=wrong_button_img, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, relief="flat",
                      activebackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

window.mainloop()
