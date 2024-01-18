import os
# #Declara
# numeros = [] #Lista vacia
# #Obtener longitud
# print(len(numeros))
# print(type(numeros))
# #Agregar elemento lista
# numeros.append(1)
# print(numeros)
# #acceder elemento lista
# print(numeros[0])
# #Modificar elemento
# numeros[0] = 20
# print(numeros[0])
# #Eliminar elemento
# numeros.pop(0)
# print(len(numeros))
# #Inicializar
os.system('cls')
frutas = ["Manzana","Pera","Pera"]
frutas.insert(0,"Uvas")
print(frutas.index("Manzana"))
eliminar = input("Ingrese el nombre de la fruta a borrar :")
#frutas.pop(frutas.index(eliminar))
#Acceder valores
for item in frutas:
    print(item)

# for i,item in enumerate(frutas):
#     if (eliminar == item):
#         frutas.remove(eliminar)
os.system('cls')
tem = []
for item in frutas:
    if (eliminar != item):
        tem.append(item)
frutas = tem
for item in frutas:
    print(item)