"""
The molar fraction of H 2 in the fuel stream is 0.5 and
the molar fraction of O 2 in the oxidant stream is 0.21.
The remaining species are chemically inert.
"""

# inputs
import math

R = 8.314
T = 298
n = 2
F = 96487
Er = 1.229
x_h2 = 0.5
x_o2 = 0.21

E = Er - (R * T / (n * F)) * math.log(x_h2 ** (-1) * x_o2 ** (-0.5))
print(E)