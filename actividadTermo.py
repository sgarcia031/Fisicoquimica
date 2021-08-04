#INTEGRANTES: Marcela Aristizábal Julio / Samuel García Isaza

import numpy as np
import math
import matplotlib.pyplot as plt

#Para este ejercicio tomaremos como referencia la masa del nitrógeno (N2)
masa_N2 = 4.65 * 10 ** -26 

k_B = 1.38e-23  

v = np.arange(10, 3000, 15)

#Primera evaluación del gas N2 (nitrógeno) a temperatura de 300K
moles_N2_1 = 4 * math.pi * (masa_N2 / (2 * math.pi * k_B * 300)) ** (3 / 2) * (v**2) * np.exp(-masa_N2 * v**2 / (2 * k_B * 300))

#Segunda evaluación del gas N2 (nitrógeno) a temperatura de 1500K
moles_N2_2 = 4 * math.pi * (masa_N2 / (2 * math.pi * k_B * 1500)) ** (3 / 2) * (v**2) * np.exp(-masa_N2 * v**2 / (2 * k_B * 1500))

#Tercera evaluación del gas N2 (nitrógeno) a temperatura de 5000K
moles_N2_3 = 4 * math.pi * (masa_N2 / (2 * math.pi * k_B * 5000)) ** (3 / 2) * (v**2) * np.exp(-masa_N2 * v**2 / (2 * k_B * 5000))

#Gas a 300K
plt.plot (v, moles_N2_1, label = "Gas N2 a 300 K")
#Gas a 1500K
plt.plot (v, moles_N2_2, label = "Gas N2 a 1500 K")
#Gas a 5000k
plt.plot (v, moles_N2_3, label = "Gas N2 a 5000 K")

plt.xlabel ('Velocidad (m/s)')
plt.ylabel ('n(v)')

plt.title('Distribución de velocidades de Maxwell-Boltzmann')
plt.legend()                                                   
plt.show() 