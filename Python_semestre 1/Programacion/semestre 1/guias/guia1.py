####### Primer ejercicio #######

n1 = int(input ("ingrese 1 numero (solo contaran los enteros)\n"))
n2 = int(input ("ingrese 1 numero (solo contaran los enteros)\n"))
n3 = int(input ("ingrese 1 numero (solo contaran los enteros)\n"))

if n1!=n2 and n1!=n3 and n2!=n3:
 if n1>n2 and n1>n3:
    print("El primer numero es el mayor")
 else:
  if n2>n1 and n2>n3:
   print("el segundo numero es el mayor") 
  else:
    if n3>n2 and n3>n1:
       print("el tercer numero es el mayor")
else:
 print("Por favor ingrese numeros que sean diferentes entre si") 

 ###### Segundo ejercicio ########

p1 = input("ingrese una palabra:\n").lower()
p2 = input("ingrrese otra palabra:\n").lower()
if len (p1) > len(p2):
  print ("la palabra ",p1 ,"tiene mas caracteres")
elif len (p1) < len(p2):
   print ("la palabra",p2 ,"tiene mas caracteres")
else: 
   print("ambas palabras tienen la misma cantidad de caracteres")
###### tercer ejercicio #######

a= float(input("ingrese el lado a del triangulos\n"))
b= float(input("ingrese el lado b del triangulos\n"))
c= float(input("ingrese el lado c del triangulos\n"))
p = a+b+c
sp = p*0.5
area = (sp*(sp-a)*(sp-b)*(sp-c))**0,5
if a==b and b==c:
  print ("El triangulo es equilatero")
elif a==b or a==c or b==c:
   print ("El triangulo es isoceles")
else:
  print ("El triangulo es escaleno")
print("El area es de:",area)

##### Cuarto ejercicio ######

n1 = input("Ingrese el primer nombre: ")
n2 = input("Ingrese el segundo nombre: ")

if n1[0] == n2[0] and n1[-1] == n2[-1]:
 print("Ambos nombres comienzan y terminan con la misma letra")
else:
   if n1[0] == n2[0] and n1[-1] != n2[-1]:
      print("Ambos nombres comienzan con la misma letra.")
   else:
      if n1[-1] == n2[-1] and n1[0] != n2[0]:
         print("Ambos nombres terminan con la misma letra.")

###### Quinto ejercicio ######

n1=float(input("ingrese nota 1:\n"))
n2=float(input("ingrese nota 2:\n"))
n3=float(input("ingrese nota 3:\n"))

p = n1*0.3+n2*0.4+n3*0.3

if (p) < 4.0:
  print("el estudiante reprobo la asignatura")
if (p) <= 5.9 and (p) >= 4.0:
 print("el estudiante aprobo la asignatura")
if (p)>=6.0 and (p) <= 7.0:
   print("el alumno aprobo con distincion")
elif p>7.0:
   print("las notas exceden el maximo permitido")

###### Sexto ejercicio ######

g1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
g2 = {"Marcos", "Nicolás", "Diego", "Matias"}

r = g1.intersection(g2)

if len(r) >0:
    for e in r:
        print(e)
else:
 print("no hay estudiantes repetidos en ambos grupos")

###### Septimo ejercicio ######

name = () 
age = ()
worker1 = ()
worker2 = ()
worker3 = ()
worker4 = ()
worker5 = ()


print('\n#### INGRESO DATOS PRIMER TRABAJADOR ####\n')

namee = input("Nombre del primer trabajador: ")
name += (namee,)

while True:
    agee = int(input('Ingrese la edad del primer trabajador: '))
    if (agee < 0) or (agee > 150):
        continue
    else:
        age += (agee,)
        break

print('\n#### INGRESO DATOS SEGUNDO TRABAJADOR ####\n')


namee = input("Nombre del segundo trabajador: ")
name += (namee,)

while True:
    agee = int(input("Ingrese la edad del segundo trabajador: "))
    if (agee<0) and (agee>150):
       continue
    else:
      age +=(agee,)
      break

print('\n#### INGRESO DATOS TERCER TRABAJADOR ####\n')


namee = input("Nombre del tercer trabajador: ")
name += (namee,)

while True:
    agee = int(input("Ingrese la edad del tercer trabajador: "))
    if (agee<0) and (agee>150):
       continue
    else:
      age +=(agee,)
      break

print('\n#### INGRESO DATOS CUARTO TRABAJADOR ####\n')


namee = input("Nombre del cuarto trabajador: ")
name += (namee,)

while True:
    agee = int(input("Ingrese la edad del cuarto trabajador: "))
    if (agee<0) and (agee>150):
       continue
    else:
      age +=(agee,)
      break

print('\n#### INGRESO DATOS QUINTO TRABAJADOR ####\n')


namee = input("Nombre del quinto trabajador: ")
name += (namee,)

while True:
    agee = int(input("Ingrese la edad del quinto trabajador: "))
    if (agee<0) and (agee>150):
       continue
    else:
      age +=(agee,)
      break

worker1 += (name[0],age[0])
worker2 += (name[1],age[1])
worker3 += (name[2],age[2])
worker4 += (name[3],age[3])
worker5 += (name[4],age[4])
print(worker1)
print(worker2)
print(worker3)
print(worker4)
print(worker5)

###### OCTAVO EJERCICIO ######


a = input("ingrese un mes del año(1/12)")
meses= ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

if a in ("1","2","12"):
  estacion = "verano"
elif a in ("3","4","5"):
  estacion = "otoño"
elif a in ("6","7","8"):
  estacion = "invierno" 
elif a in ("9","10","11"):
  estacion = "primavera"
else:
  print("mes invalido")
print(f"el mes {meses[int(a)-1]} corresponde a {estacion}")

###### NOVENO EJERCICIO ######

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

numeros.pop()
numeros.insert(0, 2)
print(numeros)
sin_dup= (set(numeros))
print(sin_dup)
media = sum(numeros) / len(numeros)
print(media)
mediana = (min(numeros) + max(numeros)) /2
print(mediana)


###### DECIMO EJERCICIO ######

agenda = {
  'Nombre':'Cristian',
  'direccion':'Lynch',
  'ciudad':'osorno',
  'numero telefonico': '+56946805939'}
redes_sociales=  {'instagram':'cristvvn',
                  'facebook':'cristian leonardo',
                  'twitter':'cristian'}
print(redes_sociales['facebook'])

agenda.update(redes_sociales)
print(agenda)


##### EJERCICIO MATI ######

a=int(input("ingrese el lado del cuadrado"))
p = a*4
area = (a*a)
print("el area es de: ",area)
print(f"el perimetro es de: {p:.2f}")


# 5. Escribir un programa que permite capturar una cadena de caracteres e imprima 
# un diccionario con la cantidad de apariciones de cada palabra que existen en la 
# cadena. Por ejemplo, si recibe “Qué lindo día que hace hoy” , se deberá imprimir: 
# ‘que’: 2, ‘lindo’: 1, ‘día’: 1, ‘hace’: 1, ‘hoy’: 1.

cadena = str(input("oracion:\n")) 
c1 = cadena.split()

dict = {}

for i in c1:
  if i not in dict:
     
      count = c1.count(i)
      dict[i] = count
      
print(count)      
