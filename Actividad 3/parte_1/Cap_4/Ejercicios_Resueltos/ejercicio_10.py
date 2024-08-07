import tkinter as tk

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato
        self.matricula_base = 50000

    def calcular_pago_matricula(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            incremento = self.patrimonio * 0.03
        else:
            incremento = 0
        return self.matricula_base + incremento

def mostrar_resultado():
    try:
        # Obtener los valores ingresados por el usuario
        numero_inscripcion = entrada_numero_inscripcion.get()
        nombres = entrada_nombres.get()
        patrimonio = float(entrada_patrimonio.get())
        estrato = int(entrada_estrato.get())

        # Crear una instancia de Estudiante y calcular el pago de matrícula
        estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)
        pago_matricula = estudiante.calcular_pago_matricula()

        # Mostrar los resultados
        etiqueta_resultado.config(text=f"Número de inscripción: {numero_inscripcion}\n"
                                       f"Nombres: {nombres}\n"
                                       f"Pago de matrícula: ${pago_matricula:.2f}")
    except ValueError:
        # Manejar entradas no numéricas
        etiqueta_resultado.config(text="Por favor, ingrese valores válidos en los campos correspondientes.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Matrícula Universitaria")

# Campos de entrada para los datos del estudiante
tk.Label(ventana, text="Número de Inscripción:").grid(row=0, column=0)
entrada_numero_inscripcion = tk.Entry(ventana)
entrada_numero_inscripcion.grid(row=0, column=1)

tk.Label(ventana, text="Nombres:").grid(row=1, column=0)
entrada_nombres = tk.Entry(ventana)
entrada_nombres.grid(row=1, column=1)

tk.Label(ventana, text="Patrimonio:").grid(row=2, column=0)
entrada_patrimonio = tk.Entry(ventana)
entrada_patrimonio.grid(row=2, column=1)

tk.Label(ventana, text="Estrato Social:").grid(row=3, column=0)
entrada_estrato = tk.Entry(ventana)
entrada_estrato.grid(row=3, column=1)

# Botón para calcular el pago de matrícula
boton_calcular = tk.Button(ventana, text="Calcular Matrícula", command=mostrar_resultado)
boton_calcular.grid(row=4, column=0, columnspan=2)

# Etiqueta para mostrar los resultados
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=5, column=0, columnspan=2)

# Iniciar la ventana principal
ventana.mainloop()
