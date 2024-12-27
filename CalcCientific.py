import tkinter as tk
from tkinter import ttk
import math

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # Configuración de la GUI
        self.config_gui()

        # Creación de los botones y campos de texto
        self.crear_botones_y_campos()

        # Configuración de los modos
        self.config_modos()

    def config_gui(self):
        # Configuración del tema
        self.root.configure(bg="#f0f0f0")

        # Configuración de la fuente
        self.font = ("Helvetica", 12)

    def crear_botones_y_campos(self):
        # Campo de texto para la entrada de números
        self.entrada = tk.Entry(self.root, width=35, font=self.font, bg="#ffffff", fg="#000000")
        self.entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botones básicos
        self.boton_suma = tk.Button(self.root, text="+", command=self.suma, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_suma.grid(row=1, column=0, padx=10, pady=10)

        self.boton_resta = tk.Button(self.root, text="-", command=self.resta, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_resta.grid(row=1, column=1, padx=10, pady=10)

        self.boton_multiplicacion = tk.Button(self.root, text="*", command=self.multiplicacion, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_multiplicacion.grid(row=1, column=2, padx=10, pady=10)

        self.boton_division = tk.Button(self.root, text="/", command=self.division, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_division.grid(row=1, column=3, padx=10, pady=10)

        # Botones científicos
        self.boton_seno = tk.Button(self.root, text="sin", command=self.seno, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_seno.grid(row=2, column=0, padx=10, pady=10)

        self.boton_coseno = tk.Button(self.root, text="cos", command=self.coseno, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_coseno.grid(row=2, column=1, padx=10, pady=10)

        self.boton_tangente = tk.Button(self.root, text="tan", command=self.tangente, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_tangente.grid(row=2, column=2, padx=10, pady=10)

        self.boton_logaritmo = tk.Button(self.root, text="log", command=self.logaritmo, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_logaritmo.grid(row=2, column=3, padx=10, pady=10)

        # Botones de función
        self.boton_igual = tk.Button(self.root, text="=", command=self.igual, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_igual.grid(row=3, column=0, padx=10, pady=10)

        self.boton_borrar = tk.Button(self.root, text="C", command=self.borrar, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_borrar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_retroceso = tk.Button(self.root, text="DEL", command=self.retroceso, width=5, font=self.font, bg="#cccccc", fg="#000000")
        self.boton_retroceso.grid(row=3, column=2, padx=10, pady=10)

    def config_modos(self):
        # Modo estándar
        self.modo_estandar = tk.Button(self.root, text="Modo Estándar", command=self.modo_estandar_func, width=15, font=self.font, bg="#cccccc", fg="#000000")
        self.modo_estandar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Modo claro
        self.modo_claro = tk.Button(self.root, text="Modo Claro", command=self.modo_claro_func, width=15, font=self.font, bg="#cccccc", fg="#000000")
        self.modo_claro.grid(row=4, column=2, columnspan=2, padx=10, pady=10)

        # Modo oscuro
        self.modo_oscuro = tk.Button(self.root, text="Modo Oscuro", command=self.modo_oscuro_func, width=15, font=self.font, bg="#cccccc", fg="#000000")
        self.modo_oscuro.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Modo nitidez
        self.modo_nitidez = tk.Button(self.root, text="Modo Nitidez", command=self.modo_nitidez_func, width=15, font=self.font, bg="#cccccc", fg="#000000")
        self.modo_nitidez.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

        # Modo moderno
        self.modo_moderno = tk.Button(self.root, text="Modo Moderno", command=self.modo_moderno_func, width=15, font=self.font, bg="#cccccc", fg="#000000")
        self.modo_moderno.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def suma(self):
        self.entrada.insert(tk.END, "+")

    def resta(self):
        self.entrada.insert(tk.END, "-")

    def multiplicacion(self):
        self.entrada.insert(tk.END, "*")

    def division(self):
        self.entrada.insert(tk.END, "/")

    def seno(self):
        self.entrada.insert(tk.END, "sin(")

    def coseno(self):
        self.entrada.insert(tk.END, "cos(")

    def tangente(self):
        self.entrada.insert(tk.END, "tan(")

    def logaritmo(self):
        self.entrada.insert(tk.END, "log(")

    def igual(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except Exception as e:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def borrar(self):
        self.entrada.delete(0, tk.END)

    def retroceso(self):
        self.entrada.delete(len(self.entrada.get())-1, tk.END)

    def modo_estandar_func(self):
        self.root.configure(bg="#f0f0f0")
        self.entrada.configure(bg="#ffffff", fg="#000000")
        self.boton_suma.configure(bg="#cccccc", fg="#000000")
        self.boton_resta.configure(bg="#cccccc", fg="#000000")
        self.boton_multiplicacion.configure(bg="#cccccc", fg="#000000")
        self.boton_division.configure(bg="#cccccc", fg="#000000")

    def modo_claro_func(self):
        self.root.configure(bg="#ffffff")
        self.entrada.configure(bg="#ffffff", fg="#000000")
        self.boton_suma.configure(bg="#ffffff", fg="#000000")
        self.boton_resta.configure(bg="#ffffff", fg="#000000")
        self.boton_multiplicacion.configure(bg="#ffffff", fg="#000000")
        self.boton_division.configure(bg="#ffffff", fg="#000000")

    def modo_oscuro_func(self):
        self.root.configure(bg="#000000")
        self.entrada.configure(bg="#000000", fg="#ffffff")
        self.boton_suma.configure(bg="#000000", fg="#ffffff")
        self.boton_resta.configure(bg="#000000", fg="#ffffff")
        self.boton_multiplicacion.configure(bg="#000000", fg="#ffffff")
        self.boton_division.configure(bg="#000000", fg="#ffffff")

    def modo_nitidez_func(self):
        self.root.configure(bg="#f0f0f0")
        self.entrada.configure(bg="#ffffff", fg="#000000", font=("Helvetica", 18))
        self.boton_suma.configure(bg="#cccccc", fg="#000000", font=("Helvetica", 18))
        self.boton_resta.configure(bg="#cccccc", fg="#000000", font=("Helvetica", 18))
        self.boton_multiplicacion.configure(bg="#cccccc", fg="#000000", font=("Helvetica", 18))
        self.boton_division.configure(bg="#cccccc", fg="#000000", font=("Helvetica", 18))

    def modo_moderno_func(self):
        self.root.configure(bg="#000000")
        self.entrada.configure(bg="#000000", fg="#ffffff", font=("Helvetica", 18))
        self.boton_suma.configure(bg="#000000", fg="#ffffff", font=("Helvetica", 18))
        self.boton_resta.configure(bg="#000000", fg="#ffffff", font=("Helvetica", 18))
        self.boton_multiplicacion.configure(bg="#000000", fg="#ffffff", font=("Helvetica", 18))
        self.boton_division.configure(bg="#000000", fg="#ffffff", font=("Helvetica", 18))

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = CalculadoraCientifica(root)
    root.mainloop()