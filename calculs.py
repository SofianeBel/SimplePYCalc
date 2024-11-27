import inspect

def handle_button_click(value):
    frame = inspect.currentframe()
    print(f"Button {value} clicked at line {frame.f_back.f_lineno}!")
    return value

def handle_buttonOp_click(value):
    frame = inspect.currentframe()
    print(f"Button {value} clicked! at line {frame.f_back.f_lineno}")
    return value

def handle_label_change(value):
    return value


class Calculs():
    def __init__(self):
        self.current_value = 0
        self.operator = None
        self.new_value = ''
        self.is_result = False

    def input_number(self, num):
        if self.is_result:
            self.new_value = str(num)
            self.is_result = False
        else:
            self.new_value += str(num)
        return self.new_value

    def input_operator(self, op):
        if self.operator and self.new_value != '':
            self.calculate()
        elif self.new_value != '':
            self.current_value = float(self.new_value)
        self.operator = op
        self.new_value = ''
        return self.current_value

    def calculate(self):
        if self.operator == '+':
            self.current_value += float(self.new_value)
        elif self.operator == '-':
            self.current_value -= float(self.new_value)
        elif self.operator == 'x':
            self.current_value *= float(self.new_value)
        elif self.operator == '/':
            if float(self.new_value) != 0:
                self.current_value /= float(self.new_value)
            else:
                self.current_value = 'Erreur : division par zéro'
        self.operator = None
        self.new_value = ''
        self.is_result = True
        return self.current_value

    def clear(self):
        self.current_value = 0
        self.operator = None
        self.new_value = ''
        self.is_result = False