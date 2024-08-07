import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        lado = math.sqrt((self.diagonal_mayor / 2)**2 + (self.diagonal_menor / 2)**2)
        return 4 * lado

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura, lado_izquierdo, lado_derecho):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado_izquierdo = lado_izquierdo
        self.lado_derecho = lado_derecho

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return self.base_mayor + self.base_menor + self.lado_izquierdo + self.lado_derecho

class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")

        # Variables de entrada
        self.figura = tk.StringVar()
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()
        self.valor3 = tk.StringVar()
        self.valor4 = tk.StringVar()

        # Widgets de la interfaz
        tk.Label(root, text="Seleccione la figura:").grid(row=0, column=0, sticky="w")
        self.figuras_menu = tk.OptionMenu(root, self.figura, "Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo", "Rombo", "Trapecio", command=self.actualizar_entradas)
        self.figuras_menu.grid(row=0, column=1, sticky="w")

        self.label_valor1 = tk.Label(root, text="Radio/Base:")
        self.label_valor1.grid(row=1, column=0, sticky="w")
        self.entry_valor1 = tk.Entry(root, textvariable=self.valor1)
        self.entry_valor1.grid(row=1, column=1, sticky="w")

        self.label_valor2 = tk.Label(root, text="Altura:")
        self.label_valor2.grid(row=2, column=0, sticky="w")
        self.entry_valor2 = tk.Entry(root, textvariable=self.valor2)
        self.entry_valor2.grid(row=2, column=1, sticky="w")

        self.label_valor3 = tk.Label(root, text="")
        self.label_valor3.grid(row=3, column=0, sticky="w")
        self.entry_valor3 = tk.Entry(root, textvariable=self.valor3)
        self.entry_valor3.grid(row=3, column=1, sticky="w")

        self.label_valor4 = tk.Label(root, text="")
        self.label_valor4.grid(row=4, column=0, sticky="w")
        self.entry_valor4 = tk.Entry(root, textvariable=self.valor4)
        self.entry_valor4.grid(row=4, column=1, sticky="w")

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=5, column=0, columnspan=2)

        self.resultado = tk.Label(root, text="")
        self.resultado.grid(row=6, column=0, columnspan=2)

    def actualizar_entradas(self, seleccion):
        if seleccion == "Círculo":
            self.label_valor1.config(text="Radio:")
            self.label_valor2.grid_remove()
            self.entry_valor2.grid_remove()
            self.label_valor3.grid_remove()
            self.entry_valor3.grid_remove()
            self.label_valor4.grid_remove()
            self.entry_valor4.grid_remove()
        elif seleccion == "Rectángulo":
            self.label_valor1.config(text="Base:")
            self.label_valor2.config(text="Altura:")
            self.label_valor2.grid()
            self.entry_valor2.grid()
            self.label_valor3.grid_remove()
            self.entry_valor3.grid_remove()
            self.label_valor4.grid_remove()
            self.entry_valor4.grid_remove()
        elif seleccion == "Cuadrado":
            self.label_valor1.config(text="Lado:")
            self.label_valor2.grid_remove()
            self.entry_valor2.grid_remove()
            self.label_valor3.grid_remove()
            self.entry_valor3.grid_remove()
            self.label_valor4.grid_remove()
            self.entry_valor4.grid_remove()
        elif seleccion == "Triángulo Rectángulo":
            self.label_valor1.config(text="Base:")
            self.label_valor2.config(text="Altura:")
            self.label_valor2.grid()
            self.entry_valor2.grid()
            self.label_valor3.grid_remove()
            self.entry_valor3.grid_remove()
            self.label_valor4.grid_remove()
            self.entry_valor4.grid_remove()
        elif seleccion == "Rombo":
            self.label_valor1.config(text="Diagonal Mayor:")
            self.label_valor2.config(text="Diagonal Menor:")
            self.label_valor2.grid()
            self.entry_valor2.grid()
            self.label_valor3.grid_remove()
            self.entry_valor3.grid_remove()
            self.label_valor4.grid_remove()
            self.entry_valor4.grid_remove()
        elif seleccion == "Trapecio":
            self.label_valor1.config(text="Base Mayor:")
            self.label_valor2.config(text="Base Menor:")
            self.label_valor3.config(text="Altura:")
            self.label_valor4.config(text="Lado Izquierdo y Derecho:")
            self.label_valor2.grid()
            self.entry_valor2.grid()
            self.label_valor3.grid()
            self.entry_valor3.grid()
            self.label_valor4.grid()
            self.entry_valor4.grid()

    def calcular(self):
        figura = self.figura.get()
        try:
            if figura == "Círculo":
                radio = float(self.valor1.get())
                circulo = Circulo(radio)
                area = circulo.calcular_area()
                perimetro = circulo.calcular_perimetro()
                resultado = f"Área: {area:.2f}, Perímetro: {perimetro:.2f}"
            elif figura == "Rectángulo":
                base = float(self.valor1.get())
                altura = float(self.valor2.get())
                rectangulo = Rectangulo(base, altura)
                area = rectangulo.calcular_area()
                perimetro = rectangulo.calcular_perimetro()
                resultado = f"Área: {area:.2f}, Perímetro: {perimetro:.2f}"
            elif figura == "Cuadrado":
                lado = float(self.valor1.get())
                cuadrado = Cuadrado(lado)
                area = cuadrado.calcular_area()
                perimetro = cuadrado.calcular_perimetro()
                resultado = f"Área: {area:.2f}, Perímetro: {perimetro:.2f}"
            elif figura == "Triángulo Rectángulo":
                base = float(self.valor1.get())
                altura = float(self.valor2.get())
                triangulo = TrianguloRectangulo(base, altura)
                area = triangulo.calcular_area()
                perimetro = triangulo.calcular_perimetro()
                resultado = f"Área: {area:.2f}, Perímetro: {perimetro:.2f}"
            elif figura == "Rombo":
                diagonal_mayor = float(self.valor1.get())
                diagonal_menor = float(self.valor2.get())
                rombo = Rombo(diagonal_mayor, diagonal_menor)
                area = rombo.calcular_area()
                perimetro = rombo.calcular_perimetro()
                resultado = f"Área: {area:.2f}, Perímetro: {perimetro:.2f}"
            elif figura == "Trapecio":
                base_mayor = float(self.valor1.get())
                base_menor = float(self.valor2.get())
                altura = float(self.valor3.get())
                lado_izquierdo = float(self.valor4.get().split()[0])
                lado_derecho = float(self.valor4.get().split()[1])
                trapecio = Trapecio(base_mayor, base_menor, altura, lado_izquierdo, lado_derecho)
                area = trapecio.calcular_area()
                perimetro = trapecio.calcular_perimetro()
                resultado = f"Área: {area:.2f}, Perímetro: {perimetro:.2f}"
            else:
                resultado = "Por favor, seleccione una figura válida."
        except ValueError:
            resultado = "Error: Por favor, ingrese valores numéricos válidos."

        self.resultado.config(text=resultado)

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazFiguras(root)
    root.mainloop()
