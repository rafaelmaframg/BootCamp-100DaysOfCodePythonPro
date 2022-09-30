import json
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

# ---------------------------- Search Data ------------------------------- #


def search_data():
    website = entry_website.get()
    if website != "":
        try:
            with open(os.path.join(PATH, 'data.json'), 'r') as file:
                loaded = json.load(file)
                messagebox.showinfo(website, message=f"User: {loaded[website]['email']}\n Password: {loaded[website]['password']}")
        except:
            messagebox.showerror(message="Nothing found")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if website != "" and email != "" and password != "":
        try:
            with open(os.path.join(PATH, 'data.json'), 'r') as file:
                loaded = json.load(file)

        except FileNotFoundError:
            with open(os.path.join(PATH, 'data.json'), 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            loaded.update(new_data)
            with open(os.path.join(PATH, 'data.json'), 'w') as file:
                json.dump(loaded, file, indent=4)
        finally:
            entry_password.delete(0, last='end')
            entry_website.delete(0, last='end')
            messagebox.showinfo(message='Done!', title="Done!")
    
    else:
        messagebox.showerror(message="Please, don't leave any fields empty!", title="ERROR!")

# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.config(pady=50, padx=50)
window.title("My Password Manager")

logo = tk.Canvas(width=120, height=175)
img = tk.PhotoImage(file=os.path.join(PATH, 'logo.png'))
logo.create_image(55, 88, image=img)
logo.grid(row=0, column=0, columnspan=3)

lbl_website = tk.Label(text="Website:")
lbl_website.grid(sticky='e', row=1, column=0)

entry_website = tk.Entry(width=20)
entry_website.grid(sticky='w', row=1, column=1)
entry_website.focus()

btn_search = tk.Button(text="Search", width=13, command=search_data)
btn_search.grid(sticky='w', row=1, column=2)

lbl_email = tk.Label(text="Username:")
lbl_email.grid(row=2, column=0)

entry_email = tk.Entry(width=37)
entry_email.insert(0, "teste@teste.com")
entry_email.grid(sticky='w', row=2, column=1, columnspan=2)

lbl_password = tk.Label(text="Password:")
lbl_password.grid(sticky='e', row=3, column=0)

entry_password = tk.Entry(width=20)
entry_password.grid(sticky='w', row=3, column=1)

btn_generate = tk.Button(text="Generate Password", command=generate_password)
btn_generate.grid(sticky='w', row=3, column=2)

btn_add = tk.Button(text="ADD", width=35, command=save_data)
btn_add.grid(row=4, column=1, columnspan=2)
window.mainloop()