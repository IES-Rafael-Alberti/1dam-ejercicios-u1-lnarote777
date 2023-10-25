#Ejercicio2.11
#Escribir un programa que lea un entero positivo, n, introducido por el usuario 
#y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
#La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
print("Introduce un número entero positivo: ")
num=int(input())
suma=0
if num <= 0:
    print("Error, introduzca un número entero positivo:")
else:
    for i in range(1, num + 1):
        suma= num*(num+1)/2
    print("La suma de los primeros enteros hasta ", num , " es: ", suma)


#sin bucle
n=int(input("Introduce un numero entero positivo: "))
resultado=n*(n+1)/2
print("La suma de los primeros enteros hasta " , n, "es" , resultado )