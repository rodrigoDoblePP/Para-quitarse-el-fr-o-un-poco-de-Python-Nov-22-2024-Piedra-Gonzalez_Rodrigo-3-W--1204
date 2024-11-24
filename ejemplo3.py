#Ejercicio 3
print (" ")
print ("Piedra Gonzalez Rodrigo 3-w 1204")
print (" ")

def filtrar_palabras(lista, n): # # Usamos una lista por comprensión para 
#filtrar las palabras cuya longitud sea mayor a n
    return [palabra for palabra in lista if len(palabra) > n]

# Ejemplo de uso
palabras = ["Siento que merezco mas", "Ven", "Nunca he sido honesto", "Mujeres", "programación"]
n = int(input("Escribe un número: "))
resultado = filtrar_palabras(palabras, n) ## Llamamos a la función para obtener las
# palabras que tienen más de 'n' caractere
print("Palabras con más de", n, "caracteres:", resultado) #Imprimimos resultado
