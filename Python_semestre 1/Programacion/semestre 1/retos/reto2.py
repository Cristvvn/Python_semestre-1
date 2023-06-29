nombre=input("Escribe tu nombre: \n")
asignatura=input("¿Cual es tu asignatura?:\n")

lab1= float(input ("¿Cual fue tu primera nota de laboratorio?:\n"))
lab2= float(input("¿Cual fue tu segunda nota de laboratorio?:\n"))

prom_labs= (lab1 * 0.3) + (lab2 * 0.7)

print("Estudiante" ,nombre, "tu promedio de la asignatura" ,asignatura, "es" ,prom_labs,)

dic = {
"nombre_estudiante": nombre,
"nombre_asignatura": asignatura,
"lab1": lab1,
"lab2" : lab2,
"promedio": round(prom_labs, 1)
}
print(dic)