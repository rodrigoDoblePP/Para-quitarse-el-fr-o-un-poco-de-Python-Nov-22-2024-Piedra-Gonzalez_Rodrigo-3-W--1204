#Ejercicio 8
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

# Creamos una lista vacía para almacenar los nombres
nombres = []

# Pedimos al usuario que ingrese 4 nombres
for x in range(1, 5):
    nombres.append(input("Ingresa un nombre: ").lower()) 

# Pedimos al usuario que ingrese la letra a buscar
letra_buscada = input("¿Qué letra estás buscando?: ").lower()  

# Inicializamos la variable cantidad para contar cuántos nombres contienen la letra buscada
cantidad = 0

# Recorremos la lista de nombres
for nombre in nombres:
    # Si la letra buscada está en el nombre, incrementamos la cantidad
    if letra_buscada in nombre:
        cantidad += 1

# Imprimimos el número de nombres que contienen la letra buscada
print(cantidad)

