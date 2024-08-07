import tkinter as tk

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        return self.calcular_salario_bruto() * self.porcentaje_retencion / 100

    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() - self.calcular_retencion()

def calcular_salario_neto():
    codigo = entrada_codigo.get()
    nombres = entrada_nombres.get()
    horas_trabajadas = float(entrada_horas_trabajadas.get())
    valor_hora = float(entrada_valor_hora.get())
    porcentaje_retencion = float(entrada_porcentaje_retencion.get())

    empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion)
    salario_neto = empleado.calcular_salario_neto()

    etiqueta_resultado.config(text=f"Salario Neto: ${salario_neto:.2f}")

# Creación de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Calculadora de Salario Neto")

# Campos de entrada
tk.Label(ventana, text="Código del Empleado:").grid(row=0, column=0)
entrada_codigo = tk.Entry(ventana)
entrada_codigo.grid(row=0, column=1)

tk.Label(ventana, text="Nombres:").grid(row=1, column=0)
entrada_nombres = tk.Entry(ventana)
entrada_nombres.grid(row=1, column=1)

tk.Label(ventana, text="Horas Trabajadas:").grid(row=2, column=0)
entrada_horas_trabajadas = tk.Entry(ventana)
entrada_horas_trabajadas.grid(row=2, column=1)

tk.Label(ventana, text="Valor Hora:").grid(row=3, column=0)
entrada_valor_hora = tk.Entry(ventana)
entrada_valor_hora.grid(row=3, column=1)

tk.Label(ventana, text="Porcentaje Retención:").grid(row=4, column=0)
entrada_porcentaje_retencion = tk.Entry(ventana)
entrada_porcentaje_retencion.grid(row=4, column=1)

# Botón para calcular el salario neto
boton_calcular = tk.Button(ventana, text="Calcular Salario Neto", command=calcular_salario_neto)
boton_calcular.grid(row=5, column=0, columnspan=2)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=6, column=0, columnspan=2)

# Iniciar la ventana principal
ventana.mainloop()
