class SumaNaturales:
    """
    Clase para sumar los primeros N números naturales.
    """

    def __init__(self):
        """
        Constructor de la clase SumaNaturales.
        Inicializa los atributos N y SUMA.
        """
        self.N = 0  # Cantidad de números naturales a sumar
        self.SUMA = 0  # Suma de los números naturales

    def leer_numero(self):
        """
        Método para leer la cantidad de números naturales a sumar desde la entrada estándar.
        """
        self.N = int(input("Ingrese la cantidad de números naturales a sumar: "))

    def sumar_naturales(self):
        """
        Método para sumar los primeros N números naturales.
        Imprime los números y la suma parcial en cada iteración.
        """
        self.SUMA = 0
        self.num = 1
        print("N        NUM         SUMA")
        while self.num <= self.N:
            self.SUMA += self.num
            print(f"{self.num:2}      --{self.num}--       --{self.SUMA}--")
            self.num += 1

    def imprimir_suma(self):
        """
        Método para imprimir el resultado de la suma de los números naturales.
        """
        print(f"{' ':>12} {self.num:2}       {self.SUMA:2}")


if __name__ == "__main__":
    suma = SumaNaturales()
    suma.leer_numero()
    suma.sumar_naturales()
    suma.imprimir_suma()
