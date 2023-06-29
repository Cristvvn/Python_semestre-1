nombre1= input ("¿Cual es el nombre del primer paciente?\n")
edad1= input(int("¿Cual es la edad del primer paciente?\n"))
peso1= input (float("¿Cual es el peso del primer paciente?\n"))
estatura1= input (float("¿Cual es la estatura del primer paciente?\n"))

tupla1=tuple(nombre1+edad1+peso1+estatura1)


nombre2= input ("¿Cual es el nombre del segundo paciente?\n")
edad2= input (int("¿Cual es la edad del segundo paciente?\n"))
peso2= input (float("¿Cual es el peso del segundo paciente?\n"))
estatura2= input (float("¿Cual es la estatura del segundo paciente?\n"))

tupla2=tuple(nombre2+edad2+peso2+estatura2)


nombre3= input ("¿Cual es el nombre del tercer paciente?\n")
edad3= input (int("¿Cual es la edad del tercer paciente?\n"))
peso3= input (float("¿Cual es el peso del tercer paciente?\n"))
estatura3= input (float("¿Cual es la estatura del tercer paciente?\n"))

tupla3=tuple(nombre3+edad3+peso3+estatura3)

tupla4=(tupla1+tupla2+tupla3)

print(tupla4)

###############################


patient_name = ()
patient_age = ()
patient_weight = ()
patient_height = ()

patient_1 = ()
patient_2 = ()
patient_3 = ()

#### PRIMER PACIENTE###

print('\n#### INGRESO DATOS PRIMER PACIENTE ####\n')

#NOMBRE
pat_name = input('Ingrese el nombre del primer paciente: ')
patient_name += (pat_name,)

# EDAD
while True:
    pat_age = int(input('Ingrese la edad del primer paciente: '))
    if (pat_age < 0) or (pat_age > 140):
        continue
    else:
        patient_age += (pat_age,)
        break

# PESO
while True:
    pat_wei = float(input('Ingrese el peso del primer paciente (Kg.): '))
    if (pat_wei < 0) or (pat_wei > 700):
        continue
    else:
        patient_weight += (pat_wei,)
        break

# ESTATURA
while True:
    pat_hei = int(input('Ingrese la estatura del primer paciente (Cm): '))
    if (pat_hei < 20) or (pat_hei > 300):
        continue
    else:
        patient_height += (pat_hei,)
        break

#### SEGUNDO PACIENTE###

print('\n#### INGRESO DATOS SEGUNDO PACIENTE ####\n')

#NOMBRE
pat_name = input('Ingrese el nombre del segundo paciente: ')
patient_name += (pat_name,)

# EDAD
while True:
    pat_age = int(input('Ingrese la edad del segundo paciente: '))
    if (pat_age < 0) or (pat_age > 140):
        continue
    else:
        patient_age += (pat_age,)
        break

# PESO
while True:
    pat_wei = float(input('Ingrese el peso del tercer paciente (Kg.): '))
    if (pat_wei < 0) or (pat_wei > 700):
        continue
    else:
        patient_weight += (pat_wei,)
        break

# ESTATURA
while True:
    pat_hei = int(input('Ingrese la estatura del tercer paciente (Cm): '))
    if (pat_hei < 20) or (pat_hei > 300):
        continue
    else:
        patient_height += (pat_hei,)
        break

#### TERCER PACIENTE###

print('\n#### INGRESO DATOS TERCER PACIENTE ####\n')

#NOMBRE
pat_name = input('Ingrese el nombre del tercer paciente: ')
patient_name += (pat_name,)

# EDAD
while True:
    pat_age = int(input('Ingrese la edad del tercer paciente: '))
    if (pat_age < 0) or (pat_age > 140):
        continue
    else:
        patient_age += (pat_age,)
        break

# PESO
while True:
    pat_wei = float(input('Ingrese el peso del tercer paciente (Kg.): '))
    if (pat_wei < 0) or (pat_wei > 700):
        continue
    else:
        patient_weight += (pat_wei,)
        break

# ESTATURA
while True:
    pat_hei = int(input('Ingrese la estatura del tercer paciente (Cm): '))
    if (pat_hei < 20) or (pat_hei > 300):
        continue
    else:
        patient_height += (pat_hei,)
        break

patient_1 += (patient_name[0],patient_age[0],patient_weight[0],patient_height[0])
patient_2 += (patient_name[1],patient_age[1],patient_weight[1],patient_height[1])
patient_3 += (patient_name[2],patient_age[2],patient_weight[2],patient_height[2])

print(patient_1)
print(patient_2)
print(patient_3)


#tupla_nums += (user_num,)