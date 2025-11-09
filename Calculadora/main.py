import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")

entrada = tk.Entry(ventana,width=400,  font=("Arial", 18), borderwidth=5, justify="right", bg="#D6D58E")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#Para hacer los botones de la calculadora necesitamos una lista

botones=[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3)
]

for (texto, fila, columna) in botones:
    tk.Button(ventana, text=texto, width=9, height=4, font=("Arial", 14)).grid(row=fila, column=columna),
    command=lambda t=texto: entrada.insert((tk.END, t)).grid(row=fila, column=columna, padx=5, pady=5)



ventana.mainloop()

