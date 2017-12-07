from random import random
from math import sqrt
from time import clock



def main():
    N = 10000
    Nin = 0
    
    for i in range(N):
        x = random()
        y = random()

        dis = sqrt(x**2+y**2)
        
        if ( dis <= 1.0):
            
            Nin = Nin + 1
        pi = Nin/N*4
    print (pi)

main()

        
