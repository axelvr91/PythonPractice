import os

proyectos=["Video_Edicion","Fitness_App","Ecommerce_Ropa","Entrenamiento_Personal","Finanzas"]

for p in proyectos:
    #Verificar si la carpeta existe
    if not os.path.exists(p):
        os.makedirs(p)
        print("Carpeta creada:"+p)
    else:
        print("La carpeta "+ p + " ya existe")
        
     