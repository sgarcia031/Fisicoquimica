# INTEGRANTES
# Marcela Aristizábal Julio
# Samuel García Isaza

from sympy import symbols ,Function,Eq
from sympy.solvers.ode.ode import dsolve
import matplotlib.pyplot as plt
import numpy as np

A = 3e-4                             #Área de la base de la capa(shell)
l = 1e-3                             #Altura de la capa(shell)
Ce = 3.726                           #Calor específico de la capa (shell)
p = 1.1e3                            #Densidad de la capa (shell)
tao = 60                             #Tao = 60 s ––––> 1 min
Tc = 37                              #Temperatura núcleo(core).
To = 35                              #–––> Coindición iniicial (CI) #Temperatura de la capa (shell) con t = 0.
Ta = 23                              #Temperatura ambiente.
h = 20                               #Coeficiente de transmision de calor piel(skin)-aire.
ko = 20                              #Coeficiente de transmision de calor núcleo-capa inicial.

# Planteamiento y solución de la EDO (Ecuacion diferencial ordinaria)
t = symbols("t")
J = symbols("J")
f = symbols("f")
T = Function("T")
ecudif = Eq(T(t).diff() , J - f*T(t))
ecuacion = dsolve(ecudif,T(t))                # Solución de la ecuacion de T(t).         


# Calcular la masa con respecto al área de la capa.
# K con respecto al tiempo.

m = A * l * p                        # Masa de la capa(shell) en kg.
t =np.arange(0,600,1)

k = ko/2 * (np.exp(-t/tao) + 1 )     # Coeficiente de transmisión de calor interfaz núcleo-capa con respecto a t.

M = (m*Ce)/A
f = (k+h)/M
J = ((k*Tc) + (h*Ta))/M

#Temperatura con respecto a t = 0.
T=(J + np.exp(f*(-t)))/f

# Comportamiento de la temperatura en el transcurso del tiempo.
plt.plot(t,T)

plt.xlabel('Tiempo(s)')                                  
plt.ylabel('Temperatura en el tiempo T(t)')                                             

plt.title('Comportamiento de la temperatura con respecto al tiempo')    
plt.show()  
