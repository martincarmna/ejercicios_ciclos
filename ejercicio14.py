cantidad = int(input("Ingresa la cantidad de números primos a mostrar: "))


num = 2  
contador = 0  


while contador < cantidad:
    es_primo = True
    
    
    for i in range(2, int(num ** 0.5) + 1):
        
        if num % i == 0:
            es_primo = False
            break
    
    
    if es_primo:
        print(num)
        contador += 1
    
    
    num += 1