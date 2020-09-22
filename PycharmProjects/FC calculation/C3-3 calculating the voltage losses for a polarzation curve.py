"""
A 100-cm2 active area hydrogen–air fuel cell stack has 90 cells,
and operates at a temperature of 80 °C.
Both the hydrogen and air are fed to the fuel cell at a pressure of 3 atm.
Create the polarization and fuel cell power curve for this fuel cell stack.

the transfer coefficient, a, is 0.5,
the exchange current density, i0 , is 10 −6.912 A/cm2 ,
the limiting current density, iL , is 1.4 A/cm2 ,
the amplification constant (a1 ) is 0.085,
the Gibbs function in liquid form, Gf,liq , is −228,170 J/mol,
the constant for mass transport, k, is 1.1,
and the internal resistance, R, is 0.19 Ωcm2.
"""
import numpy as np
import matplotlib.pyplot as plt

# inputs
R = 8.314  # [J/(mol*K)]
F = 96487  # [C]
Tc = 80
P_h2 = 3
P_air = 3
Area_cell = 100
Num_cells = 90
r = 0.19  # [ohmic * cm2]
alpha = 0.5
alpha1 = 0.085
i0 = 10 ** (-6.912)
il = 1.4
Gf_liq = -228170
k = 1.1

# convert degree to calvin
Tk = Tc + 273.15

i = np.arange(0, 1.01, 0.01)

# calculate the sat pressure of water
p_sat_water = 10 ** (-2.1794 + 0.02953 * Tk - 9.1837e-5 * Tk ** 2 + 1.4454e-7 * Tk ** 3)

# calculate the partial pressure of h2
pp_h2 = 0.5 * (P_h2 / np.exp(1.653 * i / (Tk ** 1.334)) - p_sat_water)

# calculate the partial pressure of o2
pp_o2 = P_air / np.exp(4.192 * i / (Tk ** 1.334)) - p_sat_water

# activation loss
b = R * Tk / (2 * alpha * F)
V_act = b * np.log10(i/i0)

# ohmic loss
V_ohmic = i * r

# mass transport loss
# np.where(condition, x, y) 满足条件(condition)，输出x，不满足输出y。
V_conc = np.where((1 - (i / il)) > 0, -alpha1 * i ** k * np.log(1 - (i / il)), 0)

# calculate nernst voltage
E_nernst = -Gf_liq / (2 * F) - (R * Tk * np.log(P_h2 * P_air ** 0.5) / (2 * F))

V_out = E_nernst - V_act - V_ohmic - V_conc
V_out = np.where(V_out > 0, V_out, 0)

plt.plot(i, V_out, label='output')
plt.plot(i, V_act, label='activation')
plt.plot(i, V_ohmic, label='ohmic')
plt.plot(i, V_conc, label='mass transport')
plt.xlabel("current density(A/cm2)")
plt.ylabel("output voltage(V)")
plt.grid()
plt.legend()
plt.show()
