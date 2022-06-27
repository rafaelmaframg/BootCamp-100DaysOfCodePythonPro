import tkinter as tk
from tkinter import messagebox
import os



path = os.path.dirname(__file__)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    with open(os.path.join(path,'data.txt'), 'a') as file:
        file.write(f"{entry_website.get()} | {entry_email.get()} | {entry_password.get()}\n")
    entry_password.delete(0, last='end')
    entry_website.delete(0, last='end')
    messagebox.showinfo(message='Done!', title="Done!")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.config(pady=50, padx=50)
window.title("My Password Manager")

logo = tk.Canvas(width=150, height=200)
img = tk.PhotoImage(file=os.path.join(path, 'logo.png'))
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

btn_generate = tk.Button(text="Generate Password")
btn_generate.grid( row=3, column=2)

btn_add = tk.Button(text="ADD", width=36, command=save_data)
btn_add.grid(row=4, column=1, columnspan=2)
window.mainloop()