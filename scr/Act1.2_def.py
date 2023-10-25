#Ejercico 2.2
# Recibe horas y coste y retorna el importe total.

def importe(a, b):
    return "Importe total: " + str(a*b)


a=int(input("Horas de trabajo: "))
b=int(input("Coste por horas: "))
print(importe(a, b))