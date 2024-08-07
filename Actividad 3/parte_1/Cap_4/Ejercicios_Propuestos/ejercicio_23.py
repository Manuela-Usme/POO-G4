import tkinter as tk
from tkinter import messagebox
import cmath

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        if self.a == 0:
            return "El valor de A no puede ser cero."
        
        discriminante = self.b ** 2 - 4 * self.a * self.c
        if discriminante > 0:
            raiz1 = (-self.b + discriminante**0.5) / (2 * self.a)
            raiz2 = (-self.b - discriminante**0.5) / (2 * self.a)
            return f"Raíces reales y distintas: {raiz1:.2f}, {raiz2:.2f}"
        elif discriminante == 0:
            raiz = -self.b / (2 * self.a)
            return f"Raíz doble: {raiz:.2f}"
        else:
            raiz1 = (-self.b + cmath.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - cmath.sqrt(discriminante)) / (2 * self.a)
            return f"Raíces complejas: {raiz1}, {raiz2}"

def mostrar_resultado():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        ecuacion = EcuacionCuadratica(a, b, c)
        resultado = ecuacion.calcular_soluciones()

        etiqueta_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese valores numéricos válidos.")

ventana = tk.Tk()
ventana.title("Solución de Ecuación Cuadrática")

tk.Label(ventana, text="Coeficiente A:").grid(row=0, column=0)
entrada_a = tk.Entry(ventana)
entrada_a.grid(row=0, column=1)

tk.Label(ventana, text="Coeficiente B:").grid(row=1, column=0)
entrada_b = tk.Entry(ventana)
entrada_b.grid(row=1, column=1)

tk.Label(ventana, text="Coeficiente C:").grid(row=2, column=0)
entrada_c = tk.Entry(ventana)
entrada_c.grid(row=2, column=1)

boton_calcular = tk.Button(ventana, text="Calcular Soluciones", command=mostrar_resultado)
boton_calcular.grid(row=3, column=0, columnspan=2)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=2)

ventana.mainloop()
