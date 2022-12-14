from random import randrange 
from graphics import *
from button import Button 

def main():

    win = GraphWin("three button monte", 350, 100)
    win.setCoords(0,0,6,3)
    b1 = Button(win, Point(1,2), 1.5, 1, '1')
    b1.activate()
    b2 = Button(win, Point(3,2), 1.5, 1, '2')
    b2.activate()
    b3 = Button(win, Point(5,2), 1.5, 1, '3')
    b3.activate()


    m = Text(Point(3, .75), 'guess')
  
    m.draw(win)

    secret = randrange(1,4)

    choice = None
    while choice == None:
        pt  = win.getMouse()
        for button in [b1,b2,b3]:
            if button.clicked(pt):
                choice = button
    
    choiceNum = int(choice.getLabel()[-1])
    if choiceNum == secret:
        m.setText('you win')
    else:
        m.setText("you lose, you're done. the answer was door{0}".format(secret))

    win.getMouse()
    win.close()
if __name__ == '__main__':
    main()

