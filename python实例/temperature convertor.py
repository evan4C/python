# temperature convert

from graphics import *

def main():

    win = GraphWin("convetor",400,300)
    win.setCoords(0.0,0.0,3.0,4.0)

    Text(Point(1,3),"Celsius Temperature:").draw(win)
    Text(Point(1,1),"Fahrenheit Temperature:").draw(win)
    inPut = Entry(Point(2,3),5)
    inPut.setText("0")
    inPut.draw(win)
    outPut = Text(Point(2,1),"")
    outPut.draw(win)
    button = Text(Point(1.5,2.0),"convert it")
    button.draw(win)
    Rectangle(Point(1,1.5),Point(2,2.5)).draw(win) # 按钮框

    win.getMouse()

    c = eval(inPut.getText())
    f = 9.0 / 5.0 * c + 32.0

    outPut.setText(f)
    button.setText("quit")

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
    
    
