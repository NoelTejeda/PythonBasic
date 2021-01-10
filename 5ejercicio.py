"""Un profesor desea saber qué porcentaje de hombres y que porcentaje de 
mujeres hay en su curso si se conocen el número de hombres (nh) y el número 
de mujeres (nm)."""

nh=int(input("indique la cantidad de hombres en el salon: "))
nm=int(input("indique la cantidad de mujeres en el salon: "))

sumsalon=nh+nm
porch=nh*100/sumsalon
porcm=nm*100/sumsalon

print("el % de hombres es de: "+str(porch),"y el % de mujeres es de: "+str(porcm))