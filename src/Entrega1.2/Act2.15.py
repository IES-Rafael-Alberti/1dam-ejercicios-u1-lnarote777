#Ejercicio 2.15
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
#Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
capital=float(input("Cantidad depositada en cuenta de ahorros: "))
intereses=capital*(1+0.04)
año1= capital*intereses
año2= año1*intereses
año3=año2*intereses
print("Ahorros tras el primer año: ", round(año1,2))
print("Ahorros tras el segundo año: " , round(año2,2))
print("Ahorros tras el tercer año: ", round(año3,2))