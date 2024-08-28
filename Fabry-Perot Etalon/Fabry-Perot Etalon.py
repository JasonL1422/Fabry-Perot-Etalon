#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Aug 27 23:20:34 2024

@author: jongcheollee
"""

import numpy as np
import matplotlib.pyplot as plt

c=3e8 # (m/s)
n=1 # air gap
d=0.0103e-3 # (m), effective thickness
R=0.965

fsr=c/(2*n*d) # (Hz)
fsr="{:.2e}".format(fsr)
fwhm= (c*(1-R))/(2*np.pi*n*d*np.sqrt(R))
fwhm="{:.2e}".format(fwhm)
Fin=(np.pi*np.sqrt(R))/(1-R)
Fin="{:.2f}".format(Fin)

print("fsr=",fsr,"(Hz), fwhm=",fwhm,"Finesse=",Fin)

def delta(lamda,theta):
    return (2 * np.pi * n * d * np.cos(theta * np.pi / 180)) / lamda
def Transmission(lamda,theta):
    return 1 / (1 + (4 * R / (1 - R) ** 2) * np.sin(delta(lamda,theta) / 2) ** 2)

#-------

lamda=800 * 10 ** -9
x = np.linspace(10,80,2000)
y = Transmission(lamda, x)
plt.plot(x,y,label=f'lamda={lamda * 10**9:.0f}nm')
plt.xlabel('Angle (deg)')
plt.ylabel('Transmission')
plt.legend()
plt.show()

#-------

theta = 45.68 #deg
x2 = np.linspace(700e-9,900e-9,2000)
y2 = Transmission(x2, theta)
plt.plot(x2 * 10**9,y2, label=f'Angle={theta}°')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Transmission')
plt.legend(loc='upper left')
plt.show()

#-------

theta = 42 #deg
x2 = np.linspace(700e-9,900e-9,2000)
y2 = Transmission(x2, theta)
plt.plot(x2 * 10**9,y2,label=f'Angle={theta}°')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Transmission')
plt.legend()
plt.show()

#-------

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection = '3d')

lamda = np.linspace(700e-9,900e-9,2000)
theta = np.linspace(10,80,200)

l, t = np.meshgrid(lamda,theta)
z = Transmission(l, t)
ax.plot_surface(l*1e9, t, z, cmap='copper')
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Angle (°)')
ax.set_zlabel('Transmission')

plt.show()

#-------

theta = 45.68 #deg
Rval=[0.75, 0.8, 0.9]

for R in Rval:
    x2 = np.linspace(700e-9,900e-9,2000)
    y2 = Transmission(x2, theta)
    plt.plot(x2 * 10**9,y2, label=f'R={R}')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Transmission')
plt.legend(loc='upper right')
plt.show()



