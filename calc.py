import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        # Кнопки пока пустые
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20)
            button.grid(row=row, column=col)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
