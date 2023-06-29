edad = 16

if edad >=18 :
    print('eres mayor de edad')
else:
    print('eres menor de edad\n')
    
print('#######\n')

edad = 19
print('usted puede votar'if edad >=18 else 'usted no puede votar\n')

print('#######\n')

num = 0
while num<=100:
 print(num)
 num+= 2

#####EJERCICIOS#####


num = int(input('Indique un número: '))

print(num,"es par" if (num % 2)== 0 else "es impar")

print('el numero es menor que 50' if num<50 else 'el numero es mayor que 50')
  
numero=num
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
 
print('El número', num,'no es primo'if contador >0 else  'es primo')


###################


num = (10)
while num<=30 and num>=10:
 print(num)
 num+= 2
print('#######SUMA#######')
suma = 0
for i in range(10,31, 2):
    suma+=i
    print(suma)
