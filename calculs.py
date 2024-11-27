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


class calculs():
    def __init__(self):
        self.value = 0

    def add(self, value):
        self.value += value
        return self.value
    
    def substract(self, value):
        self.value -= value
        return self.value
    
    def multiply(self, value):
        self.value *= value
        return self.value
    
    def divide(self, value):
        self.value /= value
        return self.value