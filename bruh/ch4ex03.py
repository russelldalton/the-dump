from graphics import *

def main(): 
    win = GraphWin('Portrait', 400, 400)
    win.setBackground('grey')
    
    
    Oval(Point(75,30), Point(325,375)).draw(win)

    lefteye=Circle(Point(160,160),15).draw(win)
    lefteye.setFill('red')
    righteye=lefteye.clone()
    righteye.move(80,0)
    righteye.draw(win)
    mouth=Line(Point(160,240),Point(240,240))
    mouth.setWidth(40)
    mouth.draw(win)

    nose=Polygon(Point(200,130),Point(220,210), Point(180,210)).draw(win)
    nose.setFill('black')

    win.getMouse()
    win.close()
        
    



main()
