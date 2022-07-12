#VL10 Folie 11

import numpy as np
import matplotlib.pyplot as plt
#omega_0 = np.sqrt(rho_0*c**2/(m*d))
rho_0 = 1.2041 #kg/m^3
c = 343.2 #m/s
Z_0 = rho_0*c
d = 0.05 #m
omega = np.geomspace(20,20000,1000)
f_0 = 300 #Hz
omega_0 = 2 * np.pi * f_0
r = 1 #schallhart
m = rho_0*c**2/(omega_0**2*d)
const = m*d
d = np.array([0.01, 0.05, 0.1, 0.15, 0.2])
m = const/d
def absorb (m, omega_0):
    return 4*r*Z_0 / ( (r+Z_0)**2 + ( (m/omega) * (omega**2-omega_0**2) )**2 )


for i in range(len(m)):
    alpha = absorb(m[i], omega_0)*100
    plt.semilogx(omega/omega_0, alpha, label = 'd = '+str(int(100*d[i]))+' cm')
plt.legend()
plt.xlabel('$\omega / \omega_0$ ')
plt.ylabel('Absorptionskoeffizient / %')
plt.show()