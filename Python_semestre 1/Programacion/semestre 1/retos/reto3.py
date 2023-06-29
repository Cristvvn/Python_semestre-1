ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas",]
ica = [134, 99, 245, 50]

indice_minimo= min(ica)
indice_maximo = max(ica)

ciudad_max = ciudades[ica.index(indice_maximo)]

ciudad_min = ciudades[ica.index(indice_minimo)]

print("Las ciudades con menos Indice de calidad  del Aire son:" ,ciudades[3],":",indice_minimo)


print("Las ciudades con mayor Indice de calidad  del Aire son:" ,ciudades[2],":",indice_maximo)