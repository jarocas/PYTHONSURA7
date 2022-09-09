''''
#Listar numeros pares

numerosPares = []
#Generar un ciclo while que de 10 vueltas

contador = 0
while(contador < 10):
    numero = int(input("Digita un número: "))
    if(numero % 2== 0):
        numerosPares.append(numero)
        contador=contador+1
    else:
        print("El número",numero," no es un número par...")

for observador in numerosPares:
    print(observador)
'''

#Variables con datos de diferente tipo

pueblo = {}
#Agregando atributos nuevos a un diccionario
pueblo ['nombre'] = "Marinilla"
pueblo['distancia'] = "30 km"
#agregar otro dato
pueblo2 = {}
pueblo2['nombre'] = "Santuario"
pueblo2['distancia'] = "20 km"

print(pueblo)
print(pueblo2)