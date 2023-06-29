def list():
    lista = []
    cantidad = int(input('Ingrese la cantidad de elementos de la lista: '))
    for i in range(cantidad):
        numero = float(input('Ingrese un número: '))
        lista.append(numero)
    return lista

def p(lista):
    print('La lista ingresada es:')
    for numero in lista:
        print(numero)

def multiplicar(lista1, lista2):
    r = []
    if len(lista1) == len(lista2) or len(lista1) != len(lista2):
        for i in range(len(lista1)):
            m= lista1[i] * lista2[i]
            r.append(m)
        return r

def dividir(lista1, lista2):
    re = []
    if len(lista1) == len(lista2) or len(lista1) != len(lista2):
        for i in range(len(lista1)):
            d= lista1[i] / lista2[i]
            re.append(d)
        return re

def promedio(lista1, lista2):
    combinadas = lista1 + lista2

    total = sum(combinadas)
    promedio = total / len(combinadas)
    return promedio

def mediana(list1, list2):
    combinadas = list1 + list2
    combinadas.sort()
    f = len(combinadas)
    if f % 2 == 0:
        med1 = combinadas[f // 2]
        med2 = combinadas[f// 2 - 1]
        mediana = (med1 + med2) / 2
    else:
        mediana = combinadas[f // 2]

    return mediana



print('##### Ingresar la primera lista #####')
lista1 = list()
print('\n')

print('##### Ingresar la segunda lista #####')
lista2 = list()
print('\n')

print('Listas ingresadas: \n')


print('##### Primera lista #####')
p(lista1)
print('\n')

print('##### Segunda lista #####')
p(lista2)
print('\n')

r = multiplicar(lista1, lista2)
re = dividir(lista1, lista2)
pr = promedio(lista1, lista2)
me = mediana(lista1, lista2)

print('El resultado de la multiplicación de las listas es:')
print(r)
print('\n')

print('El resultado de la division de las listas es: ')
print(re)
print('\n')

print('El promedio de las listas combinadas es:')
print(pr)
print('\n')

print('La mediana de las listas combinadas es:')
print(me)

#a. Función para multiplicar elementos de ambas listas
#b. Función para dividir elementos de ambas listas
#c. Función para obtener el promedio de ambas listas combinadas
#d. Función para obtener la mediana de ambas listas combinadas