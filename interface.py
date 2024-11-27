import customtkinter
from calculs import handle_button_click, handle_buttonOp_click, handle_label_change

def on_button_click(value):
    """
    Gère l'événement de clic sur un bouton.

    Args:
        value (str): La valeur associée au bouton cliqué.

    Returns:
        str: La valeur du bouton cliqué.
    """
    handle_button_click(value)
    return value

def on_buttonOp_click(value):
    """
    Gère l'événement de clic sur un bouton opératoire.

    Args:
        value (str): La valeur associée au bouton opératoire cliqué.

    Returns:
        str: La valeur du bouton opératoire cliqué.
    """
    handle_buttonOp_click(value)
    return value

def on_label_change(value):
    """
    Gère le changement de la valeur du label.

    Args:
        value (str): La nouvelle valeur du label.

    Returns:
        str: La nouvelle valeur du label.
    """
    print(f"Label changed to {value}!")
    return value



class Interface():
    """
    Gère l'interface graphique de l'application.
    """
    def __init__(self):
        app = customtkinter.CTk()
        app.title("my app")
        app.geometry("400x500")

        # Section pour le label
        label_frame = customtkinter.CTkFrame(app)
        label_frame.pack(pady=50)

        screen = customtkinter.CTkLabel(label_frame, text=" ", font=("Helvetica", 32))
        screen.pack()

        # Section pour les boutons numériques
        num_frame = customtkinter.CTkFrame(app)
        num_frame.pack(pady=10)

        for i in range(9, -1, -1):
            button = customtkinter.CTkButton(num_frame, text=str(i), command=lambda i=i: on_button_click(i))
            button.grid(row=(9 - i)//3, column=(9 - i)%3, padx=5, pady=5)
            if i == 0:
                button.grid(row=3, column=1)

        # Section pour les boutons opératoires
        op_frame = customtkinter.CTkFrame(app)
        op_frame.pack(pady=10)

        for i, sign in enumerate(["+", "-", "x", "/"]):
            buttonOp = customtkinter.CTkButton(op_frame, text=sign, command=lambda sign=sign: on_buttonOp_click(sign))
            buttonOp.pack(side="left", padx=5, pady=5)

        app.mainloop()
    
