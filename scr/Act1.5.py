#Ejercicio 2.5
#Escribe un programa que pida el importe sin IVA de un artículo 
#y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
importesiniva=float(input("Importe sin iva del producto: "))
iva=float(input("Tipo de iva (%): "))
importeiva= importesiniva * (iva/100+1)
print(importeiva)