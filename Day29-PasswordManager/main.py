from copy import copy
import pyperclip 
import tkinter as tk
from tkinter import messagebox
import random
import os



PATH = os.path.dirname(__file__)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    entry_password.delete(0, last='end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password = [ random.choice(letters) for _ in range(nr_letters)] + \
               [ random.choice(symbols) for _ in range(nr_symbols)] + \
               [ random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password)
    password = ''.join(password)
    pyperclip.copy(password)
    entry_password.insert(index=0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()


    if website != "" and email != "" and password != "":
        with open(os.path.join(PATH, 'data.txt'), 'a') as file:
            file.write(f"{website} | {email} | {password}\n")
        entry_password.delete(0, last='end')
        entry_website.delete(0, last='end')
        messagebox.showinfo(message='Done!', title="Done!")
    
    else:
        messagebox.showerror(message="Please, don't leave any fields empty!", title="ERROR!")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(pady=50, padx=50)
window.title("My Password Manager")

logo = tk.Canvas(width=150, height=200)
img = tk.PhotoImage(file=os.path.join(PATH, 'logo.png'))
logo.create_image(70, 100, image=img)
logo.grid(row=0, column=1)

lbl_website = tk.Label(text="Website:")
lbl_website.grid(sticky='e', row=1, column=0)

entry_website = tk.Entry(width=43)
entry_website.grid( row=1, column=1, columnspan=2)
entry_website.focus()

lbl_email = tk.Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)

entry_email = tk.Entry(width=43)
entry_email.insert(0, "teste@teste.com")
entry_email.grid(row=2, column=1, columnspan=2)

lbl_password = tk.Label(text="Password:")
lbl_password.grid(row=3, column=0)

entry_password = tk.Entry(width=24)
entry_password.grid(row=3, column=1)

btn_generate = tk.Button(text="Generate Password", command=generate_password)
btn_generate.grid( row=3, column=2)

btn_add = tk.Button(text="ADD", width=36, command=save_data)
btn_add.grid(row=4, column=1, columnspan=2)
window.mainloop()