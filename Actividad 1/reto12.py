class Trabajador:
    """
    Clase para representar y calcular el salario de un trabajador.

    Attributes:
    - NOM (str): Nombre del trabajador.
    - NHT (float): Número de horas trabajadas por el trabajador.
    - VHN (float): Valor de la hora normal de trabajo del trabajador.
    """

    def __init__(self):
        """
        Inicializa un objeto Trabajador con valores predeterminados.
        """
        self.NOM = ""
        self.NHT = 0
        self.VHN = 0

    def leer_datos(self):
        """
        Solicita al usuario que ingrese los datos del trabajador.
        """
        self.NOM = input("Ingrese el nombre del trabajador: ")
        self.NHT = float(input("Ingrese el número de horas trabajadas: "))
        self.VHN = float(input("Ingrese el valor de la hora normal de trabajo: "))

    def calcular_salario(self):
        """
        Calcula el salario del trabajador según las horas trabajadas y el valor de la hora normal.
        
        Returns:
        - float: El salario devengado por el trabajador.
        """
        if self.NHT > 40:
            HET = self.NHT - 40
            if HET > 8:
                HEE8 = HET - 8
                salario = 40 * self.VHN + 16 * self.VHN + HEE8 * 3 * self.VHN
            else:
                salario = 40 * self.VHN + HET * 2 * self.VHN
        else:
            salario = self.NHT * self.VHN

        return salario

    def mostrar_resultado(self):
        """
        Muestra el resultado del salario devengado por el trabajador.
        """
        salario = self.calcular_salario()
        print(f"EL TRABAJADOR {self.NOM} DEVENGO: ${salario}")

trabajador = Trabajador()
trabajador.leer_datos()
trabajador.mostrar_resultado()
