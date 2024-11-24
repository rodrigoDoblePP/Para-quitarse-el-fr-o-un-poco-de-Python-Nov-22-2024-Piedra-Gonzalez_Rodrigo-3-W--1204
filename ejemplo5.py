#Ejercicio 5
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

# Solicita al usuario que ingrese un número binario
binario = input("Escribe un número binario: ")

# Inicializa la variable decimal a 0
decimal = 0

# Recorre cada dígito del número binario (desde el final)
for i in range(len(binario)):
    # Suma al valor decimal el valor de cada dígito binario multiplicado por 2 elevado a su posición
    decimal += int(binario[-(i + 1)]) * (2 ** i)

# Imprime el resultado en formato decimal
print(f"El número decimal es: {decimal}")

