"""El dueño de una tienda compra un artículo a un costo dado (costo). 
Obtener el precio al que lo debe vender (pre_vta) para obtener una 
ganancia del 30% respecto al precio de venta."""

costo=int(input("indique el precio costo del articulo: "))
pre_vta=(costo*0.3)+costo
print("El precio que debe vender debe ser de: "+str(pre_vta) +"Bs")