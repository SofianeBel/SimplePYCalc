import customtkinter
from calculs import Calculs

calculs = Calculs()

def on_button_click(value):
    result = calculs.input_number(value)
    screen.configure(text=result)

def on_buttonOp_click(op):
    calculs.input_operator(op)
    screen.configure(text=calculs.current_value)

def on_equals_click():
    result = calculs.calculate()
    screen.configure(text=result)

def on_clear_click():
    calculs.clear()
    screen.configure(text='0')

class Interface():
    def __init__(self):
        app = customtkinter.CTk()
        app.title("Calculatrice")
        app.geometry("400x500")

        # Section pour le label
        global screen
        screen = customtkinter.CTkLabel(app, text="0", font=("Helvetica", 32))
        screen.pack(pady=10)

        # Section pour les boutons numériques
        num_frame = customtkinter.CTkFrame(app)
        num_frame.pack(pady=10)

        for i in range(9, -1, -1):
            button = customtkinter.CTkButton(num_frame, text=str(i), command=lambda i=i: on_button_click(i))
            button.grid(row=(9 - i)//3, column=(9 - i)%3, padx=5, pady=5)
            if i == 0:
                button.grid(row=3, column=1)

        # Bouton égal
        equals_button = customtkinter.CTkButton(app, text='=', command=on_equals_click)
        equals_button.pack(pady=5)

        # Section pour les boutons opératoires
        op_frame = customtkinter.CTkFrame(app)
        op_frame.pack(pady=10)

        for sign in ["+", "-", "x", "/"]:
            buttonOp = customtkinter.CTkButton(op_frame, text=sign, command=lambda sign=sign: on_buttonOp_click(sign))
            buttonOp.pack(side="left", padx=5, pady=5)

        # Bouton Clear
        clear_button = customtkinter.CTkButton(app, text='C', command=on_clear_click)
        clear_button.pack(pady=5)

        app.mainloop()

