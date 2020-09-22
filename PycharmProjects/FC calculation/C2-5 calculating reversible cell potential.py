# inputs

hf_H2 = 0  # enthalpy of formation at standard state(J/mol)
hf_O2 = 0  # enthalpy of formation at standard state(J/mol)
hf_H2Ol = -285826  # enthalpy of formation at standard state(J/mol)
sf_H2 = 130.68  # entropy of formation at standard state(J/mol)
sf_O2 = 205.14  # entropy of formation at standard state(J/mol)
sf_H2Ol = 69.92  # entropy of formation at standard state(J/mol)
T_ref = 298
T = 313
n = 2
F = 96487

# calculate gibbs free energy

delH = hf_H2Ol - (hf_H2 + (1/2) * hf_O2)
delS = sf_H2Ol - (sf_H2 + (1/2) * sf_O2)
delG = delH - (T_ref * delS)

# calculate the reversible potential

Er = delG / (-n * F)

Et = Er - (delS/(-n * F)) * (T - T_ref)

print(Er, Et)
