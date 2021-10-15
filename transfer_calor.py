#Integrantes: 

#Marcela Aristizábal Julio
#Samuel García Isaza

import numpy as np
from matplotlib import pyplot as plt

r = 0.2                    
imax = 50                #Número máximo de pasos espaciales ---> x
nmax = 1000              #Número máximo de pasos temporales ---> y, (tiempo t) 

T = np.zeros((nmax,imax))   #Creamos un array de zeros.

#Temperatura específica en la frontera en el tiempo t=0.
T[nmax-1,:] = 25         #Cada celda de la última fila se convertirá en 25ºC (frontera inferior).
T[0,:] = 25              #Cada celda de la primera fila se convertirá en 25ºC (frontera superior).
T[:,0] = 75              #Cada celda de la primera columna se convertirá en 75ºC (frontera izquierda).
T[:,imax-1] = 75         #Cada celda de la útima columna se convertirá en 75ºC (frontera derecha). 

print(T) #Condiciones de frontera en el arreglo con t=0.

#Creamos una rejilla para graficar.

t = np.arange(0,T.shape[0])             #Número de pasos para t según el número de filas.
x = np.arange(0,T.shape [1])            #Número de pasos para x según el número de columnas.

X,Y = np.meshgrid(x,t)

for n in range(0, nmax-1):                   #Ciclo for para la evolución temporal. -1 para que no se desborde (0-100) y no de valores de 101 que no existe.
    for i in range (1, imax-1):              #Ciclo for para la evolución espacial.
        T[n+1,i]= T[n,i]+ r*(T[n,i+1] - 2*T[n,i] + T[n,i-1])

Z = T 

fig = plt.figure (figsize=[12,9])
ax= fig.add_subplot (111,projection = '3d')
ax.view_init (25,60)

#Creamos la superficie 
ax.plot_surface (X,Y,Z)

ax.set_xlabel ('Posición (mm)')
ax.set_ylabel ('Tiempo (ms)')
ax.set_zlabel ('Temperatura (K)')
ax.set_title ('Distribución de temperatura espacial-temporal')

plt.show()
