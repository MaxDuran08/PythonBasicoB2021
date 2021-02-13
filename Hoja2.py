print("Guarde contraseña")
contraseña1= input()
print("Ingrese contraseña")
contraseña2= input()

if contraseña1==contraseña2.lower() or contraseña1==contraseña2.upper():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")




print("Ingrese su nombre")
nombre=input()
print("Ingrese su sexo")
sexo= input()
if (nombre[0]=="n" or nombre[0]=="N") and (sexo=="hombre"):
    print("pertenece al grupo A")
else:
    if(nombre[0]=="L" or nombre.find[0]=="l") and (sexo=="mujer"):
        print("Pertenece al grupo A")
    else:
        print("pertenece al grupo B")