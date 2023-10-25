#Ejercicio 1.34ç
#Inicio

#	num = 3
	
#	Escribe "Dime cuantos números debe tener la serie: "
#	Lee total

#	cont = 1
#	Mientras (cont <= total) hacer
#       Escribe num
#		Si (cont < total) entonces
#			Escribe " "
#		num = num + 3
#		cont = cont + 1
		
#Fin


num= 3
serie= int(input("Dime cuántos números dee tener la serie: "))
cont=1
while cont<= serie:
    print (num, end="")
    if cont<serie:
        print(" ", end="")
    num+=3
    cont+=1
print()