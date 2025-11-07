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