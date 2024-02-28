class Operaciones:
    def __init__(self, num):
        """
        Inicializa una instancia de la clase Operaciones.

        Parameters:
        - num: float - El número sobre el cual se realizarán las operaciones.
        """
        self.num = num
        self.cuadrado = 0
        self.cubo = 0

    def calcular_cuadrado(self):
        """
        Calcula el cuadrado del número almacenado en la instancia y lo asigna al atributo cuadrado.
        """
        self.cuadrado = self.num ** 2

    def calcular_cubo(self):
        """
        Calcula el cubo del número almacenado en la instancia y lo asigna al atributo cubo.
        """
        self.cubo = self.num ** 3

    def imprimir_resultados(self):
        """
        Imprime los resultados de las operaciones de cuadrado y cubo del número almacenado en la instancia.
        """
        print(f"El cuadrado de {self.num} es: {self.cuadrado}")
        print(f"El cubo de {self.num} es: {self.cubo}")


# Solicitar al usuario que ingrese un número
num = float(input("Ingrese un número: "))

# Crear una instancia de la clase Operaciones con el número ingresado
operaciones = Operaciones(num)

operaciones.calcular_cuadrado()
operaciones.calcular_cubo()

operaciones.imprimir_resultados()
