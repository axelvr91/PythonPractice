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
#conditionals#

def que_EsMayor ( a,b):
    print("Ingrese dos numeros para comparar cual es mayor")
    print("Ingrese el primer numero:")
    a=int(input())
    print("Ingrese el segundo numero:")
    b=int(input())

    resultado=0
    if a>b:
    
        resultado=a
        return resultado
    
    else:
        resultado=b
        return resultado
    
print("El numero mayor es:",que_EsMayor(0,0))

    


