#Ejercicio 2.26
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
lista=input("Lista de la compra: ")
salto='\n'
listaseparada= lista.replace(", " , salto )
print(listaseparada)