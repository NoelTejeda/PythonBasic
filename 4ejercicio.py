"""Diseñe un algoritmo que permita a los estudiantes saber cuál será su calificación final en la materia de Programación Digital, 
 si la calificación se compone de los siguientes porcentajes:
 i.- 55% del promedio de sus tres calificaciones parciales (c1, c2, c3).
ii.- 30% de la calificación del examen final (ef). 
iii.- 15% de la calificación de un trabajo final (tf)."""

c1= int(input("ingrese las tres calificaciones parcial 1: "))
c2= int(input("ingrese las tres calificaciones parcial 2: "))
c3= int(input("ingrese las tres calificaciones parcial 3: "))
ef= int(input("ingrese la calificacion del examen final: "))
tf= int(input("ingrese la calificacion del trabajo final: "))

np=((c1+c2+c3)/3)*0.55
nef=ef*0.30
ntf=tf*0.15
cf=np+nef+ntf

print("la calificación del estudiante es de: "+str(cf))
