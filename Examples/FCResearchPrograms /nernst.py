def nernst():
    import math
    T=eval(input("enter the temperature: "))
    R=8.314
    F=96485
    E0=eval(input("enter E0: "))
    aRed=eval(input("enter aRed: "))
    aOx=eval(input("enter aOx: "))
    z=eval(input("enter z: "))
    Y=E0-R*T/(z*F)*math.log(aRed/aOx, math.e)
    print("E= {}".format(Y))

nernst()
