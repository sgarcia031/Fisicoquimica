import numpy as np
import matplotlib.pyplot as plt
import time

# Instantes para tomar "fotos" del crecimiento bacteriano

time_steps = 5 #5 segundos

n = 20; D = 0.2; Lambda = 0.1 
# n = Dimensiones de donde van a crecer las bacterias (20x20)
# D = coeficiente de difusión
# Lambda = constante de la tasa de la reproducción

a = int (n/2) # Para que sea en la mitad (el centro) de la cuadrícula
b = int (n/2)

C = np.zeros ((n,n)) #Cuadrícula de 20 x 20 en blanco (Sin bacterias)

grad_C = np.zeros ((n,n)) #Cargamos el valor para el Laplaciano en ceros, dentro de un ciclo for

# Ubicamos con bacteria en el centro de la cuadrícula
C[a,b] = 1 #En coordenadas (10, 10)

x = np.arange (0,n)
y = np.arange (0,n)
X , Y = np.meshgrid(x,y)

for step in range (0, time_steps): #Desde 0 --> 5
    for x in range (1, n-1): # Recorriendo valores de X. Empieza desde 1 y no desde 0 hasta n-1; para tomar valores previos y posteriores (evita errores)
        for y in range (1, n-1): # Valores en Y
            grad_C [x,y] =  C [x, y-1] + C [x, y+1] + C [x-1, y] + C [x+1, y] 
            C = (1-4 * D)*C + D * grad_C + Lambda * C 
            Z = C

#CREACION DE FIGURA. NOTA: Esta es la gráfica con el resultado final, en caso de querer ver gráficas de todo el proceso, dar dos tabs al código desde este punto hasta el final (menos el plt.show)
fig = plt.figure(figsize = (12,9))
ax = fig.add_subplot (111, projection = '3d')
ax.view_init(30,60)
# time.sleep(0.1) ###En caso de querer verlo imagen por imagen del proceso
surf = ax.plot_surface (X,Y,Z, cmap='viridis',edgecolor='none')
ax.set_title ('Expansion Bacteriana')
ax.set_zlabel ('Presencia de bacterias')
ax.set_xlabel ('Eje x de cuadricula')
ax.set_ylabel ('Eje y de cuadricula')
fig.colorbar(surf) #Concentracion de bacterias (diferenciado por colores)

plt.show()