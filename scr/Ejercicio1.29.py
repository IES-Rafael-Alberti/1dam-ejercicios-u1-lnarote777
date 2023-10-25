#Ejercicio 1.29

#Inicio
#   escribe ( introduzca su nombre)
#   escribe (introducza su edad (0-125)
#   lee nom , edad
#   tiempo = 125 - edad
#   si nom =="" entonces 
#       nom =desconocido
#   Mientras edad<0 and edad>125 hacer:
#       escribe (introduzca su edad: )
#   escribe ( "te llamas " nom " y tienes " edad " años, te quedan " tiempo "años por cumplir.")
#Fin


nom=str(input("Introduzca su nombre: "))
edad= int(input("Introduzca su edad (0-125): "))
tiempo=125-edad
if nom=="":
    nom="Desconocido"
while edad<0 and edad>125 :
    print("Introduzca una edad válida (0-125): ")
print("Te llamas ", nom ," y tienes ", edad, " años, te quedan " ,tiempo ,"años por cumplir.")

