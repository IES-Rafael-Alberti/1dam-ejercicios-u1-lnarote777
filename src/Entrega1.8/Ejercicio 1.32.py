#Ejercicio 1.32

#Inicio

#	Escribe "Introduce un número: "
#	Lee x
#	Escribe "Introduce otro: "
#	Lee y

#	Si (x >= y) entonces
#		numIni = x 
#		numFin = y
#	Sino
#		numIni = y
#		numFin = x
		
#	mientras (numIni<=numFin) hacer
#		Escribe numIni 
#		Si (numIni != numFin) entonces
#			Escribe "-"
#       numIni = numIni + 1

#Fin


x=int(input("Introduce un número: "))
y=int(input("Introduce otro: "))

if x >= y :
    numIni= y
    numFin = x
else:
    numIni = x
    numFin = y
    
while numIni <= numFin :
    print(numIni, end="")
    if numIni != numFin :
        print("-", end="")
    numIni+=1
