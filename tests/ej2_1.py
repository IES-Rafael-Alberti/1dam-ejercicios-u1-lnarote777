def pedirEdad():
    """Pedir la edad y comprobar que se trata de un número entero entre 1 y 125"""
    salir = False
    while not salir:
        entrada =input("Introduzca su edad: ")
        
        if entrada.isnumeric() and 0 < int(entrada) <= 125:
            salir = True
        else:
            print("***Error*** edad introducida no válida.")
            
    edad = int(entrada)        

    return edad
      
def mayorEdad():
      
      
          
            
def main():
    edad = pedirEdad()
    
    if mayorEdad(edad):
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")