#####EJERCICIO UNO#####

lista=("La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participacion democratica")

lista_sub1 = lista.split()

lista_sub2 = lista_sub1.count("Universidad") + lista_sub1.count("universidad")
lista_sub3= str(lista_sub2)

tupla=tuple(lista_sub3)
print(tupla)
print(type(tupla))



#####EJERCICIO DOS#####

i = sum(range(500,810,10))
print(i)

j = sum(range(456,396,-2))

print(j)

resultado= (i + j)

print(f"el resultado es: {resultado}")




#####EJERCICIO TRES#####

print("##### EJERCICIO 3 #####")

hora_diu=12000
hora_noct=16000

dom_diu= 14000
dom_noct=19000

empleado1={
    "Lunes":hora_noct,
    "Martes":hora_noct,
    "Miercoles":hora_noct,
    "Jueves":hora_diu,
    "Viernes":hora_diu
}

empleado1["Semanal1"]=(hora_diu+hora_diu+hora_noct+hora_noct+hora_noct)*10


empleado2={
    "Martes":hora_noct,
    "Miercoles":hora_noct,
    "Jueves":hora_noct,
    "Domingo":dom_diu
}

empleado2["Semanal2"]=(hora_noct+hora_noct+hora_noct+dom_diu)*10


empleado3={
    "Miercoles":hora_diu,
    "Jueves":hora_diu,
    "Viernes":hora_diu,
    "Sabado":hora_noct,
    "Domingo":dom_noct
}
empleado3["Semanal3"]=(hora_diu+hora_diu+hora_diu+hora_noct+dom_noct)*10

print(empleado1)
print(empleado2)
print(empleado3)




#####EJERCICIO CUATRO#####

while True:
    try:
        numero = int(input('Ingrese un numero entero: '))
        if numero < 1:
            print('Ingese un valor igual o mayor a 1.')
            continue
        else:
            break
    except ValueError:
        print('Ingese un numero valido.')
print()

# Gestiona la impresion de las lineas
own = 1
for i in range(numero):
    own_list = []
    edd_sum = 0
    j = 0

    # Realiza los calculos que se imprimiran por linea.
    while j <= i:
        edd_sum += own
        own_list.append(str(own))
        own += 2
        j += 1

    oxd_str = ' + '.join(own_list)

    print(f'{i+1}**3 = {edd_sum} ➜  {oxd_str} = {edd_sum}')




#####EJERCICIO CINCO#####

import random

rand_list = []

for i in range (0, 20):
    random_num = random.randint(40, 350)
    rand_list.append(random_num)
print(rand_list)

while True:
    try:
        num_user = int(input("Digite un numero entre 40 y 350:\n "))
        if num_user >= 40 and num_user <= 350:
            break
        print("Digite un valor igual o mayor a 40")
        continue
    except ValueError:
        print("Digite un numero valido")

if num_user not in rand_list:
    print("\nEl numero no se encuentra en la lista")
else:
    oc = rand_list.count(num_user)
    print("\nEl número se encuentra en la lista")
    print("El número aparece:", oc)




#####EJERCICIO SEIS#####

import time
for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            print (f"{horas:02}:{minutos:02}:{segundos:02}")
            time.sleep(1)    




#####EJERCICIO SIETE#####

facts = 1
facts_lista = []

while True:
    try:
        num = int(input("Digite un número entero: \n"))
        if num < 0:
            print("Digite un número entero positivo")
            continue
        else:
            break
    except:
        print('Ingresa un número valido')

if num == 0:
    print('El factorial de 0 es: 1')
    print('\n0! = 1')

else:
    for i in range(1, num+1):
        facts = facts * i

    for j in range(num, 0, -1):
        j = str(j)
        facts_lista.append(j)
    
    print('El factorial de', num, 'es:', facts)
    facts_list_str = ' * '.join(facts_lista)
    print(f'\n{num}! = {facts_list_str} = {facts}')
