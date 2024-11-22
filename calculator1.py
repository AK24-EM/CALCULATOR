import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        # Entry field to display numbers and results
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Add buttons to the calculator
        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=("Helvetica", 14), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        current = self.result_var.get()

        # If clear button is pressed
        if button == 'C':
            self.result_var.set("0")
        # If equals button is pressed
        elif button == '=':
            try:
                result = eval(current)
                self.result_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.result_var.set("0")
        # For other buttons
        else:
            if current == "0":
                self.result_var.set(button)
            else:
                self.result_var.set(current + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()