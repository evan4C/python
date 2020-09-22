"""
A hydrogen fuel cell operates at 80 °C at 1 atm.
It has a Naﬁon 112 membrane of 50 mm,
and the following equation can be used for the water content across the membrane:
lambda(z) = 5 + 2exp(100z). This fuel cell has a current density of 0.8 A/cm2 ,
and the water activities at the anode and cathode are 0.8 and 1.0, respectively.
Estimate the ohmic over voltage loss across the membrane.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def mem_resistance(z):
    # inputs
    Tc = 80
    T = Tc + 273.15
    z = 0.005  # membrane thickness
    aw_a = 0.8  # water activity
    aw_c = 1  # water activity
    n = 2.5  # electro-osmotic drag coefficient
    Mn = 1  # nafion equivalent weight(kg/mol)
    i = 0.8  # current density
    F = 96487
    den_dry = 0.00197  # membrane dry density(kg/cm3)
    C = 2.3  # constant dependent upon boundary conditions
    alpha = 1.12  # ratio of water flux to hydrogen flux

    # convert water activity on the nafion surfaces to water contents
    lambda_an = 0.043 + (17.81 * aw_a) - (39.85 * aw_a ** 2) + (36 * aw_a ** 3)
    lambda_ca = 0.043 + (17.81 * aw_c) - (39.85 * aw_c ** 2) + (36 * aw_c ** 3)

    # calculate water diffusivity
    diff = 10 ** -6 * np.exp(2416 * (1 / 303 - 1 / 353)) * (2.563 - 0.33 * 10 + 0.0264 * 10 ** 2 - 0.000671 * 10 ** 3)
    delta_lambda = (11 * alpha / n) + C * np.exp((i * Mn * n) / (22 * F * den_dry * diff) * z)
    sigma = np.exp(1268 * (1 / 303 - 1 / T)) * 0.005193 * (delta_lambda - 0.00326)

    return sigma


# integrate thickness to calculate resistance
R = integrate.quad(mem_resistance, 0, 0.0050)

# calculate the voltage loss
i = 0.8
print(i * R[0])