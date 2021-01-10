"""Diseñe un algoritmo para un vendedor que gana un sueldo base (sb) más un 10% extra por comisión de sus ventas y  
 desea calcular cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
 (v1, v2, v3) y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones."""

sb=int(input("indique el salario base del trabajador: "))
v1=int(input("indique cuál fue el monto de la venta 1: "))
v2=int(input("indique cuál fue el monto de la venta 2: "))
v3=int(input("indique cuál fue el monto de la venta 3: "))

vt=(v1+v2+v3)*0.01
gantotal=sb+vt

print("la ganancia por concepto de venta es de: "+str(vt))
print("la ganancia total del mes es de: "+str(gantotal))