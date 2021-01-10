"""Diseñe un algoritmo para convertir una cantidad en 
bolívares (can_bs) en dólares, asumiendo que la unidad cambiaría es un
dato proporcionado (tasa)."""

can_bs=int(input("Indique la cantidad en bolivares a cambiar: "))
tasa=int(input("Indique la tasa $ del día: "))

resultado= can_bs / tasa
c=round(resultado, 2)
# Una solución posible pasa por redondear el resultado a 2 decimales con la función round().

print("la cantidad en $ es: "+str (c) + "$")
# me gustaria que el resultado solo aparezcan dos decimales https://tutorialdeep.com/knowhow/round-float-to-2-decimal-places-python/
# ejemplo: print(round(myFloat, 2));