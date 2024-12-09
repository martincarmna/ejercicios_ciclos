'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
limite = int(input("Cuantos numeros quieres escribir: "))
menor = 0
igual = 0
mayor = 0
for i in range(1,limite + 1):
    n = int(input(f"Escribe el numero {i}: "))
    
    if n > 0:
        mayor += 1
    elif n < 0:
        menor += 1
    else:
        igual += 1
        
print(f"De los numeros introducidos {mayor} son mayores que 0")
print(f"De los numeros introducidos {menor} son menores que 0")
print(f"De los numeros introducidos {igual} son iguales a 0")