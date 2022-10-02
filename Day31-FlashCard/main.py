import os
import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
PATH = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(PATH, 'data/eng_word.csv'))


# ----------------------------Data reader---------------------------------------------
def get_new_word():
    global word, data, canvas, flip_timer
    window.after_cancel(flip_timer)
    word = data.loc[random.randint(1, 100)]
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_text, text=word['English'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)
    return word


def flip_card():
    canvas.itemconfig(card_title, text="Portuguese", fill="white")
    canvas.itemconfig(card_text, text=word['Portuguese'], fill='white')
    canvas.itemconfig(card_background, image=card_back)


# ---------------------------UI Interface -------------------------------------------
word = 'test'
window = tk.Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("FlashCard")
flip_timer = window.after(3000, func=flip_card)

canvas = tk.Canvas(window, width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file=os.path.join(PATH, "images/card_front.png"))
card_back = tk.PhotoImage(file=os.path.join(PATH, "images/card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 250, text="", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

x_img = tk.PhotoImage(file=os.path.join(PATH, "images/wrong.png"))
x_button = tk.Button(image=x_img, highlightthickness=0, command=get_new_word)
x_button.grid(row=1, column=0)

v_img = tk.PhotoImage(file=os.path.join(PATH, "images/right.png"))
v_button = tk.Button(image=v_img, highlightthickness=0, command=get_new_word)
v_button.grid(row=1, column=1)
get_new_word()


window.mainloop()
