#Ejercicio 2.13
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS:
# "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.
n = int(input("Introduce el primer número entero: "))
m = int(input("Introduce el segundo número entero: "))
cociente = n//m
resto = n%m
print("La division entre " + str(n) + " y " + str(m) + " da un cociente de " + str(cociente) + " y resto " + str(resto))