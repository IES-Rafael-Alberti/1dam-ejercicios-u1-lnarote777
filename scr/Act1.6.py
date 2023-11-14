#Ejercicio 2.6
#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado 
#y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
print("Importe final: ")
precio = int(input())
iva=10
impSinIva= precio / 1.1
print("El precio sin IVA es ", impSinIva, " y se le aplica el ", iva, " %") 
