'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''


n = int(input("Ingresa un número entero: "))


binario = ""


if n == 0:
    binario = "0"


else:
    while n > 0:
        binario = str(n % 2) + binario  
        n = n // 2 


print(f"El número en binario es: {binario}")