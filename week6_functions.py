"""
import tkinter as tk
import tkinter.font as tkfont

a = 0

def increase():
    global a
    a += 1
    l2.config(text=f"count/{a}")

def validate():
    if len(passw.get()) > 8:
        l1.config(text=login.get())
    else:
        l1.config(text="Password must be more than 8 letters")

root = tk.Tk()
root.geometry("300x300")


l1 = tk.Label(root, text="New Text", fg="blue", background="white")
l1.pack()


custom_font = tkfont.Font(family="Arial", size="11")
l2 = tk.Label(root, text="count/0", fg="red", font=custom_font)
l2.pack()

b = tk.Button(root, text="Click button", command=increase)
b.pack()

login = tk.Entry(root)
passw = tk.Entry(root)
submit = tk.Button(root, text="Submit", command=validate)

login.pack(pady="5")
passw.pack(pady="5")
submit.pack()

root.mainloop()
"""

import tkinter as tk

def average():
    av = (int(m.get()) + int(ph.get()) + int(pl.get()))/3
    
    if av >= 90:
        result.config(bg="green")
    elif av >= 70:
        result.config(bg="yellow")
    else:
        result.config(bg="red")
    
    average_button.config(text="Recalculate")

root = tk.Tk()

math = tk.Label(text="Math", font=("Courier", 12), bg="lightgray")
physics = tk.Label(text="Physics", font=("Courier", 12), bg="lightgray")
programming = tk.Label(text="Progrmming", font=("Courier", 12), bg="lightgray")

average_button = tk.Button(text="Calculate Average", bg="blue", fg="white", command=average)

result = tk.Label(text="Result", font=("Helvetica", 16, "italic"))

m = tk.Entry(root)
ph = tk.Entry(root)
pl = tk.Entry(root)

math.pack(pady="5")
m.pack(pady="5")
physics.pack(pady="5")
ph.pack(pady="5")
programming.pack(pady="5")
pl.pack(pady="5")

average_button.pack(pady="10")
result.pack(pady="5")

root.mainloop()    