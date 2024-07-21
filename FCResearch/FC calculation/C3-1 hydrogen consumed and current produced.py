"""
A fuel cell is operating at 60°C and 3 atm. The fuel cell runs for 120 hours.
How much current does the fuel cell produce at a ﬂow rate of 5 sccm?
How many moles of H2 are consumed?
"""

# inputs

R = 0.082  # ideal gas constant (L/atm/molK)
T = 333.15
dV_dt = 0.005  # volumetric flow rate (L/min)
p = 3  # atm
n = 2  # mol electron per mole fuel
F = 96487
t = 120 * 3600  # reaction time

# convert volumetric flow rate to molar flow rate

dN_dt = p * dV_dt / (R * T)

# calculate the total current

i = n * F * dN_dt * (1 / 60)

Q = i * t

N_H2 = Q / (n * F)