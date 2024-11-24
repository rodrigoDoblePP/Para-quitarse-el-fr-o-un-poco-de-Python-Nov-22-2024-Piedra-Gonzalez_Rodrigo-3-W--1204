#Ejericio 9
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

def contar_vocales(palabra):
    # Convertimos la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
    palabra_min = palabra.lower()
    
    # Inicializamos las variables para contar las vocales
    cant_a = 0
    cant_e = 0
    cant_i = 0
    cant_o = 0
    cant_u = 0
    
    # Recorremos cada letra de la palabra
    for letra in palabra_min:
        # Incrementamos el contador correspondiente si la letra es una vocal
        if letra == "a":
            cant_a += 1
        elif letra == "e":
            cant_e += 1
        elif letra == "i":
            cant_i += 1
        elif letra == "o":
            cant_o += 1
        elif letra == "u":
            cant_u += 1

    # Imprimimos el conteo de cada vocal
    print("Hay " + str(cant_a) + " a")
    print("Hay " + str(cant_e) + " e")
    print("Hay " + str(cant_i) + " i")
    print("Hay " + str(cant_o) + " o")
    print("Hay " + str(cant_u) + " u")

# Pedimos al usuario que ingrese una palabra
palabra = input("Escribe una palabra: ")
contar_vocales(palabra)
