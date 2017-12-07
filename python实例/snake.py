import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle)
    turtle.fd(rad) # move forward and draw
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 30 # the width of the pen
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40) # setup angle,0=east,90=north,180=west,270=south
    drawSnake(40,80,5,pythonsize/2)

main()
