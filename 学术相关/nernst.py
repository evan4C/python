def nernst():
    import math
    T=float(input("enter the temperature: "))
    R=8.314
    F=96485
    E0=float(input("enter E0: "))
    aRed=float(input("enter aRed: "))
    aOx=float(input("enter aOx: "))
    z=int(input("enter z: "))
    Y=E0-R*T/(z*F)*math.log(aRed/aOx, math.e)
    print("E= ",Y)

nernst()
