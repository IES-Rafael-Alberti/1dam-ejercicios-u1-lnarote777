#Ejercicio 2.20
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
#(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número 
#de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión
tlfempresa=str(input("Introduzca el nº de telefono (prefijo-teléfono-extensión) "))
telf= tlfempresa[4:13]
print("El nº de teléfono sin prefijo ni extensión es ", telf)