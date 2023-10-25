#Ejercicio 2.23
#Escribir un programa que pregunte el correo electrónico del usuario en la consola 
#y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
email=str(input("Ingrese su email: "))
correo= email.split("@")[0]
nuevoemail= correo + "@ceu.es"
print("Su nuevo email es: " , nuevoemail)