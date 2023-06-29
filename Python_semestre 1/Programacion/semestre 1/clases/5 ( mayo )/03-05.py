ciudades = ["santiago","Temuco","osorno","Punta arenas"]
ICA = ["134","99","245","50"]
minimo = ciudades[ICA.index(min(ICA))]
maximo = ciudades[ICA.index(max(ICA))]
print(f"La ciudad con mejor calidad de aire es:", minimo)
print(f"La ciudad con peor calidad de aire es:", maximo)

for i in range(len[ciudades]):
    if ICA[i]>= 0 and ICA[i]<=50:
        print(ciudades[i],"tiene un indice de calidad de aire BUENO")
    elif ICA[i]>= 51 and ICA[i]<=100:
        print(ciudades[i],"tiene un indice de calidad de aire MODERADO")
    elif ICA[i]>= 101 and ICA[i]<=150:
        print(ciudades[i],"tiene un indice de calidad de aire DAÑINO PARA GRUPOS DE GENTE SENSIBLE")
    elif ICA[i] >= 151 and ICA[i]<= 200:
        print(ciudades[i],"tiene un indice de calidad de aire DAÑINA PARA LA SALUD")

