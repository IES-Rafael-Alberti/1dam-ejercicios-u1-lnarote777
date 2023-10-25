#Ejercicio 1.5
# recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.

def importe(importesiniva , iva):
    importeiva= importesiniva * (iva/100+1)
    print(importeiva)

siniva=float(input("Importe sin iva del producto: "))
IVA=float(input("Tipo de iva (%): "))
importe(siniva, IVA)


