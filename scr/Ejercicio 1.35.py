#Ejercicio 1.35
#Inicio

#	Escribe "Introduce dos números: "
#	Lee n1
#	Lee n2
	
#	opcion = 0
#	Mientras (opcion < 1 or opcion > 4) hacer
#		Escribe "Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "
#		Lee opcion
#		Si (opcion < 1 or opcion > 4) entonces
#			Escribe "Error - No es una opción correcta (1-4)"
#	
#	Segun (opcion) entonces
#		1:
#			Escribe n1 + " + " + n2 + " = " + (n1+n2)
#		2:
#			Escribe n1 + " - " + n2 + " = " + (n1-n2)
#		3:
#			Escribe n1 + " * " + n2 + " = " + (n1*n2)
#		4:
#			Si (n2 == 0) entonces
#				Escribe "La división por cero no es posible"
#			Sino
#				Escribe n1 + " / " + n2 + " = " + (n1/n2)
	
#Fin


num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))
opcion=int(input("Introduce una opción (1=Suma / 2=Resta / 3=Multiplicación / 4=División): "))

while opcion<1 or opcion>4 :
    print("Error - No es una opción correcta (1-4)")
    opcion=int(input("Introduce una opción (1=Suma / 2=Resta / 3=Multiplicación / 4=División): "))
       
if opcion == 1 :
    print(num1 , " + " , num2 , " = "  , num1+num2)
elif opcion == 2:
    print(num1 , " - " , num2 , " = " , num1-num2)
elif opcion == 3 :
    print(num1 , " * ", num2 , " = " , num1*num2)
elif opcion == 4:
    if num2==0 :
        print("La división por cero no es posible.")
    else :
        print(num1 ," / ", num2, " = " , num1/num2 )