
from tkinter import *
import tkinter as tk


def display_selected_inputs(choice):
    choice = clicked.get()
    if choice == "Centros Cuadrados":
        seed_input.delete(0, 'end')
        num_rand_input.delete(0, 'end')
        a_lb.grid_remove()
        a_input.grid_remove()
        c_lb.grid_remove()
        c_input.grid_remove()
        m_lb.grid_remove()
        m_input.grid_remove()
        seed_lb.grid(row=1, column=0)
        seed_input.grid(row=1, column=1)
        num_rand_lb.grid(row=2, column=0)
        num_rand_input.grid(row=2, column=1)
    elif choice == "Congruencial":
        seed_input.delete(0, 'end')
        a_input.delete(0, 'end')
        c_input.delete(0, 'end')
        m_input.delete(0, 'end')
        num_rand_input.delete(0, 'end')
        num_rand_lb.grid_remove()
        num_rand_input.grid_remove()

        seed_lb.grid(row=1, column=0)
        seed_input.grid(row=1, column=1)
        a_lb.grid(row=2, column=0)
        a_input.grid(row=2, column=1)
        c_lb.grid(row=3, column=0)
        c_input.grid(row=3, column=1)
        m_lb.grid(row=4, column=0)
        m_input.grid(row=4, column=1)
        num_rand_lb.grid(row=5, column=0)
        num_rand_input.grid(row=5, column=1)


window = Tk()

# Adjust size
window.geometry("800x700")

window.title("Generador de Números Random")


# Labels e inputs
seed_lb = Label(window, text="Semilla*")
seed_input = Entry(window)
num_rand_lb = Label(window, text="No. Randoms")
num_rand_input = Entry(window)
a_lb = Label(window, text="a*")
a_input = Entry(window)
c_lb = Label(window, text="c*")
c_input = Entry(window)
m_lb = Label(window, text="m*")
m_input = Entry(window)

methods_list = [
    "Centros Cuadrados",
    "Congruencial",
    "Congruencial Mixto",
    "Multiplicativo",
    "Congruencial Lineal Combinado",
]

method_lb = Label(window, text="Método")
method_lb.grid(row=0, column=0)
clicked = StringVar()
clicked.set("")

dropdown_menu = OptionMenu(
    window, clicked, *methods_list, command=display_selected_inputs)
dropdown_menu.grid(row=0, column=1)


window.mainloop()
