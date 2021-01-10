"""Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio,
conociendo la edad y la formula es: num_pulsaciones = (220 - edad)/10 """

print("Calculadora de pulsaciones")
edad=int(input("Indique su edad: "))
num_pulsaciones=(220-edad)/10
print("el numero de pulsaciones es de: "+str(num_pulsaciones))
