#Ejercicio 7
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

# Lista para almacenar las edades ingresadas por el usuario
array = []

# Pedir al usuario que ingrese 10 edades
for x in range(10):  # 'range(10)' va de 0 a 9, que son 10 números
    edad = int(input("Escribe una edad: "))  # Convertir la entrada a entero
    array.append(edad)

# Contar cuántas edades son mayores o iguales a 20
cantidad = 0
for elemento in array:
    if elemento >= 20:
        cantidad += 1

# Mostrar la cantidad de personas con edades mayores o iguales a 20
print("Las  personas con edad mayor o igual a 20 son :", cantidad)
