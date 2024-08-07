import tkinter as tk
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
        return math.sqrt(self.base**2 + self.altura**2)

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"

# Clase para la interfaz gráfica
class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geométricas")

        # Variables de entrada
        self.figura = tk.StringVar()
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()

        # Widgets de la interfaz
        tk.Label(root, text="Seleccione la figura:").grid(row=0, column=0, sticky="w")
        self.figuras_menu = tk.OptionMenu(root, self.figura, "Círculo", "Rectángulo", "Cuadrado", "Triángulo Rectángulo", command=self.actualizar_entradas)
        self.figuras_menu.grid(row=0, column=1, sticky="w")

        self.label_valor1 = tk.Label(root, text="Radio/Base:")
        self.label_valor1.grid(row=1, column=0, sticky="w")
        self.entry_valor1 = tk.Entry(root, textvariable=self.valor1)
        self.entry_valor1.grid(row=1, column=1, sticky="w")

        self.label_valor2 = tk.Label(root, text="Altura:")
        self.label_valor2.grid(row=2, column=0, sticky="w")
        self.entry_valor2 = tk.Entry(root, textvariable=self.valor2)
        self.entry_valor2.grid(row=2, column=1, sticky="w")

        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=3, column=0, columnspan=2)

        self.resultado = tk.Label(root, text="")
        self.resultado.grid(row=4, column=0, columnspan=2)

    def actualizar_entradas(self, seleccion):
        if seleccion == "Círculo" or seleccion == "Cuadrado":
            self.label_valor1.config(text="Radio/Lado:")
            self.label_valor2.config(text="")
            self.entry_valor2.grid_remove()
        elif seleccion == "Rectángulo" or seleccion == "Triángulo Rectángulo":
            self.label_valor1.config(text="Base:")
            self.label_valor2.config(text="Altura:")
            self.entry_valor2.grid()

    def calcular(self):
        figura = self.figura.get()
        try:
            valor1 = float(self.valor1.get())
            valor2 = float(self.valor2.get()) if self.valor2.get() else None
        except ValueError:
            self.resultado.config(text="Por favor, ingrese valores numéricos válidos.")
            return

        if figura == "Círculo":
            circulo = Circulo(valor1)
            area = circulo.calcular_area()
            perimetro = circulo.calcular_perimetro()
            self.resultado.config(text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        elif figura == "Rectángulo":
            rectangulo = Rectangulo(valor1, valor2)
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()
            self.resultado.config(text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        elif figura == "Cuadrado":
            cuadrado = Cuadrado(valor1)
            area = cuadrado.calcular_area()
            perimetro = cuadrado.calcular_perimetro()
            self.resultado.config(text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        elif figura == "Triángulo Rectángulo":
            triangulo = TrianguloRectangulo(valor1, valor2)
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            tipo = triangulo.determinar_tipo_triangulo()
            self.resultado.config(text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}\nTipo: {tipo}")

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    interfaz = InterfazFiguras(root)
    root.mainloop()
