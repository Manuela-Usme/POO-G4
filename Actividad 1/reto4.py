class Edades:
    """
    Clase para calcular la edad de la mamá de Juan, Alberto, Ana, a partir de la edad de sus hijos.

    Attributes:
    - edad_juan (int): La edad de Juan, proporcionada por el usuario.
    - edad_alberto (int): La edad de Alberto, calculada como 2/3 de la edad de Juan.
    - edad_ana (int): La edad de Ana, calculada como 4/3 de la edad de Juan.
    - edad_mama (int): La edad de la mamá, calculada como la suma de las edades de Juan, Alberto y Ana.
    """

    def __init__(self, edad_juan):
        """
        Inicializa un objeto Edades con la edad de Juan y otras edades inicializadas como None.

        Args:
        - edad_juan (int): La edad de Juan, proporcionada por el usuario.
        """
        self.edad_juan = edad_juan
        self.edad_alberto = None
        self.edad_ana = None
        self.edad_mama = None

    def calcular_edades(self):
        """
        Calcula las edades de Alberto, Ana y la mamá basadas en la edad de Juan.
        """
        self.edad_alberto = int((2 / 3) * self.edad_juan)
        self.edad_ana = int((4 / 3) * self.edad_juan)
        self.edad_mama = int(self.edad_juan + self.edad_alberto + self.edad_ana)

    def imprimir_edades(self):
        """
        Imprime las edades calculadas de Alberto, Juan, Ana y la mamá.
        """
        print("Edad de Alberto:", self.edad_alberto)
        print("Edad de Juan:", self.edad_juan)
        print("Edad de Ana:", self.edad_ana)
        print("Edad de la mamá:", self.edad_mama)

edad_juan = int(input("¿Cuál es la edad de Juan? "))
edades = Edades(edad_juan)
edades.calcular_edades() 
edades.imprimir_edades() 