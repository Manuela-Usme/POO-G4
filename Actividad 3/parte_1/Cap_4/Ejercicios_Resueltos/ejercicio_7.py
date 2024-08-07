import tkinter as tk

def comparar_numeros():
    try:
        # Obtener los valores de A y B ingresados por el usuario
        A = float(entrada_A.get())
        B = float(entrada_B.get())

        # Determinar la relación entre A y B
        if A > B:
            mensaje = "A es mayor que B"
        elif A < B:
            mensaje = "A es menor que B"
        else:
            mensaje = "A es igual a B"

        # Mostrar el mensaje resultante
        etiqueta_resultado.config(text=mensaje)
    except ValueError:
        # Manejar entradas no numéricas
        etiqueta_resultado.config(text="Por favor, ingrese números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Comparador de Números")

# Etiqueta y campo de entrada para A
tk.Label(ventana, text="Valor de A:").grid(row=0, column=0)
entrada_A = tk.Entry(ventana)
entrada_A.grid(row=0, column=1)

# Etiqueta y campo de entrada para B
tk.Label(ventana, text="Valor de B:").grid(row=1, column=0)
entrada_B = tk.Entry(ventana)
entrada_B.grid(row=1, column=1)

# Botón para realizar la comparación
boton_comparar = tk.Button(ventana, text="Comparar", command=comparar_numeros)
boton_comparar.grid(row=2, column=0, columnspan=2)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=3, column=0, columnspan=2)

# Iniciar la ventana principal
ventana.mainloop()
