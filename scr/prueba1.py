
def mayor(num1 , num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    elif num1 == num2:
        return 0

    
def main():   
    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))
    print(mayor(n1 , n2))

if __name__ == "__main__":
    main()