import tkinter as tk
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * (self.lado ** 2)

def calcular_triangulo():
    try:
        lado = float(entrada_lado.get())

        triangulo = TrianguloEquilatero(lado)
        perimetro = triangulo.calcular_perimetro()
        altura = triangulo.calcular_altura()
        area = triangulo.calcular_area()

        etiqueta_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
        etiqueta_altura.config(text=f"Altura: {altura:.2f}")
        etiqueta_area.config(text=f"Área: {area:.2f}")
    except ValueError:
        etiqueta_perimetro.config(text="Entrada inválida. Introduzca un número.")
        etiqueta_altura.config(text="")
        etiqueta_area.config(text="")

# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Triángulo Equilátero")

# Campo de entrada para el valor del lado
tk.Label(ventana, text="Valor del lado:").grid(row=0, column=0)
entrada_lado = tk.Entry(ventana)
entrada_lado.grid(row=0, column=1)

# Botón para calcular el perímetro, la altura y el área
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_triangulo)
boton_calcular.grid(row=1, column=0, columnspan=2)

# Etiquetas para mostrar los resultados
etiqueta_perimetro = tk.Label(ventana, text="")
etiqueta_perimetro.grid(row=2, column=0, columnspan=2)

etiqueta_altura = tk.Label(ventana, text="")
etiqueta_altura.grid(row=3, column=0, columnspan=2)

etiqueta_area = tk.Label(ventana, text="")
etiqueta_area.grid(row=4, column=0, columnspan=2)

# Iniciar la ventana principal
ventana.mainloop()
