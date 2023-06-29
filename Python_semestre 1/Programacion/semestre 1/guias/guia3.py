print('##### EJERCICIO UNO #####\n')

def cantidad():
    while True:
        try:
            num = (int(input("Digite la cantidad de números a ingresar: \n")))
            if num < 0:
                print ("Solamente se permiten números positivos")
                continue
            else:
                break
        except ValueError:
            print ("Digite solamente números")
            continue
    return num

def pedir(num):
    listaa = []
    for i in range(num):
        num = int(input("Ingrese un número: "))
        listaa.append(num)
    return listaa

def par(listaa):
    par = 0
    for i in listaa:
        if i % 2 == 0:
            par = par + i
    return par

def impar(listaa):
    impar = 0
    for i in listaa:
        if i % 2 != 0:
            impar = impar + i
    return impar
  
        
num = cantidad()
listaa= pedir(num)




print ("El resultado de la suma par es:",par(listaa))
print ("El resultado de la suma impar es:",impar(listaa))
print ("El resultado de la suma total es:",sum(listaa))

print('\n')



print('##### EJERCICIO DOS #####\n')

def names():
    names_list = []
    while True:
        try:
            name = (str(input("Introduce un nombre (o 'exit' para salir): ")))
            if name == 'exit':
                break
            elif name.isalpha() == False:
                print ("No se permiten números")
                continue
            else:
                name = name.replace(" ","")
                if name:
                    names_list.append(name)
        except: ValueError
    return names_list
    

def names_count(names_list):
    letters_total = 0
    for i in names_list:
       letters_total += len(i)
    return letters_total




names_list = names()
letters_total = names_count(names_list)

print ("La lista de nombres ingresados es la siguiente:",names_list)
print ("La cantidad de letras totales en la lista es de:",letters_total)
print('\n')


print('##### EJERCICIO TRES #####\n')

def year():
    while True:
        try:
            years = int(input("Introduzca un año: "))
            if years < 0: 
               print("Introduzca un año válido") 
               continue
            else:
               break
        except ValueError:
            print ("Ingrese un valor válido")
            continue
    return years

def leap_year(years):
    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        print ("Es un año bisiesto")
    else:
        print("No es un año bisiesto")
    return years



years = year()
(leap_year(years))

print('\n')

print('##### EJERCICIO CUATRO #####\n')

def product_mont():
    product_price = 0
    while True:
        try:
            product = int(input("Introduzca la cantidad de dinero que cuesta el producto: "))
            if product % 10 != 0:
                print('Ingrese un monto multiplo de 10.')
                continue
            if product < 0: 
               print("No puede ser un valor negativo") 
               continue
            elif product == 0:
                print("¿Cómo algo que se va a pagar puede valer $0 pesos?")
                continue
            else:
                product_price += product
                print ("El coste de su producto corresponde a: $", product_price ,)
                break
        except ValueError:
            print ("Ingrese un valor válido")
            continue
    return product_price

def change(product_price):
    while True:
        change = 0
        pay = (int(input("Ingrese el monto a pagar: ")))
        if pay % 10 != 0:
            print('Ingresa un monto multiplo de 10.')
            continue
        if pay < product_price:
            print ("No puedes pagar menos de lo que vale el producto")
        elif pay > product_price:
            change = pay - product_price
            break
        else:
            change = pay - product_price
            print("Al pagar el precio justo del producto no tienes vuelto")
            break
    return change

def change_dev(change):
    cash = [20000,10000,5000,2000,1000,500,100,50,10]
    cash_list = []
    aux = []
    for i in cash:
        if change // i > 0:
            aux.append(i)
            aux.append(change // i)
            cash_list.append(aux)
            change -= i * aux[1]
            aux = []
    return cash_list

def desglose(cash_list):
    for i in cash_list:
        print('>>',i[0], 'x', i[1])
            
    
product_price = product_mont()
vuelto = change(product_price)
cash_list = change_dev(vuelto)



print ("Su vuelto es de $",vuelto)
desglose(cash_list)

print('\n')

print('##### EJERCICIO CINCO #####\n')

def num_int():
    num_list = []
    while True:
        try:
            num = (int(input("Indique una cantidad de números que sean enteros y positivos (Para salir del programa use -1): ")))
            if num > 0:
                num_list.append(num)
                continue
            elif num == -1: 
                break
            else:
                print("Ingrese solo números positivos")
        except ValueError:
            print ("Ingrese solamente números")
            continue
    return num_list

def num_mayor(num_list):
    for i in num_list:
        max_num = max(num_list)
    return max_num

def suma_par(num_list):
    suma_par = 0
    for i in num_list:
        if i % 2 == 0:
            suma_par = suma_par + i
    return suma_par

def suma_impar(num_list):
    suma_impar = 0
    for i in num_list:
        if i % 2 != 0:
            suma_impar = suma_impar + i
    return suma_impar

def total_sum(num_list):
    suma_total = 0
    for i in num_list:
        suma_total = sum(num_list)
    return suma_total

def promedio(num_list):
    return sum(num_list)/len(num_list)

        

num_list = num_int()
prom = promedio(num_list)
suma_par(num_list)
suma_impar(num_list) 

print("La lista de números es la siguiente",num_list)
print("La suma de los pares es",(suma_par(num_list)))
print("La suma de los impares es",(suma_impar(num_list)))
print("La suma de todos los números es", (total_sum(num_list)))
print("El promedio de los números en la lista es de",round((promedio(num_list)),2))
print("El mayor de los ingresados corresponde a", (num_mayor(num_list)))

if num_mayor(num_list) > prom:
    print('El numero',(num_mayor(num_list)),'es MAYOR al promedio')
if num_mayor(num_list) < prom:
    print('El numero',(num_mayor(num_list)),'es MENOR al promedio')
if num_mayor(num_list) == prom:
    print('El numero' (num_mayor(num_list)),'es IGUAL al promedio')