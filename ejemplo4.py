#Ejercicio 4
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

cadena = input("Ingresa una cadena: ")
cantidad = 0

for letra in cadena:
    if letra.isupper():  # Verifica si la letra es mayúscula
        cantidad += 1

print("La cantidad de letras mayúsculas es:", cantidad)
