class Operaciones:
    """
    Clase para realizar operaciones y mostrar resultados.

    Attributes:
    - suma (float): El valor acumulado de la suma.
    - x (int): El valor de la variable x.
    - y (int): El valor de la variable y.
    """

    def __init__(self):
        """
        Inicializa un objeto de la clase Operaciones con valores predeterminados.
        """
        self.suma = 0
        self.x = 20
        self.y = 40

    def ejecutar_operaciones(self):
        """
        Realiza las operaciones especificadas y muestra los resultados parciales.
        """
        print("SUMA     X       Y")
        print(f"--{self.suma}--    --{self.x}--  --{self.y}--")

        self.suma = self.suma + self.x
        print(f"--{self.suma}--    --{self.x}--")

        self.x = self.x + self.y ** 2
        print(f"--{self.suma}--   {self.x}")

        self.suma = self.suma + self.x / self.y

    def imprimir_resultado(self):
        """
        Imprime el resultado final de las operaciones.
        """
        print(f"{self.suma}") 

operaciones = Operaciones()
operaciones.ejecutar_operaciones()
operaciones.imprimir_resultado()
