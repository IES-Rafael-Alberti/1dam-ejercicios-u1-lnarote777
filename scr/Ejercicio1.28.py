#Ejercicio 1.28

#Inicio
#   escribe (Introduce un número)
#   escribe (introduce otro)
#   lee n1 , n2
#   si n1 == n2 entonces:
#       escribir ( "Los números no pueden ser iguales".)
#   sino 
#       si n1<n2 entonces:
#           n3=n2-n1
#           escribe( "el numero menor es" n1 "y entre ellos existen" n3 " numeros enteros.")
#       sino:
#           n4= n1-n2
#           escribe ( "el numero menos es " n2 "y entre ellos existen " n4 "numeros enteros.")
#Fin



n1=int(input("Introduce un número entero: "))
n2=int(input("Introduce otro: "))
if n1 == n2 :
    print("Los números no pueden  ser iguales.")
elif n1 < n2 :
    n3 = n2 - n1
    print("El número menor es ", n1," y entre ellos existen ", n3, " números enteros.")
else:
    n2<n1
    n4=n1-n2
    print("El número menor es ", n2," y entre ellos existen ", n4, " números enteros.")
