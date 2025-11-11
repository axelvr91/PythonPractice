import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")

entrada = tk.Entry(ventana,width=28,  font=("Arial", 18), borderwidth=5, justify="right", bg="#D6D58E")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#Para hacer los botones de la calculadora necesitamos una lista


ventana.mainloop()

