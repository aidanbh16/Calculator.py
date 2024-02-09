import tkinter as tk

#creation of window
window = tk.Tk()
window.resizable(False, False)
window.title("Calculator")
window.geometry("400x377")
window.configure(background="snow2")

#textbox string
calc = ""

#functions
#input function
def place(one):
    global calc
    calc += str(one)
    total.delete(1.0, "end")
    total.insert(1.0, calc)

#calculate function  
def evaluate():
    global calc
    try:
        calc = str(eval(calc))
        total.delete(1.0, "end")
        total.insert(1.0, calc)
    except:
        clear()
        total.insert(1.0, "Error")

#clear function
def clear():
    global calc
    calc = ""
    total.delete(1.0, "end")

#textbox
total = tk.Text(window, height=2, font=('Arial', 18), bg="white smoke")
total.pack(padx=20, pady=20)

#Creation of the inside of the window
frame = tk.Frame(window)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.rowconfigure(1, weight=0)
frame.pack(fill="x")

#Button creation, design, and positioning
one = tk.Button(frame, text="1", font=('Arial', 20), command=lambda: place(1), bg="azure")
one.grid(row="0", column="0", sticky=tk.W+tk.E)
two = tk.Button(frame, text="2", font=('Arial', 20), command=lambda: place(2), bg="azure")
two.grid(row="0", column="1", sticky=tk.W+tk.E)
three = tk.Button(frame, text="3", font=('Arial', 20), command=lambda: place(3), bg="azure")
three.grid(row="0", column="2", sticky=tk.W+tk.E)
plus = tk.Button(frame, text="+", font=('Arial', 20), command=lambda: place("+"), bg="thistle1")
plus.grid(row="0", column="3", sticky=tk.W+tk.E)
four = tk.Button(frame, text="4", font=('Arial', 20), command=lambda: place(4), bg="azure")
four.grid(row="1", column="0", sticky=tk.W+tk.E)
five = tk.Button(frame, text="5", font=('Arial', 20), command=lambda: place(5), bg="azure")
five.grid(row="1", column="1", sticky=tk.W+tk.E)
six = tk.Button(frame, text="6", font=('Arial', 20), command=lambda: place(6), bg="azure")
six.grid(row="1", column="2", sticky=tk.W+tk.E)
minus = tk.Button(frame, text="-", font=('Arial', 20), command=lambda: place("-"), bg="thistle1")
minus.grid(row="1", column="3", sticky=tk.W+tk.E)
seven = tk.Button(frame, text="7", font=('Arial', 20), command=lambda: place(7), bg="azure")
seven.grid(row="2", column="0", sticky=tk.W+tk.E)
eight = tk.Button(frame, text="8", font=('Arial', 20), command=lambda: place(8), bg="azure")
eight.grid(row="2", column="1", sticky=tk.W+tk.E)
nine = tk.Button(frame, text="9", font=('Arial', 20), command=lambda: place(9), bg="azure")
nine.grid(row="2", column="2", sticky=tk.W+tk.E)
mult = tk.Button(frame, text="x", font=('Arial', 20), command=lambda: place("*"), bg="thistle1")
mult.grid(row="2", column="3", sticky=tk.W+tk.E)
decimal = tk.Button(frame, text=".", font=('Arial', 20), command=lambda: place("."), bg="azure")
decimal.grid(row="3", column="0", sticky=tk.W+tk.E)
zero = tk.Button(frame, text="0", font=('Arial', 20), command=lambda: place(0), bg="azure")
zero.grid(row="3", column="1", sticky=tk.W+tk.E)
clearbut = tk.Button(frame, text="C", font=('Arial', 20), command=lambda: clear(), bg="azure")
clearbut.grid(row="3", column="2", sticky=tk.W+tk.E)
divide = tk.Button(frame, text="/", font=('Arial', 20), command=lambda: place("/"), bg="thistle1")
divide.grid(row="3", column="3", sticky=tk.W+tk.E)
equal = tk.Button(frame, text="=", font=('Arial', 20), command=lambda: evaluate(), bg="cornsilk1")
equal.grid(row="4", columnspan="4", sticky="nsew")

#opens window
window.mainloop()
            