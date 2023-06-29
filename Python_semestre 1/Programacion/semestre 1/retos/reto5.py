num = int(input("Ingrese un número:\n "))

i = num + 1

if num % 2 == 0:
    print ("Es numero par")
else:
    print ("Es numero impar")

if num % 2 == 1:
    print ("Es un numero primo")
elif num == 2:
    print("Es un numero primo")
else:
    print ("No es un numero primo")

    
if num > 50:
    print ("Es mayor a 50")
elif num == 50:
    print ("Es el mismo numero")
else:
    print ("Es menor a 50")