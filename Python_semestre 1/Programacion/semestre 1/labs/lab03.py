print('##### PRIMER EJERCICIO #####\n')


direccion12={'Nombre':'Magallanes',
             'Superficie':'1.382.291',
             'Habitantes ':'166.533'}
direccion14={'Nombre':'Los Ríos',
             'Superficie':'18.429',
             'Habitantes':'404.432'}
densidad12 = (166533/1382291)
densidad14 = (404432/18429)


capital12 = {'capital':'valdivia'}
capital14 = {'capital':'Punta arenas'}
comunas12 ={'Comunas':'Río Bueno, La Unión, Paillaco'}
comunas14 ={'Comunas':'Cabo de Hornos, Puerto Williams,Porvenir'}   
provincia12= {'provincias': 'Ranco, Valdivia'}
provincia14 = {'provincias': 'Antártica Chilena, Magallanes, Tierra delFuego, Última Esperanza'}

direccion12.update(capital12),direccion12.update(comunas12),direccion12.update(provincia12)
direccion14.update(capital14),direccion14.update(comunas14),direccion14.update(provincia14)

print ("ID 12", direccion12)
print(f'la densidad de Magallanes es de {densidad12:.1f}''\n')
print ('\n')
print ("ID 14",direccion14,)
print(f'la densidad de Los Rios es de {densidad14:.1f}''\n')

print('##### SEGUNDO EJERCICIO #####\n')

print('Se tiene las siguientes tres listas de números enteros: ')
a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
print(a)
print(b)
print(c)
print('\n')

print('Concatenar todas las listas e imprimir la lista obtenida.')
all = a + b + c
print(all,'\n')

print('Agregar el número 20 en la penúltima posición de la lista.')
all.insert(-1, 20)
print(all,'\n')

print('Ordenar la lista de forma descendente.')
all.sort(reverse=True)
print(all,'\n')

print('Insertar la lista [4,5,6] en la última posición de la lista ordenada')
all.insert(16, 4)
all.insert(17, 5)
all.insert(18, 6)
print(all,'\n')

print('Sumar todos los números dentro de la lista.')
suma = sum(all)
print(suma,'\n')

print('Obtener el promedio simple de la lista')
promedio = sum(all) / len(all)
print(promedio,'\n')