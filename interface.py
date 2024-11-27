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

def on_key_press(event):
    key = event.char
    if key.isdigit():
        on_button_click(key)
    elif key in ['+', '-', '*', '/']:
        on_buttonOp_click(key)
    elif key == '=' or key == '\r':
        on_equals_click()
    elif key == 'c' or key == 'C':
        on_clear_click()

class Interface():
    def __init__(self):
        app = customtkinter.CTk()
        app.title("Calculatrice")

        # Ajouter un effet de transparence à la fenêtre
        app.attributes('-alpha', 0.99)  # Valeur entre 0 (transparent) et 1 (opaque)

        # Section pour le label (écran)
        global screen
        screen_frame = customtkinter.CTkFrame(app)
        screen_frame.pack(pady=10, padx=10, fill='x')  # Remplit l'espace horizontalement
        screen_frame.configure(border_width=2, border_color="black")

        screen = customtkinter.CTkLabel(screen_frame, text="0", font=("Helvetica", 32))
        screen.pack(pady=10, padx=10, fill='x')  # Remplit l'espace horizontalement

        # Section pour les boutons numériques
        num_frame = customtkinter.CTkFrame(app)
        num_frame.pack(pady=10, padx=10, fill='x')  # Remplit l'espace horizontalement

        for i in range(9, -1, -1):
            button = customtkinter.CTkButton(num_frame, text=str(i), command=lambda i=i: on_button_click(i))
            button.grid(row=(9 - i)//3, column=(9 - i)%3, padx=5, pady=5, sticky='nsew')
            # mettre le 0 au milieu
            if i == 0:
                button.grid(row=3, column=1)


        # Rendre les colonnes du num_frame extensibles
        for col in range(3):
            num_frame.grid_columnconfigure(col, weight=1)

        # Bouton égal
        equals_button = customtkinter.CTkButton(app, text='=', command=on_equals_click)
        equals_button.pack(pady=30, padx=10, fill='x')  # Remplit l'espace horizontalement

        # Section pour les boutons opératoires
        op_frame = customtkinter.CTkFrame(app)
        op_frame.pack(pady=30, padx=10, fill='x')  # Remplit l'espace horizontalement

        for sign in ["+", "-", "*", "/"]:
            buttonOp = customtkinter.CTkButton(op_frame, text=sign, command=lambda sign=sign: on_buttonOp_click(sign))
            buttonOp.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        # Bouton Clear
        clear_button = customtkinter.CTkButton(app, text='C', command=on_clear_click)
        clear_button.pack(pady=5, padx=10, fill='x')  # Remplit l'espace horizontalement

        # Lier les événements de frappe de touches
        app.bind('<Key>', on_key_press)

        app.mainloop()