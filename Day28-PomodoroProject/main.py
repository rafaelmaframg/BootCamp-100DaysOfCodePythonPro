from cgitb import enable, text
from email.mime import image
import tkinter as tk
import os
import time
from tkinter.font import NORMAL
from turtle import bgcolor
from xml.etree.ElementTree import PI
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PATH = os.path.dirname(__file__)
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global loop, reps
    lbl_mark.config(text='')
    lbl1.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    btn_start.config(state=NORMAL)
    myapp.after_cancel(loop)
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_counter():
    global reps
    reps += 1
    btn_start.config(state=tk.DISABLED)
    if reps != 0 and reps % 8 == 0:
        lbl_mark.config(text='✔' * int(reps/2))
        lbl1.config(text="Long Break", fg=RED)
        counter(LONG_BREAK_MIN * 60)

    elif reps %2 == 0:
        lbl_mark.config(text='✔'* int(reps/2))
        lbl1.config(text="Break", fg=PINK)
        counter(SHORT_BREAK_MIN * 60)
    
    else:
        lbl1.config(text="Work", fg=GREEN)
        counter(WORK_MIN * 60)
     
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def counter(count):
    global loop
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(timer, text=f'{minutes}:{seconds}')
    if count > 0:
        loop = myapp.after(10, counter, count -1)
    else:
        start_counter()

        


# ---------------------------- UI SETUP ------------------------------- #
myapp = tk.Tk()

myapp.title("Pomodoro")
myapp.config(padx=100, pady=50, bg=YELLOW)

#timer label
lbl1 = tk.Label(text="Timer", font=(FONT_NAME, 35, 'bold'),fg=GREEN, bg=YELLOW)
lbl1.grid(column=1, row=0)

#tomato
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file=os.path.join(PATH,"tomato.png"))
canvas.create_image(100,112, image=tomato)
canvas.grid(column=1, row=1)
#text inside tomato
timer = canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#button start
btn_start = tk.Button(text="Start", command=start_counter)
btn_start.grid(column=0, row=2)

#text mark
lbl_mark = tk.Label(font=(FONT_NAME, 14, 'bold'), fg=GREEN, bg=YELLOW)
lbl_mark.grid(column=1, row=3)

#button reset
btn_reset = tk.Button(text='Reset', command=reset)
btn_reset.grid(column=2, row=2)

myapp.mainloop()
