import numpy as np
import matplotlib.pyplot as plt

Xi = 2e4 # längenbezogener Strömungswiderstand
sigma = 0.97 # Porösität
rho_0 = 1.2041 # Luftdichte
c = 343.2
Z_0 = c*rho_0 # Schallkennimpedanz Luft
d = 0.1 # Dicke des Absorbers

fs = np.geomspace(20,20000,1000) #np.array([300, 1000])
ws = 2*np.pi*fs
ks = ws/c

def kdash (omega):
    return omega / c * np.sqrt(1-(1j*sigma*Xi/(rho_0*omega)))

def zdash(omega):
    return rho_0*c/sigma *np.sqrt(1-(1j*sigma*Xi/(rho_0*omega)))

def z(omega):
    return -1j*zdash(omega)*1/np.tan(kdash(omega)*d)

def absorb(z):
    return 4*np.real(z/(rho_0*c))/((np.real(z/(rho_0*c)+1))**2+(np.imag(z/(rho_0*c))**2))
# Berechnung von Wandimpedanz und Absorptionsgrad mittels der zuvor berechneten Absorberkennwete

zarray = []
absorbarray = []
for omega in ws:
    zarray.append(z(omega))
    absorbarray.append(absorb(zarray[-1]))
    
#print("Wandimpedanz des Absorbers:", zarray[0], " N*s / m^3 für 300 Hz und ", zarray[1], " N*s / m^3 für 1000 Hz.")
#print("Absorptionsgrad des Absorbers", absorbarray[0], " für 300 Hz und ", absorbarray[1], " für 1000 Hz.")

plt.semilogx(fs,absorbarray)
plt.show()