#Ejericicio 10

print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

def es_bisiesto(ano):
    # Verificamos si el año es divisible por 4
    if ano % 4 == 0:
        # Si el año es divisible por 100, debe ser también divisible por 400 para ser bisiesto
        if ano % 100 != 0 or ano % 400 == 0:
            print("Es bisiesto")
        else:
            print("No es bisiesto")
    else:
        print("No es bisiesto")

# Pedimos al usuario que ingrese un año para verificar si es bisiesto
ano = int(input("Escribe un año para saber si es bisiesto: "))
es_bisiesto(ano)
