#Ejercicio 2.16
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después 
#el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
#el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
barras=int(input("Barras no del día vendidas: "))
pandeldía=3.49 
descuento= 60
pannodia= pandeldía * 0.6
suma= barras * pannodia
print("Precio pan del día: ", pandeldía, "€")
print("Descuento aplicado por no ser del día: ", descuento, "%")
print("Coste total: ", suma, "€")