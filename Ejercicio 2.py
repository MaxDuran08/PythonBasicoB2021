entero = int(print("Ingrese un entero mayor o igal a 2.")) 
 
p=entero 
 
while entero % p !=0: 
    p+=1 
if p==entero: 
    print("El numero "+str(entero)+" es primo") 
else: 
    print("El numero "+str(entero)+" no es primo")