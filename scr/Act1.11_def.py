#Ejercicio 1.11
#Recibe un número y retorna una cadena de caracteres con el resultado de la función.

def resultado(num):
    total=n*(n+1)/2
    return "La suma de los primeros enteros hasta " + str(num) + " es " + str(total)


n=int(input("Introduce un numero entero positivo: "))
print(resultado(n))