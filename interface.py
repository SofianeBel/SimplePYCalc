import customtkinter
from calculs import Calculs

class Interface:
    def __init__(self):
        self.calculs = Calculs()

        self.app = customtkinter.CTk()
        self.app.title("Calculatrice")

        # Ajouter un effet de transparence à la fenêtre
        self.app.attributes('-alpha', 0.99)  # Valeur entre 0 (transparent) et 1 (opaque)

        # Section pour le label (écran)
        self.screen_frame = customtkinter.CTkFrame(self.app)
        self.screen_frame.pack(pady=10, padx=10, fill='x')  # Remplit l'espace horizontalement
        self.screen_frame.configure(border_width=2, border_color="black")

        self.screen = customtkinter.CTkLabel(self.screen_frame, text="0", font=("Helvetica", 32))
        self.screen.pack(pady=10, padx=10, fill='x')  # Remplit l'espace horizontalement

        # Section pour les boutons numériques
        self.num_frame = customtkinter.CTkFrame(self.app)
        self.num_frame.pack(pady=10, padx=10, fill='x')  # Remplit l'espace horizontalement

        for i in range(9, -1, -1):
            button = customtkinter.CTkButton(self.num_frame, text=str(i), command=lambda i=i: self.on_button_click(i))
            button.grid(row=(9 - i) // 3, column=(9 - i) % 3, padx=5, pady=5, sticky='nsew')
            # mettre le 0 au milieu
            if i == 0:
                button.grid(row=3, column=1)

        # Rendre les colonnes du num_frame extensibles
        for col in range(3):
            self.num_frame.grid_columnconfigure(col, weight=1)

        # Bouton égal
        self.equals_button = customtkinter.CTkButton(self.app, text='=', command=self.on_equals_click)
        self.equals_button.pack(pady=30, padx=10, fill='x')  # Remplit l'espace horizontalement

        # Section pour les boutons opératoires
        self.op_frame = customtkinter.CTkFrame(self.app)
        self.op_frame.pack(pady=30, padx=10, fill='x')  # Remplit l'espace horizontalement

        for sign in ["+", "-", "*", "/"]:
            buttonOp = customtkinter.CTkButton(self.op_frame, text=sign, command=lambda sign=sign: self.on_buttonOp_click(sign))
            buttonOp.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        # Bouton Clear
        self.clear_button = customtkinter.CTkButton(self.app, text='C', command=self.on_clear_click)
        self.clear_button.pack(pady=5, padx=10, fill='x')  # Remplit l'espace horizontalement

        # Lier les événements de frappe de touches
        self.app.bind('<Key>', self.on_key_press)

        self.app.mainloop()

    def on_button_click(self, value):
        result = self.calculs.input_number(value)
        self.screen.configure(text=result)

    def on_buttonOp_click(self, op):
        self.calculs.input_operator(op)
        self.screen.configure(text=self.calculs.current_value)

    def on_equals_click(self):
        result = self.calculs.calculate()
        self.screen.configure(text=result)

    def on_clear_click(self):
        self.calculs.clear()
        self.screen.configure(text='0')

    def on_key_press(self, event):
        key = event.char
        if key.isdigit():
            self.on_button_click(key)
        elif key in ['+', '-', '*', '/']:
            self.on_buttonOp_click(key)
        elif key == '=' or key == '\r':
            self.on_equals_click()
        elif key == 'c' or key == 'C':
            self.on_clear_click()

# Pour exécuter l'interface
if __name__ == "__main__":
    Interface()