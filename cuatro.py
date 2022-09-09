#crear menu empanadas
contador = 0

print("----- MENU -----")
print("1. Agregar Empanadas.")
print("2. Mostrar empanadas.")
print("3. SALIR.")

empanadas = []
while(contador != 3):
    empanada = {}
    ingredientes = []
    contador = int(input("Digita un opción: "))
    if(contador == 1):
        print("Agregar empanada")
        empanada['nombre'] = input("Nombre de la empanada: ")
        for i in range(3):
            ingredientes.append(input(f"Nombre del ingrediente {i+1}: "))
       
        empanada['ingredientes']=ingredientes
        empanada['precio']=int(input("Digite el valor: $"))
        empanadas.append(empanada)
    elif(contador == 2):
        print("Las empanadas disponibles son:")
        print(empanadas)
    elif(contador == 3):
        break
        print("Hasta pronto...")
    else:
        print("Opción invalida")