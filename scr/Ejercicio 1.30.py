# Ejercico 1.30

#Inicio
#   escribe ("Dame un numero:")
#   escribe ("Cuanto se incrementa: ")
#   escribe ("¿Total de la serie? ")
#   lee num, incremento, serie
#   mientras (num<0 and incremento<0 ) hacer
#       escribe (" Vuelva a introducir el incremento ")
#       escribe(" vuelva a introducir el total de la serie ")
#   cont = 1
#   mientras (cont <= serie) hacer 
#       num = num + incremento
#       cont = cont + 1
#       si (cot < (serie - 1)) entonces
#           frase = frase + num + ".."
#       sino
#           frase =frase + num + "-"
#   escribe ("frase")
#Fin



num=int(input("Dame un número: "))
incremento=int(input("Dame un incremento: "))
serie=int(input("¿Hata qué numero dura la serie? "))
while incremento < 0 or serie < 0 :
    print("Vuelve a introducir el incremento (mayor que 0): ")
    incremento=input()
    print("Vuelve a introducir el numero de la serie (mayor que 0): ")
    serie=input()
frase= "SERIE => " + str(num) + "-"
cont=1
while cont<serie :
    num += incremento
    cont += 1
    if cont< (serie - 1) :
        frase += str(num) + ".."
    else:
        if cont== serie: 
            frase += str(num)
        else:
            frase += str(num) + "-"
print(frase)