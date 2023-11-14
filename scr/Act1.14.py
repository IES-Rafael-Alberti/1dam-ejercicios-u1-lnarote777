#Ejercicio 2.14
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
#muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
nºpayasos=int(input("Número de payasos del último pedido: "))
nºmuñecas=int(input("Número de muñecas del último pedido: "))
totalpayasos= nºpayasos*112
totalmuñecas=nºmuñecas*75
sumatotal= totalpayasos+totalmuñecas
print("El peso total del paquete es: ", sumatotal)