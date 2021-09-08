#INTEGRANTES: MARCELA ARISTIZABAL JULIO / SAMUEL GARCIA ISAZA

#Punto2.

import numpy as np                
import matplotlib.pyplot as plt 

def f(x, y):                                
    return x**4 + x*y**4

x = np.linspace(-1, 1, 20)                     
y = np.linspace(-1, 1, 20)

x, y = np.meshgrid(x, y)                            
z = f(x, y)                                        

ax = plt.axes(projection='3d')                      
ax.set_xlabel("X")                                 
ax.set_ylabel("Y")                                 
ax.set_zlabel("Z")                                  
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')    
ax.set_title('Gráfico 3D')
plt.show()

#Punto3.   

dx = 0.1                                                  
dy = 0.1                                                  
xr = np.arange(-1, 1, dx)                                
yr = np.arange(-1, 1, dy)                                 

x, y = np.meshgrid (xr, yr, indexing = 'ij')

z = x**4 + x*y**4 

gradx, grady = np.gradient (z, dx, dy)

n = 10                                                   
l = np.array([0.0, 0.5, 1.0, 1.5, 2.0])                 

plt.contourf(x, y, z, n)                                
ax=plt.contour(x, y, z, levels = l, colors = 'k', linewidths = 1, linestyles = 'solid')   
plt.title("Gradiente", size = 18)
plt.xlabel("X", size = 16,)
plt.ylabel("Y", size = 16)
plt.quiver(x, y, gradx , grady)                          
plt.show()

#Punto4.

import sympy
from sympy.vector import CoordSys3D, gradient, divergence        

v = CoordSys3D('v')

z = (v.x)**4 + ((v.x) * (v.y)**4)
print("La función es:", z)
print("--------------------------")

g = gradient(z)
print("El gradiente de la función es:", g)                                                  
print("--------------------------")


d = divergence(g)
print("El Laplaciano de la función es:", d)   

#Punto5.

lim = 1
dx = 0.1                                                 
dy = 0.1                                                  
xr = np.arange(-lim, lim, dx)                            
yr = np.arange(-lim, lim, dy)                            

x, y = np.meshgrid (xr, yr, indexing = 'ij')

def divergence(f, h):                               
    num_dims = len(f)                                
    return np.ufunc.reduce(np.add, [np.gradient(f[i], h[i], axis=i) for i in range(num_dims)])

z =  x**4 + x*y**4

gradx, grady = np.gradient (z, dx, dy)    

Fx  = gradx       
Fy  = grady       

F = [Fx, Fy]      
h = [dx, dy]      

g = divergence(F, h)   

plt.pcolormesh(x, y, g, shading='nearest', cmap=plt.cm.get_cmap('coolwarm'))
plt.title("Gradiente y Laplaciano", size = 18)
plt.xlabel("X", size = 16,)
plt.ylabel("Y", size = 16)
cbar = plt.colorbar()
plt.quiver(x, y, Fx , Fy)
plt.show()
