import tkinter as tk

Large_font_style = ("Arial", 40, "bold")
Small_font_style = ("Arial", 16)
Digit_font_style = ("Arial", 24, "bold")
Default_font_style = ("Arial", 24)

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x525")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.display_frame()

        self.total_label, self.label = self.display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.digit_buttons()
        self.operations_buttons()
        self.equals_button()
        self.clear_button()
        self.close_button()
        self.bind_keys()

    def display_frame(self):
        frame = tk.Frame(self.window, height=221, bg='#FFFFFF')
        frame.pack(expand=True, fill="both")
        return frame
    
    def display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg='#cfbaf0', fg='#252422', font=Small_font_style, padx=24)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg='#cfbaf0', fg='#252422', font=Default_font_style, padx=24)
        label.pack(expand=True, fill='both')

        return total_label, label
    
    def buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame
    
    def digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), borderwidth=0, bg='#03071e', fg='#ffcfd2',
                               font=Digit_font_style,command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def operations_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg='#03071e', fg='#ffcfd2', font=Default_font_style,
                                 borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg='#03071e', fg='#ffcfd2',
                           font=Default_font_style, borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def clear_button(self):
        button = tk.Button(self.buttons_frame, text="CLEAR", bg='#03071e', fg='#ffcfd2',
                           font=Small_font_style, borderwidth=0, command=self.clear)
        button.grid(row=0, column=2, columnspan=2, sticky=tk.NSEW)

    def close_button(self):
        button = tk.Button(self.buttons_frame, text="CLOSE", bg='#780000', fg='#ffcfd2',
                           font=Small_font_style, borderwidth=0, command=self.close)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        
        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()
    
    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))

            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def close(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()