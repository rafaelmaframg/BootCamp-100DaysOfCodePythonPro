import tkinter as tk
from turtle import onclick


myapp = tk.Tk()
myapp.minsize(300,200)
myapp.title("Mile To KM Converter")

myapp.config(padx=60, pady=50)

def calculate(value):
    value *= 1.609
    result.config(text=str(round(value,2)))



#entry miles
miles = tk.Entry(width=5)
miles.grid(column=1, row=0)

#label miles 
lbl = tk.Label(text='Miles')
lbl.grid(column=2, row=0)

#label is equal to
lbl1 = tk.Label(text='Is equal to')
lbl1.grid(column=0, row=1)

#  result 
result = tk.Label(text=0)
result.grid(column=1, row=1)

# KM
lbl2 = tk.Label(text='KM')
lbl2.grid(column=2, row=1)

#button calculate
btn = tk.Button(text="Calculate", command=lambda:calculate(float(miles.get())))
btn.grid(column=1, row=2)








myapp.mainloop()