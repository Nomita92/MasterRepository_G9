import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

def add():
    number1 = int(number1_entry.get())
    number2 = int(number2_entry.get())
    p = number1 + number2
    result_label.set(p)

def sub():
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    q = number1 - number2
    result_label.set(q)

def product():
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    r = number1 * number2
    result_label.set(r)

def modulus():
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    s = number1 % number2
    result_label.set(s)

def divide():
    number1 = float(number1_entry.get())
    number2 = float(number2_entry.get())
    t = number1 / number2
    result_label.set(t)

ttk.Label(root, text='Enter number 1:').pack()
number1 = tk.StringVar()
number1_entry = ttk.Entry(root, textvariable=number1)
number1_entry.focus()
number1_entry.pack()

ttk.Label(root, text='Enter number 2:').pack()
number2 = tk.StringVar()
number2_entry = ttk.Entry(root, textvariable=number2)
number2_entry.pack()

sum_button = ttk.Button(root, text='+', command=add)
sum_button.pack()

sub_button = ttk.Button(root, text='-', command=sub)
sub_button.pack()

product_button = ttk.Button(root, text='*', command=product)
product_button.pack()

modulus_button = ttk.Button(root, text='%', command=modulus)
modulus_button.pack()

divide_button = ttk.Button(root, text='/', command=divide)
divide_button.pack()

result_label = tk.StringVar()
result_label.set("Result")
l = ttk.Label(root, textvariable=result_label)
l.pack()

root.mainloop()