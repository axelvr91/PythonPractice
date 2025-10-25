def mean(mylist):
    the_mean=sum(mylist) / len(mylist)
    return the_mean

print("Ejemplo 01",mean([1,4,5]))

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

def convert(amount):
    output=amount*502
    return output


print("Cuanto desea convertir?")
amount=float(input())
print("El valor seria:",convert(amount))


#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

def area_cuadrado(lado):
    area=lado*lado
    return area

print("Area del cuadrado:",area_cuadrado(7))

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

def converter(onz):
    mililitros=29.57353
    conversion=onz* mililitros
    return conversion

print(converter(5))

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#


