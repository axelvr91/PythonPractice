#For loop
monday_temperatures = [9.1, 8.8, 7.6]
for temperature in monday_temperatures:
    print(temperature)

print("-----")
# el for permite iterar sobre una lista o cualquier otro tipo de colección 
# (tuplas, conjuntos, diccionarios, cadenas de texto, etc.) y ejecutar un 
# bloque de código para cada elemento en esa colección.

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

print("-----")
#otro ejemplo

colors02 = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors02:
    if isinstance(color, int):
        print(color)

#nota tambie se puede usar el type()

print("-----")

#otro ejemplo
colors03 = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for colore in colors03:
    if isinstance(colore, int) and colore > 50:
        print(colore)

# otro ejemplo, de tuplas 
datosAlazar = {"Juan", 25, "Ana", 30, "Pedro", 28}

for dato in datosAlazar.keys(): #.items() es un método que devuelve una vista de los pares clave-valor
    print(dato)                  #keys es un método que devuelve una vista de las claves del diccionario
                                #.values() devuelve una vista de los valores del diccionario

#esto permite iterar sobre cada par clave-valor en el diccionario y
#imprimirlos como tuplas.

for pair in datosAlazar.items():
    print(f"{pair}[0] tine la edad de {pair}[1] años")
#otra forma de hacerlo es desempaquetando las tuplas directamente en el bucle for


#ejemplo
diccionario={"John Smith":"+37682929928","Marry Simpons":"+423998200919"}
for datos, value in diccionario.items():
    print (f"{datos}:{value}")

#otro ejemplo
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for numbers11 in phone_numbers:
    phone_numbers[numbers11]= phone_numbers[numbers11].replace("+","00")
    print(phone_numbers[numbers11])