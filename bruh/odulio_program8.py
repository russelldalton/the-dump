import time
from graphics import *
"""
program: odulio_program8.py
name: Jobe Odulio
description: 
date:
notes:
"""





def main():
    #create window
    win = GraphWin('tik tac toe', 500, 500)
    win.setCoords(0,0,300,300)
    win.setBackground('blue')
    message = Text(Point(300, 500),'')
    message.draw(win)
    message.setText('tic-tac-toe')
    # boarders
    boarder1 = Line(Point(10, 100),Point(280,100))
    boarder1.setWidth(10)
    boarder1.draw(win)

    boarder2 = Line(Point(10, 190),Point(280,190))
    boarder2.setWidth(10)
    boarder2.draw(win)
 

    boarder3 = Line(Point(100, 10),Point(100,300))
    boarder3.setWidth(10)
    boarder3.draw(win)

    boarder4 = Line(Point(190, 10),Point(190,300))
    boarder4.setWidth(10)
    boarder4.draw(win)













    print ('Jobe Odulio')
    print ('CIS 110 Program 8')
    print (time.asctime(time.localtime(time.time())))
main()
