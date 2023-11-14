#Ejercicio 2.27
#Escribir un programa que pregunte el nombre del un producto, su precio y un número de unidades
# y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 
#dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
name=str(input("Nombre del producto: "))
precio=float(input("Precio del producto: "))
unidades=int(input("Nº de unidades: "))
total=precio*unidades

print("{} {:09.2f} {:03d} {:011.2f}" .format(name, precio, unidades, total))