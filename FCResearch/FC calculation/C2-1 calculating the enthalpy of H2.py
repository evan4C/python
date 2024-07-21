# UnitSystem SI

# Inputs
V = 1.696  # Specific Volume (m3/kg)
U = 2506.7  # Specific Internal Energy (kJ/kg)
# Conversions
# 1 psi = 6894.76 N/m2
# 1 kJ = 1000 N*m
P = 6894.76/1000
H = U + P * V
print(H)
