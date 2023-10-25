#Ejercicio 2.12
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
#Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.
print("Introduzca su peso en kg: ")
peso = float(input())
print("Introduzca su altura en metros: ")
altura =float(input())
imc = peso / altura**2
print("Su indice de masa corporal es ", round(imc, 2 ))