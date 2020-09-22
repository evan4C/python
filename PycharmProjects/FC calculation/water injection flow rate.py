import numpy as np

# inputs
T_H2_in = 20 + 273.15
T_air_out = 80 + 273.15
RH = 0.5  # relative humidity
P = 120  # pressure
n_cell = 1
Power = 500
V = 0.7
M_H2O = 18.015
F = 96485
S_O2 = 2  # oxygen stoichiometric ratio
r_O2 = 0.2095  # mole fraction of oxygen in air
r_O2_in = r_O2

I = Power / V
n_O2 = 4


# calculate the saturation pressure
def Pvs(T):
    a = -5800.2206
    b = 1.3914993
    c = -0.048640239
    d = 0.41764768e-4
    e = -0.14452093e-7
    f = 6.5459673
    result = np.exp(a / T + b + c * T + d * (T ** 2) + e * (T ** 3) + f * np.log(T)) / 1000
    return result


Pvs_in = Pvs(T_H2_in)
m_H2O_air_in = S_O2 * RH * M_H2O * Pvs_in * I * n_cell / (r_O2 * n_O2 * F * (P - RH * Pvs_in))
n_H2 = 2
m_H2O_gen = I * M_H2O / (n_H2 * F)
deltaPca = 18.675

Pvs_out = Pvs(T_air_out)
m_H2O_air_out = (S_O2 - r_O2_in) / r_O2_in * M_H2O / (4 * F) * Pvs_out / (P - deltaPca - Pvs_out) * I * n_cell
m_H2O_inject = m_H2O_air_out - m_H2O_air_in - m_H2O_gen

print(m_H2O_inject)