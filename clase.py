import tkinter as tk 

def convertir():
    try:
        #obteniene el valor ingresado en el campo de entrada 
        kilometros = float(entrada_kilometros.get())

        #realizar la conversion a millas (1 kilometro = 0.621371 millas)
        millas=kilometros*0.621371

        #actualizar la etiqueta de reslutado
        etiqueta_resultado.config(text=f"{kilometros}kilometros son {millas}millas")
    except ValueError:
        #manejo de erorores para entrada no valiadas
        etiqueta_resultado.config(text="ingrese un valor numerico valido")
# crea la ventana principal
ventana=tk.Tk()
ventana.title("convettidor de kilometros a millas")
ventana.geometry("300x150") #establece el tamaño de la ventana

#crea  etiqueta de instrucciones y calcula la cuadricula
etiqueta_instrucion = tk.Label(ventana, text="ingrese la distancia en kilometros:")
etiqueta_instrucion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#crea campo de entrada y colocarla en la cuadricula
entrada_kilometros= tk.Entry(ventana)
entrada_kilometros.grid(row=1, column=0, padx=10, pady=10)

#crea boten de comvercion
boton_convertir=tk.Button(ventana, text="convertir", command=convertir)
boton_convertir.grid(row=1, column=1, padx=10, pady=10)

#crea etiqueta de resultado y colocaoa en la cuadricula
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

#inciar la aplicacion
ventana.mainloop()