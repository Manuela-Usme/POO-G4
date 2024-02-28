class Empresa:
    """
    Clase que gestiona los salarios de los vendedores de una empresa con base a las ventas de los departamentos.
    """

    def __init__(self):
        """
        Constructor de la clase Empresa.
        Se inicializa todas las variables necesarias.
        """
        self.VD1 = 0  # Ventas del departamento 1
        self.VD2 = 0  # Ventas del departamento 2
        self.VD3 = 0  # Ventas del departamento 3
        self.SALAR = 0  # Salario de los vendedores
        self.SALAR1 = 0  # Salario de los vendedores del departamento 1
        self.SALAR2 = 0  # Salario de los vendedores del departamento 2
        self.SALAR3 = 0  # Salario de los vendedores del departamento 3
        self.TOTVEN = 0  # Total de ventas de la empresa
        self.PORVEN = 0  # Porcentaje de ventas totales

    def leer_datos(self):
        """
        Método para leer los datos de entrada desde el usuario.
        """
        self.VD1 = int(input("Ventas del departamento 1: "))
        self.VD2 = int(input("Ventas del departamento 2: "))
        self.VD3 = int(input("Ventas del departamento 3: "))
        self.SALAR = float(input("Salario de los vendedores: "))

    def calcular_salarios(self):
        """
        Método para calcular los salarios de los vendedores con base a las ventas de los departamentos.
        """
        self.TOTVEN = self.VD1 + self.VD2 + self.VD3
        self.PORVEN = 0.33 * self.TOTVEN

        if self.VD1 > self.PORVEN:
            self.SALAR1 = self.SALAR + 0.2 * self.SALAR
        else:
            self.SALAR1 = self.SALAR

        if self.VD2 > self.PORVEN:
            self.SALAR2 = self.SALAR + 0.2 * self.SALAR
        else:
            self.SALAR2 = self.SALAR

        if self.VD3 > self.PORVEN:
            self.SALAR3 = self.SALAR + 0.2 * self.SALAR
        else:
            self.SALAR3 = self.SALAR

    def mostrar_salarios(self):
        """
        Método para mostrar los salarios calculados.
        """
        print(f"SALARIO VENDEDORES DEPTO. 1: {self.SALAR1}")
        print(f"SALARIO VENDEDORES DEPTO. 2: {self.SALAR2}")
        print(f"SALARIO VENDEDORES DEPTO. 3: {self.SALAR3}")
        print(f"TOTAL DE VENTAS DE LA EMPRESA: {self.TOTVEN}")
        print(f"PORCENTAJE DE VENTAS TOTALES: {self.PORVEN}")

empresa = Empresa()
empresa.leer_datos()
empresa.calcular_salarios()
empresa.mostrar_salarios()
