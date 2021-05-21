from scipy.interpolate import lagrange
from os import system
import matplotlib.pyplot as plt
import numpy as np

#Variables declaradas
x = []
y = []
xi = 0

print("\n\t\t|| INTERPOLACION DE LAGRANGE ||")

#petición cantidad de pares ordenados
pares = int(input("\n\tCantidad de pares ordenados a utilizar: "))

#Rellena los vectores con los pares ordenados
for i in range(pares):
    x.append(int(input("\tIngrese el valor de X en el par ordenado #"+str(i+1)+": ")))
    y.append(int(input("\tIngrese el valor de Y en el par ordenado #"+str(i+1)+": ")))

#inicializa las variables de maximo y minimo para luego rellenarla    
xmax = 0
xmin = x[0]    

#Rellena las variables de maximo y minimo en x
for j in range(pares):
    if(x[j] > xmax):
        xmax = x[j]
    if(x[j] < xmin):
        xmin = x[j]

op = 0    

#Pregunta si desea ingresar un x para saber su resultado interpolado        
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

#Se realiza el polinomio de lagrange mediante la libreria scipy
p = lagrange(x, y)

#Solicitamos un rango de numero con intervalos 0.1 entre la x maximo y minima de los pares ordenados
xprueba = np.arange(xmin, (xmax + 0.1), 0.1)
yprueba = []

#Se prueban los valoren en x para el polinomio de lagrange
for i in xprueba:
    #Se rellena el vector y que será utilizado para el gráfico
    yprueba.append(p(i))

#Se imprimen los puntos ingresados por el usuario en el gráfico y los obtenidos en las pruebas
plt.plot(x , y, 'ok', label='puntos conocidos')
plt.plot(xprueba, yprueba, '--k', label='valores verdaderos')

#Etiquetas de los ejes
plt.xlabel("X")
plt.ylabel("Y")
#Orden de mostrar el gráfico
plt.show()    

system("cls")

#Se imprime la información ingresada y el polinomio
print("\n\t\t|| INTERPOLACION DE LAGRANGE ||")
print("\n\tValores de X: ")
print(x)
print("\n\tValores de Y: ")
print(y)
print("\n\tPolinomio resultante:")
print(p)

#Si se ingreso un valor en x para evaluar su resultado f(x), ingresará en el if
if xi != 0:
    #Resultado de la evalución en f(x)
    resultado = p(xi)
    #Se inprime el resultado de la evaluación
    print("\n\tEl resultado del polinomio, evaluado en X = "+str(xi)+" es "+str(resultado))


    
    
   
 
