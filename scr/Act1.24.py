#Ejercicio 2.24
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
#y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio=float(input("Precio del producto en euros (dos decimales): "))
euros=int(precio)
centimos=int((precio-euros)*100)
print("Nº de euros: ", euros)
print("Nº de céntimos: ", centimos)