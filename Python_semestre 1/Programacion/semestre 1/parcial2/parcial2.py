
print('##### EJERCICIO 1 #####\n')  

def w(p):
  p = p.lower() 
  p = p.replace(' ','') 
  inv = p [::-1] 

  if p == inv:
      return True 
  else:
      return False 

p = input('Ingrese una palabra: \n')

if w(p):
    print('La palabra',p,'es un palindromo.')
else:
    print('La palabra',p,'no es un palindromo.')

##### EJERCICIO 2 #####
print('##### EJERCICIO 2 #####\n')  

f = int(input('ingrese el numero de filas: \n')) 

for i in range(1, f +1):
    for j in range(f - i): 
        print(' ', end = '')
    for k in range (i , 2 * i):
        print(k % 10, end = '')
    for l in range (2 * i - 2, i - 1, -1): 
        print(l % 10, end = '')
        
    print()
    
##### EJERCICIO 3 #####
print('##### EJERCICIO 3 #####\n')  
  
min = {9, 5, 2, 7, 6, 1}
max = {12, 14, 11, 10, 15, 9}

if 9 in min and max: 
    print('La temperatura 9°C está presente en ambos sets.\n')
else:
    print('La temperatura 9°C no está presente en ambos sets.\n')
if 6 in min or 6 in max:
    print('La temperatura 6°C está presente en al menos uno de los sets.\n')
else:
    print('La temperatura 6°C no está presente en ninguno de los sets.\n')
if 17 in min or 17 in max:
    print('La temperatura 17°C está presente en al menos uno de los sets.\n')
else:
    print('La temperatura 17°C no está presente en ninguno de los sets.\n')

emin = {temp ** 4 for temp in min}
emax = {temp ** 4 for temp in max}

print("Temperaturas minimas elevadas a 4: ", emin, '\n')
print("Temperaturas maximas elevadas a 4: ", emax, '\n')

all = emin.union(emax)
print("Unión de ambos sets: ", all, '\n')
