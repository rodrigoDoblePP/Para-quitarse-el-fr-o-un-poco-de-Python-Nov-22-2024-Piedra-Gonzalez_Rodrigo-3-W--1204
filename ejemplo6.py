#Ejercicio 6
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

# Solicitar datos al usuario
ano_curso = int(input("Escribe el año en curso: "))
nombre_uno = input("Primer nombre: ")
ano_uno = int(input("Primer año: "))
nombre_dos = input("Segundo nombre: ")
ano_dos = int(input("Segundo año: "))
nombre_tres = input("Tercer nombre: ")
ano_tres = int(input("Tercer año: "))

# Calcular cuántos años cumplen
cumple_uno = ano_curso - ano_uno
cumple_dos = ano_curso - ano_dos
cumple_tres = ano_curso - ano_tres

# Mostrar los resultados
print(nombre_uno + " cumplirá " + str(cumple_uno))
print(nombre_dos + " cumplirá " + str(cumple_dos))
print(nombre_tres + " cumplirá " + str(cumple_tres))
