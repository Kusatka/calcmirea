import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        # Кнопки калькулятора
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 0),
            ('C', 4, 1), ('=', 4, 2)
        ]

        for (text, row, col) in buttons:
            if text == "+":
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=self.addition)
            elif text == "-":
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=self.subtraction)
            elif text == "=":
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=self.calculate)
            elif text == "C":
                button = tk.Button(self.root, text=text, padx=20, pady=20, command=self.clear_display)
            else:
                button = tk.Button(self.root, text=text, padx=20, pady=20,
                                   command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col)

    def button_click(self, value):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + value)

    def clear_display(self):
        self.display.delete(0, tk.END)

    def addition(self):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + "+")

    def subtraction(self):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + "-")

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Ошибка")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
