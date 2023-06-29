
grupo1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
grupo2 = {"Marcos", "Nicolás", "Diego", "Matias"}

ambos = grupo1.intersection(grupo2)

if len(ambos) > 0:
    print("Los siguientes estudiantes están en ambos grupos:")
    for i in ambos:
        print(i)
else:
    print("No hay estudiantes en común en ambos grupos.")
