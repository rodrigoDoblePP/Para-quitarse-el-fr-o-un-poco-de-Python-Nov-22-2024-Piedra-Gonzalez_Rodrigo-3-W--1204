print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

#Ejercicio 1

def max_in_list(lista):
    # Inicializamos la variable numero_mayor con el primer valor de la lista
    numero_mayor = lista[0]

    # Recorremos la lista para comparar cada número con el actual numero_mayor
    for numero in lista:
        # Si encontramos un número mayor o igual al numero_mayor, lo actualizamos
        if numero_mayor <= numero:
            numero_mayor = numero
        else:
            # Si no, mantenemos el valor de numero_mayor 
            numero_mayor = numero_mayor
    
    # Imprimimos el número mayor encontrado
    print(numero_mayor)

# Lista de números para probar la función
lista = [1, 90, 69, 91, 54, 69, 5, 8, 0]

# Llamamos a la función con la lista
max_in_list(lista)
