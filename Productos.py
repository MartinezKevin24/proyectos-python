print("\n\t\tSelector de mejorres ofertas en productos");

name0 = input("\tIngrese el nombre del Producto 1: ")
gr0 = int(input("\tCantidad en gramos de "+name0+": "))
price0 = float(input("\tPrecio de los "+str(gr0)+"gr: "))
result0 = (100 * price0)/gr0

name1 = input("\n\tIngrese el nombre del Producto #2: ")
gr1 = int(input("\tCantidad en gramos de "+name1+": "))
price1 = float(input("\tPrecio de los "+str(gr1)+"gr: "))
result1 = (100 * price1)/gr1

print("\n\tValor del "+name0+" por cada 100gr es de: "+str(result0))
print("\tValor del "+name1+" por cada 100gr es de: "+str(result1))

if(result1 < result0):
    dif = result0 - result1
    print("\n\tEl precio "+name1+" Es mucho mejor que el de "+name0+" por $"+str(dif)+" de diferencia.")
elif (result0 < result1):
    dif = result1 - result0
    print("\n\tEl precio "+name0+" Es mucho mejor que el de "+name1+" por $"+str(dif)+" de diferencia.") 
else:
    print("\n\tLos productos "+name0+" y "+name1+" tienen el mismo valor por cada 100gr")    
