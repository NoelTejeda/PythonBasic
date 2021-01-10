#Una tienda ofrece un descuento del 15% sobre el total de la compra 
#de sus clientes, diseñe un algoritmo para saber cuánto deberá pagar c/u 
#si conoce el total de su compra.

tc=int(input("ingrese el total de su compra: "))
desc=tc-(tc*0.15)
print("la cantidad a pagar será de: "+str(desc))