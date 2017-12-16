# drawing 

from graphics import *

def main():

    win = GraphWin("click me")
    win.setCoords(0.0,0.0,200.0,200.0)

    massage = Text(Point(100,10),"click 5 points")
    massage.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)

    polygon = Polygon(p1,p2,p3,p4,p5)
    polygon.setFill("blue")
    polygon.draw(win)

    massage.setText("click anywhere to quit")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
    

    
