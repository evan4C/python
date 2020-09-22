import numpy as np
import matplotlib.pyplot as plt

# inputs

U = 400
Uf = 334.86
Ug = 2482.2
Sf = 1.0753
Sg = 7.6122

# calculate the mole fraction of the mixture

X = (U - Uf)/(Ug - U)

# calculate the entropy

S = ((1 - X) * Sf) + X * Sg
print(S)


