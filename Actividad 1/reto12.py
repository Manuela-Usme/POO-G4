class Empleado:
    """
    Clase para representar a un empleado y calcular su salario bruto, retención en la fuente y salario neto.
    """

    def __init__(self, horas_trabajadas, valor_hora):
        """
        Inicializa un objeto Empleado con las horas trabajadas y el valor por hora.
        
        Args:
        - horas_trabajadas (int): Número de horas trabajadas por el empleado.
        - valor_hora (float): Valor monetario de una hora de trabajo.
        """
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.salario_bruto = 0
        self.retencion_fuente = 0
        self.salario_neto = 0

    def calcular_salario_bruto(self):
        """
        Calcula el salario bruto multiplicando las horas trabajadas por el valor de la hora.
        """
        self.salario_bruto = self.horas_trabajadas * self.valor_hora

    def calcular_retencion_fuente(self):
        """
        Calcula la retención en la fuente, que corresponde al 12.5% del salario bruto.
        """
        self.retencion_fuente = 0.125 * self.salario_bruto 

    def calcular_salario_neto(self):
        """
        Calcula el salario neto restando la retención en la fuente al salario bruto.
        """
        self.salario_neto = self.salario_bruto - self.retencion_fuente

    def mostrar_resultados(self):
        """
        Muestra los resultados del cálculo del salario: salario bruto, retención en la fuente y salario neto.
        """
        print("Salario bruto del empleado:", self.salario_bruto)
        print("Retención en la fuente:", self.retencion_fuente)
        print("Salario neto del empleado:", self.salario_neto)


# Declarar constantes
horas_trabajadas = 48
valor_hora = 5000

# Instancia de la clase Empleado
empleado = Empleado(horas_trabajadas, valor_hora)

# Calcular salario bruto, retención en la fuente y salario neto
empleado.calcular_salario_bruto()
empleado.calcular_retencion_fuente()
empleado.calcular_salario_neto()

# Mostrar resultados
empleado.mostrar_resultados()
