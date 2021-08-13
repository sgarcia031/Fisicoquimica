#INTEGRANTES: Marcela Aristizabal Julio / Samuel Garcia Isaza

import numpy as np
import matplotlib.pyplot as plt

c = 1                
n = 1                
R = 8.314            
Ti = 323.15         #Temperatura a 50 grados (C)      
Vi = 1                
Vf = 5               
v_variable = np.arange(1, 1000, 20)

#Definición de trabajos 
W1 = R*Ti*n*np.log(v_variable) - R*Ti*n*np.log(Vi)
W2 = -R*v_variable*c*n + R*Vi*c*n + R*n*(Ti + Vi*c)*np.log(v_variable) - R*n*(Ti + Vi*c)*np.log(Vi)

#GRAFICA

plt.plot (v_variable, W1, label = 'W1(V)')
plt.plot (v_variable, W2, label = 'W2(V)')

plt.title ('Comparación entre trabajos')
plt.xlabel('Variación del Volumen (m^3)')
plt.ylabel('Trabajo realizado (Joules)')
plt.legend ()
plt.show ()