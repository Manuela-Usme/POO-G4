import tkinter as tk

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

def mostrar_resultado():
    try:
        nombre = entrada_nombre.get()
        salario_por_hora = float(entrada_salario_por_hora.get())
        horas_trabajadas = int(entrada_horas_trabajadas.get())

        empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
        salario_mensual = empleado.calcular_salario_mensual()

        if salario_mensual > 450000:
            etiqueta_resultado.config(text=f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual:.2f}")
        else:
            etiqueta_resultado.config(text=f"Nombre: {nombre}")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingrese valores válidos en los campos correspondientes.")

ventana = tk.Tk()
ventana.title("Cálculo de Salario Mensual")

tk.Label(ventana, text="Nombre del Empleado:").grid(row=0, column=0)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Salario por Hora:").grid(row=1, column=0)
entrada_salario_por_hora = tk.Entry(ventana)
entrada_salario_por_hora.grid(row=1, column=1)

tk.Label(ventana, text="Horas Trabajadas en el Mes:").grid(row=2, column=0)
entrada_horas_trabajadas = tk.Entry(ventana)
entrada_horas_trabajadas.grid(row=2, column=1)
boton_calcular = tk.Button(ventana, text="Calcular Salario", command=mostrar_resultado)
boton_calcular.grid(row=3, column=0, columnspan=2)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=2)

ventana.mainloop()
