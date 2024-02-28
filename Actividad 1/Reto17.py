import math

class Circulo:
    def __init__(self, radio):
        """
        Constructor de la clase Circulo.

        Parámetros:
        - radio: float, radio del círculo.
        """
        self.radio = radio
        self.area = 0
        self.longitud_circunferencia = 0

    def calcular_area(self):
        """
        Calcula el área del círculo.
        """
        self.area = round(math.pi * (self.radio ** 2), 3)

    def calcular_longitud_circunferencia(self):
        """
        Calcula la longitud de la circunferencia del círculo.
        """
        self.longitud_circunferencia = round(2 * math.pi * self.radio, 3)

    def imprimir_resultados(self):
        """
        Imprime los resultados del área y la longitud de la circunferencia del círculo.
        """
        print(f"El área del círculo es: {self.area}")
        print(f"La longitud de la circunferencia es: {self.longitud_circunferencia}")


# Solicitar al usuario el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Crear una instancia de la clase Circulo con el radio proporcionado
circulo = Circulo(radio)

# Calcular el área y la longitud de la circunferencia del círculo
circulo.calcular_area()
circulo.calcular_longitud_circunferencia()

# Imprimir los resultados del área y la longitud de la circunferencia
circulo.imprimir_resultados()
