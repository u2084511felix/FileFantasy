
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x400")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the current input
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, bg="light gray", justify="right")
        entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button("C", 5, 0)
        self.create_button("(", 5, 1)
        self.create_button(")", 5, 2)
        self.create_button("CE", 5, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, text):
        if text == "C":
            self.result_var.set("")
        elif text == "CE":
            self.result_var.set(self.result_var.get()[:-1])
        elif text == "=":
            try:
                self.result_var.set(eval(self.result_var.get()))
            except:
                self.result_var.set("Error")
        else:
            self.result_var.set(self.result_var.get() + text)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
