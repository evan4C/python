# EXAMPLE 2-2: Calculating the Enthalpy of H2, O2, and Water
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# font configuration
font = FontProperties(weight='bold', size=12)

# Inputs

T = 353  # temperature(K)
T_ref = 298  # reference temperature(K)
T_av = (T + T_ref) / 2  # average temperature(K)
m_H2 = 2.016  # moles of hydrogen
m_O2 = 31.999  # moles of oxygen
m_H2O = 18.015  # moles of H2O
hf_H2 = 0  # enthalpy at standard state
hf_O2 = 0  # enthalpy at standard state
hf_H2Ol = -285826  # enthalpy at std state of water in liquid phase(J/mol)
hf_H2Og = -241826  # enthalpy at std state of water in gas phase(J/mol)

# Interpolate values

T_table = np.array([250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 900, 1000])
cp_h2_table = np.array([14.051, 14.307, 14.427, 14.476, 14.501, 14.513, 14.530, 14.546, 14.571,
                        14.604, 14.645, 14.695, 14.822, 14.983])
cp_o2_table = np.array([0.913, 0.918, 0.928, 0.941, 0.956, 0.972, 0.988, 1.003, 1.017, 1.031, 1.043,
                        1.054, 1.074, 1.090])
cp_h2og_table = np.array([33.324, 33.669, 34.051, 34.467, 34.914, 35.390, 35.891, 36.415,
                          36.960, 37.523, 38.100, 38.690, 39.895, 41.118])

T_table2 = np.arange(273, 454, 20)
cp_h2ol_table = np.array([4.2178, 4.1818, 4.1784, 4.1843, 4.1964, 4.2161, 4.250, 4.283, 4.342, 4.417])

# interpolate values to calculate specific heats (KJ/kgK)

f_cp_h2 = interp1d(T_table, cp_h2_table)
cp_h21 = f_cp_h2(T_av)

f_cp_o2 = interp1d(T_table, cp_o2_table)
cp_o21 = f_cp_o2(T_av)

f_cp_h2og = interp1d(T_table, cp_h2og_table)
cp_h2og1 = f_cp_h2og(T_av)

f_cp_h2ol = interp1d(T_table2, cp_h2ol_table)
cp_h2ol1 = f_cp_h2ol(T_av)

# convert to a per mole basis

cp_h2 = cp_h21 * m_H2
cp_o2 = cp_o21 * m_O2
cp_h2og = cp_h2og1
cp_h2ol = cp_h2ol1 * m_H2O

# Determine absolute enthalpy

h_h2 = hf_H2 + cp_h2 * (T - T_ref)
h_o2 = hf_O2 + cp_o2 * (T - T_ref)
h_h2ol = hf_H2Ol + cp_h2ol * (T - T_ref)
h_H2Og = hf_H2Og + cp_h2og * (T - T_ref)

R = 8.314
T_table3 = np.arange(300, 1001, 50)


# enthalpy calculations

def f_hs_h2(t_h2):
    hs_h2 = 3.057 * t_h2 + ((1 / 2) * 2.677e-3 * t_h2 ** 2) - ((1 / 3) * 5.810e-6 * t_h2 ** 3) + (
                (1 / 4) * 5.521e-9 * t_h2 ** 4) - ((1 / 5) * 1.812e-12 * t_h2 ** 5)
    return hs_h2


def f_hs_o2(t_o2):
    hs_o2 = 3.626 * t_o2 + ((1 / 2) * 1.878e-3 * t_o2 ** 2) - ((1 / 3) * 7.055e-6 * t_o2 ** 3) + (
                (1 / 4) * 6.764e-9 * t_o2 ** 4) - ((1 / 5) * 2.156e-12 * t_o2 ** 5)
    return hs_o2


def f_hs_h2o(t_h2o):
    hs_h2o = 4.070 * t_h2o + ((1 / 2) * 1.108e-3 * t_h2o ** 2) - ((1 / 3) * 4.152e-6 * t_h2o ** 3) + (
                (1 / 4) * 2.964e-9 * t_h2o ** 4) - ((1 / 5) * 0.807e-12 * t_h2o ** 5)
    return hs_h2o


h_H2_list = []
h_O2_list = []
h_H2O_list = []

for t in T_table3:
    hs_H2 = R * (f_hs_h2(t) - f_hs_h2(298))
    h_H2 = hf_H2 + hs_H2
    h_H2_list.append(h_H2)
    hs_O2 = R * (f_hs_o2(t) - f_hs_o2(298))
    h_O2 = hf_O2 + hs_O2
    h_O2_list.append(h_O2)
    hs_H2O = R * (f_hs_h2o(t) - f_hs_h2o(298))
    h_H2O = hf_H2Og + hs_H2O
    h_H2O_list.append(h_H2O)

plt.plot(T_table3, h_H2_list, label='H2')
plt.plot(T_table3, h_O2_list, label='O2')
# plt.plot(T_table3, h_H2O_list)
plt.legend()
plt.title("Hydrogen and Oxygen Enthalpies", fontproperties=font)
plt.xlabel("Temperature (K)", fontproperties=font)
plt.ylabel("Hydrogen and Oxygen Enthalpies (KJ/kg)", fontproperties=font)
plt.grid(True)
plt.show()
