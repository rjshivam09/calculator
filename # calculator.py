# calculator.py

import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.expression = ""

        # Create entry field
        self.entry_field = tk.Entry(self.root, width=35, borderwidth=5)
        self.entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create number buttons
        button_1 = tk.Button(self.root, text="1", padx=40, pady=20, command=lambda: self.append_to_expression("1"))
        button_2 = tk.Button(self.root, text="2", padx=40, pady=20, command=lambda: self.append_to_expression("2"))
        button_3 = tk.Button(self.root, text="3", padx=40, pady=20, command=lambda: self.append_to_expression("3"))
        button_4 = tk.Button(self.root, text="4", padx=40, pady=20, command=lambda: self.append_to_expression("4"))
        button_5 = tk.Button(self.root, text="5", padx=40, pady=20, command=lambda: self.append_to_expression("5"))
        button_6 = tk.Button(self.root, text="6", padx=40, pady=20, command=lambda: self.append_to_expression("6"))
        button_7 = tk.Button(self.root, text="7", padx=40, pady=20, command=lambda: self.append_to_expression("7"))
        button_8 = tk.Button(self.root, text="8", padx=40, pady=20, command=lambda: self.append_to_expression("8"))
        button_9 = tk.Button(self.root, text="9", padx=40, pady=20, command=lambda: self.append_to_expression("9"))
        button_0 = tk.Button(self.root, text="0", padx=40, pady=20, command=lambda: self.append_to_expression("0"))

        # Create operator buttons
        button_add = tk.Button(self.root, text="+", padx=40, pady=20, command=lambda: self.append_to_expression("+"))
        button_subtract = tk.Button(self.root, text="-", padx=40, pady=20, command=lambda: self.append_to_expression("-"))
        button_multiply = tk.Button(self.root, text="*", padx=40, pady=20, command=lambda: self.append_to_expression("*"))
        button_divide = tk.Button(self.root, text="/", padx=40, pady=20, command=lambda: self.append_to_expression("/"))
        button_equals = tk.Button(self.root, text="=", padx=40, pady=20, command=self.calculate)
        button_clear = tk.Button(self.root, text="Clear", padx=40, pady=20, command=self.clear_expression)

        # Grid layout
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)

        button_0.grid(row=4, column=0)
        button_add.grid(row=4, column=1)
        button_subtract.grid(row=4, column=2)

        button_multiply.grid(row=5, column=0)
        button_divide.grid(row=5, column=1)
        button_equals.grid(row=5, column=2)
        button_clear.grid(row=6, column=0, columnspan=3)

    def append_to_expression(self, value):
        self.expression += value
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, result)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_expression(self):
        self.expression = ""
        self.entry_field.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()