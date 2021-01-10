"""En un hospital existen tres áreas: Ginecología, Pediatría y Traumatología. 
El presupuesto anual del hospital pre_a) se reparte conforme a la siguiente.
tabla:

Área			Porcentaje del presupuesto
Ginecología				40%
Traumatología			30%
Pediatría				30%
Diseñar un algoritmo para calcular la cantidad de dinero que recibirá cada área."""

presupuesto= int (input("Indique la cantidad del presupuesto: "))
Ginecología= (presupuesto*40)/100
Traumatología=(presupuesto*30)/100
pediatria=(presupuesto*30)/100

print("la cantidad de dinero que recibirá Ginecologia será: "+str(Ginecología))
print("la cantidad de dinero que recibirá Traumatologia será: "+str(Traumatología))
print("la cantidad de dinero que recibirá pediatria será: "+str(pediatria))