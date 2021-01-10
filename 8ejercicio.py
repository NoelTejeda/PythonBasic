#Calcular el nuevo salario de un obrero si obtuvo un incremento del 25% sobre su salario anterior (sa).

salario_anterior = int(input("Indique su salario anterior: "))
nvo_salario= (salario_anterior * 0.25) + salario_anterior
sal_nvo= round (nvo_salario,2)
print("su nuevo salario es: "+ str(sal_nvo))