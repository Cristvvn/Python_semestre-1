estatura = 1.76
peso = 64.3
edad = 18
print(f"mi estatura es de {estatura} y mi peso es de {peso}")
int(peso)
float(edad)
imc = peso / (estatura**2)
print (f"mi imc es de;{imc}\n")
print ("mi imc es de :{:.2f}".format (imc))

asignatura = "programacion"
carrera = "ingenieria civil en informatica"

ampolleta = False
interruptor = True
print (ampolleta,interruptor)
print ("la variable ampolleta es de tipo;",type(interruptor),"\n")
print (bool(0))
print (bool(""))
print (bool(None))
print (bool("true"))
print (bool(0))
print (bool(1))
print ("\n")

####-LISTA-####
nueva_lista = list()
otra_lista = []
lista_mixta = {}
print ("esta es una lista vacia",nueva_lista)
print ("esta es otra lista vacia",otra_lista)
print (type(otra_lista))

lista = []
print("lista:")
estudiantes = ["Matias","Nelson","Cristian","Diego","Matias"]
num = [1,2,3,4,5,6]
Lenguaje = ["Python"]
data = ["Osorno", {"UV":"nivel bajo","Temp °C": 15}]


print("lista de cadena de caracteres",estudiantes)
print("lista de numeros",num)
print("lista de un elemento",Lenguaje)
print("lista mixta",lista_mixta)
print("esto igual es una lista",data)
print(len(lista_mixta))
print(estudiantes.count("Matias"))("\n")

print(estudiantes[0])
print(estudiantes[1])
print("posicion -2",estudiantes[-2])("\n")

data_asig = [10023,"programacion",1,True]
cod,ramo,semestre,estado = data_asig

print("suma de listas",estudiantes + num)

print(list("python"))
print(list(range(10,21)))
print("\n")

newtupla = tuple()



