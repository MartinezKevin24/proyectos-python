import numpy as np
import matplotlib.pyplot as plt

#Variables a utilizar
op = 0
xi = 0
matriz = []
xmatriz = []
ymatriz = []

print("\n\t\t|| INTERPOLACION DE NEWTON ||")

#Solicitud de la cantidad de pares ordenados a utilizar
cantPares = int(input("\n\tCuantos pares ordenados seran ingresado?: "))

#Se expande la matriz a utilizar
for i in range(cantPares):
    matriz.append([0] * (cantPares+1))

#Se rellena la matriz con los valores de Y al ser ingresados y los valores de X en un vector aparte para facilitar su manejo
for i in range(cantPares):
    xmatriz.append(int(input("\n\tIngrese el valor de X en el par ordenado #"+str(i)+": ")))
    #Las Y serán almacenadas en la primera columna de la matriz
    matriz[i][0] = int(input("\n\tIngrese el valor de Y en el par ordenado #"+str(i)+": "))

#se rellena un vector con los valores de Y ingresados para representarlo en el gráfico
for i in range(cantPares):
    ymatriz.append(matriz[i][0])

xmax = 0
xmin = xmatriz[0]

#Ciclo que separa el maximo y minimo valor de X    
for j in range(cantPares):
    if(xmatriz[j] > xmax):
        xmax = xmatriz[j]
    if(xmatriz[j] < xmin):
        xmin = xmatriz[j]

#Comenzamos a recorrer las columnas desde la 1, ya que esta se encuentra despues de la columna con los f(x) o Y. 
#Este tiene que ser menor o igual a la cantidad de pares ordenados, ya que si hay 4 pares ordenados, las columnas que tendra son 4 + 1.
for j in range(1, cantPares):
    for i in range(cantPares - j): 
        #se van rellenado las columnas de manera escalonada
        matriz[i][j] = (matriz[i+1][j-1]-matriz[i][j-1])/(xmatriz[i+j]-xmatriz[i])

xt = 1
yt = matriz[0][0]

#Se obtiene un vector con intervalos de 0.1 entre el X minimo y maximo
xprueba = np.arange(xmin, (xmax + 0.1), 0.1)
yprueba = []

#ingresa a probar todos los valores del intervalo de X
for x in xprueba:
    
    for i in range(cantPares-1):
        #Multiplica cada uno de los valores de X en los pares ordenados
        xt = xt * (x - xmatriz[i])
        #Se toman los primeros valores de a_1, a_2, a_3, ..., a_n con el acomulado de los X, acomulandolo en Yt.
        yt = yt + matriz[0][i+1] * xt
    
    #Se agrega el resultado de los y en el vector que contiene los y para el gráfico
    yprueba.append(yt)
    #Reinicia los valores de los acomuladores Xy y Yt
    xt = 1
    yt = matriz[0][0]

#Imprime los puntos de los pares ordenados ingresados
plt.plot(xmatriz, ymatriz, "o", label="pares ordenados")
#Imprime los puntos que se obtuvieron en las pruebas para la gráfica
plt.plot(xprueba, yprueba, "--k", label="Puntos verdaderos")

#Etiquetas de los ejes
plt.xlabel("X")
plt.ylabel("Y")

#Se ordena imprimir la gráfica
plt.show()

#Pregunta si quiere evaluar una X dentro del rango de las X en el par ordenado
while True:
   print("\n\tDesea ingresar la X para conocer el resultado del polinomio? SI[1] NO[0]")    
   op = int(input("\n\tIngrese la opcion elegida: "))
   
   #Si la opción está entre el rango de opciones ingrsa al if
   if(op < 2):
       #Si la opción dentro del rango es SI ingresa al if
       if(op == 1):
           while True:
               #Solicita el valor de la x, la cual debe estar entre el rango de las x ingresadas como par ordenado
               xi = int(input("\n\tIngrese el valor de X a interpolar: "))
               #Si es mayor o menor a este rango, se imprimirá un mensaje y repetira el bucle
               if xi < xmin:
                   print("\n\tIngresa un valor que se encuentre entre "+str(xmin)+" y "+str(xmax))
               elif xi > xmax:
                   print("\n\tIngresa un valor que se encuentre entre "+str(xmin)+" y "+str(xmax))
               else:
                   break    
       break

#Si se ingreso un valor en x para evaluar su resultado f(x), ingresará en el if
if xi != 0:
    #Se repite la operación para saber el f(x) interpolado una vez más, pero con el X que se desea evaluar
    for i in range(cantPares-1):
        xt = xt * (xi - xmatriz[i])
        yt = yt + matriz[0][i+1] * xt
        
    #Se imprime el resultado de la interporlación de X        
    print("\n\tEl resultado de la ecuación interpolada es un aproximado a: "+str(yt))      
        