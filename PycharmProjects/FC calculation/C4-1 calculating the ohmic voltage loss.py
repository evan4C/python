"""
Determine the ohmic voltage loss for a 100 cm2 PEMFC
that has an electrolyte membrane with a conductivity of 0.10 Ω−1 cm−1
and a thickness of 50 microns (um).
The current density is 0.7 A/cm2 and R for the fuel is 0.005Ω.
Plot the ohmic voltage losses for electrolyte thicknesses of 25, 50, 75, 100, and 150 microns (mm).
"""
import numpy as np
import matplotlib.pyplot as plt

# inputs

i = 0.7  # A/cm2
A = 100  # cell area
L = 0.005  # membrane thickness
sigma = 0.1  # conductivity s/cm
R_elec = 0.005  # electrical resistance

I = i * A
R_ionic = L / (sigma * A)
V_ohmic = I * (R_elec + R_ionic)
print(V_ohmic)


def mem_resistance(thickness):
    sigma = 0.1
    A = 100
    return thickness / (sigma * A)


L1 = 0.0025
L2 = 0.005
L3 = 0.01
L4 = 0.015

i = np.arange(0, 1, 0.01)
I = i * A
V1 = I * (mem_resistance(L1) + R_elec)
V2 = I * (mem_resistance(L2) + R_elec)
V3 = I * (mem_resistance(L3) + R_elec)
V4 = I * (mem_resistance(L4) + R_elec)

plt.plot(i, V1, label=L1)
plt.plot(i, V2, label=L2)
plt.plot(i, V3, label=L3)
plt.plot(i, V4, label=L4)
plt.xlabel("current density(A/cm2)")
plt.ylabel("ohmic voltage(V)")
plt.grid()
plt.legend()
plt.show()