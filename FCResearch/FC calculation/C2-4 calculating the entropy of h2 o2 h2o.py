import math
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# font configuration
font = FontProperties(weight='bold', size=12)

# inputs

R = 8.314
T = np.arange(300, 1001, 50)
sf_h2 = 130.57
sf_o2 = 205.03
sf_h2o = 188.72
s_h2 = []
s_o2 = []
s_h2o = []

for t in T:
    st_h2 = math.log10(24.42) + 22.26e-3 * (t - 298) - 24.2e-6 * (t ** 2 - 298 ** 2) + \
        15.3e-9 * (t ** 3 - 298 ** 3) - 3.78e-12 * (t ** 4 - 298 ** 4)
    s_h2.append(sf_h2 + st_h2)

    st_o2 = math.log10(30.15) - 15.6e-3 * (t - 298) + 29.33e-6 * (t ** 2 - 298 ** 2) - \
        18.7e-9 * (t ** 3 - 298 ** 3) + 4.48e-12 * (t ** 4 - 298 ** 4)
    s_o2.append(sf_o2 + st_o2)

    st_h2o = math.log10(33.84) - 9.216e-3 * (t-298) + 17.26e-6 * (t ** 2 - 298 ** 2) - \
        8.21e-9 * (t ** 3 - 298 ** 3) + 1.67e-12 * (t ** 4 - 298 ** 4)
    s_h2o.append(sf_h2o + st_h2o)

plt.plot(T, s_h2, label='H2')
plt.plot(T, s_o2, label='O2')
plt.plot(T, s_h2o, label='H2O')
plt.legend()
plt.title("Hydrogen, Oxygen and Water Entropy", fontproperties=font)
plt.xlabel("Temperature (K)", fontproperties=font)
plt.ylabel("Entropy (KJ/kg)", fontproperties=font)
plt.grid(True)
plt.show()
