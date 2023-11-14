#Ejercicio 2.4
#NO recibe parámetros y retorna la temperatura convertida en grados Celsius. 
#Dentro de la función se pedirá al usuario los grados Farenheit.
def temperatura():
    f=float(input("Tenperatura en Fahrenheit: "))
    x = (f - 32) * 5 / 9
    return "Temperatura en celsius: " + str(x)
 
print(temperatura())

