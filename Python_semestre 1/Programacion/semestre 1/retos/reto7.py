
def idk():

   frase=((input("Ingrese alguna oración:\n")))
   palabras=frase.split()
   return {palabra: len(palabra) for palabra in palabras}

diccionario=idk()
print(diccionario)
