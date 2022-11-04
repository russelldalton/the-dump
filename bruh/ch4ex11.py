
from graphics import *

def main():
    win = GraphWin('design a house', 500, 500)
    win.setCoords(0,0,200,200)
    message = Text(Point(100,5),'')
    message.draw(win)

    message.setText('click bottom left')
    p1 = win.getMouse()
    p1.draw(win)
    message.setText('click upper right')
    p2 = win.getMouse()
    p1.undraw()
    Rectangle(p1, p2).draw(win)

    houseWidth= p2.getX() - p1.getX()
    doorWidth= 0.3 * houseWidth
    halfDoor = doorWidth/2.0
    message.setText('click top of door')
    p3 = win.getMouse()
    door=Rectangle(Point(p3.getX() - halfDoor,p1.getY()), Point(p3.getX() + halfDoor, p3.getY()))

    door.setFill('brown')
    door.draw(win)

    message.setText('click center of window')
    p4 = win.getMouse()
    Circle(p4, halfDoor).draw(win)

    message.setText('click top of roof')
    p5 = win.getMouse()
    roof = Polygon(Point(p1.getX(), p2.getY()), p5, p2)
    roof.draw(win)
    roof.setFill('grey')

    message.setText("you're done")
    win.getMouse()
    win.close()

main()
