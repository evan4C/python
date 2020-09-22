"""
Use the activation overpotential equation derived from the Butler-Volmer equation to calculate and
plot the activation losses for a fuel cell
operating at a current density of 0.7 A/cm2 , a = 0.5, and an exchange current density of 10^−6.912 at
(1) a temperature range from 300 to 400 K and
(2) a current density from 0 to 1 A at increments of 0.01 and a temperature of 300 K.
"""
import numpy as np
import matplotlib.pyplot as plt


# inputs

R = 8.314
F = 96487
alpha = 0.5
i0 = 10 ** (-6.912)

# constant current density with temperature range

i = 0.7
T = np.arange(300, 401, 1)

b = R * T / (2 * alpha * F)
v_act = b * np.log10(i/i0)  # Tafel equation

plt.subplots()
plt.plot(T, v_act)
plt.title("activation loss as a function of temperature")
plt.xlabel("temperature(K)")
plt.ylabel("activation loss(V)")
plt.grid()

# constant temperature with current density range

i2 = np.arange(0, 1.01, 0.01)
T2 = 300

b2 = R * T2 / (2 * alpha * F)
v_act2 = b2 * np.log10(i2/i0)

plt.subplots()
plt.plot(i2, v_act2)
plt.title("activation loss as a function of current density")
plt.xlabel("current density(A/cm^2)")
plt.ylabel("activation loss(V)")
plt.grid()
plt.show()


