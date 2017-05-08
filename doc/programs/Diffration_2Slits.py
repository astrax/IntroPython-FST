from numpy import pi, linspace, sin, cos
import matplotlib.pyplot as plt

lamda=650*1.E-9; k=(2.*pi)/lamda       # Wavelength
b= 0.001*1.E-0                         # Slit width
d=1.5*1.E-3                            # Edge-Slits distance 
a=b+d                                  # Center-slits distance
D = 2                                  # Screen-Slit Distantance (m)
e= 1 * 1.E-2                           # Side of a square-shaped screen (m)
X_Mmax=e/2. ; X_Mmin = -e/2.           # Interval for position
N =400                                 # Size of space discretisation 
X=linspace(X_Mmin, X_Mmax,N)           # Screen coordinates
B=(k*b*X)/(2.*D)                       # Intermediate variable
A=(k*a*X)/(2.*D)
I=(cos(A)**2 * (sin(B)/B)**2)
envelop=(sin(B)/B)**2
fig = plt.figure(figsize=(8, 5))
fig.suptitle('Fraunhofer Diffraction by identic double slits',fontsize=14, fontweight='bold')
ax1 = fig.add_subplot(111)
ax1.grid(True)
ax1.plot(X,I,'-k', linewidth=3)
ax1.plot(X,envelop,'--k', linewidth=2, alpha=0.8)
ax1.set_xlim(X_Mmin, X_Mmax)
ax1.set_xlabel(r'$X \ (m)$',fontsize=14, fontweight='bold')
ax1.set_ylabel(r'$I(X,Y)/I_0$',fontsize=14, fontweight='bold')
ax1.set_title(r"$wavelength \ \lambda = %.1e \ m, \ b = %.0e \ m, \ a = %.0e \ m, \ D = %.0e \ m$"% (lamda,b,a,D),
              fontsize=14)
plt.savefig("2slits1D_identique.png")
plt.show()
