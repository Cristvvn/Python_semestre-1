mes = input("Ingrese un mes: ")

if mes.lower() in ["diciembre", "enero", "febrero"]:
    estacion = "verano"
elif mes.lower() in ["marzo", "abril", "mayo"]:
    estacion = "otoño"
elif mes.lower() in ["junio", "julio", "agosto"]:
    estacion = "invierno"
elif mes.lower() in ["septiembre", "octubre", "noviembre"]:
    estacion = "primavera"
else:
    estacion = "mes inválido"

print(f"La estación correspondiente al mes de {mes} es {estacion}.")
