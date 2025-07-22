import tkinter as tk
class Caclulatorlogic():
    def __init__(self):
        self.expression = ''
    def input(self, char):
        if char == '=' :
            return self.evaluate()
        else :
            self.expression += str(char)
            return self.expression
    def evaluate(self):
        try :
            result =  str(eval(self.expression))
            self.expression = result
            return result
        except Exception:
            self.expression = ''
            return 'Error'
    def clear(self):
        self.expression = ''
        return ''

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x400")
        self.root.resizable(False, False)

        self.logic = Caclulatorlogic()
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry field
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=20)

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('Arial', 18),
                               width=22, bd=5, relief="ridge", justify='right')
        input_field.pack()

        # Buttons layout
        btns_frame = tk.Frame(self.root)
        btns_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(btns_frame, text=btn_text, font=('Arial', 16), width=5, height=2,
                                command=lambda txt=btn_text: self.on_button_click(txt))
                btn.grid(row=i, column=j, padx=5, pady=5)

        # Clear button
        clear_btn = tk.Button(self.root, text="C", font=('Arial', 16), width=20, height=2,
                              bg='red', fg='white', command=self.clear_input)
        clear_btn.pack(pady=10)

    def on_button_click(self, char):
        result = self.logic.input(char)
        self.input_text.set(result)

    def clear_input(self):
        result = self.logic.clear()
        self.input_text.set(result)

if __name__ == "__main__":
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()