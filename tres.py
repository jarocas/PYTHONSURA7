#crear un menú de opciones
contador = 0

print("Enamorate de Antioquia")
print("***** MENU *****")
print("1. Agregar pueblos")
print("2. Mostrar rutas")
print("3. Salir")
pueblos = []
while(contador != 3):
    pueblo = {}
    contador = int(input("Digita una opción: "))
    if(contador == 1):
        print("Agregar un pueblo")
        pueblo['nombre'] = input("Ingrese el nombre del pueblo: ")
        pueblo['distancia'] = int(input("Ingrese la diatncia del pueblo: "))
        pueblo['poblacion'] = int(input("Ingrese la población del pueblo: "))
        pueblos.append(pueblo)
    elif(contador == 2):
        print("Mostando Rutas")
        print(pueblos)
        
    elif(contador == 3):
        print("Saliendo...")
        break
    else:
        print("Opcion inválida")