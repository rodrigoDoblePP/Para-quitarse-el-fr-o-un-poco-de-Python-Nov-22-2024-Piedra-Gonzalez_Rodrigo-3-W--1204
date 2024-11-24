#Ejercicio 2
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

def mas_larga(lista):
    # Inicializamos palabra_mayor con la longitud de la primera palabra
    palabra_mayor = len(lista[0])
    # Inicializamos palabra_mostrar con la primera palabra de la lista
    palabra_mostrar = lista[0]

    # Recorremos la lista para comparar la longitud de cada palabra
    for palabra in lista:
        # Si encontramos una palabra más larga, actualizamos palabra_mostrar y palabra_mayor
        if palabra_mayor <= len(palabra):
            palabra_mostrar = palabra
            palabra_mayor = len(palabra)
        else:
            palabra_mostrar = palabra_mostrar

    # Imprimimos la palabra más larga
    print(palabra_mostrar)

# Lista de frases para probar la función
lista = ["Siento que merezco mas", "Ven", "¿Que vamos a hacer?"]
mas_larga(lista)
