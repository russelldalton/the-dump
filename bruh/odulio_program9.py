import time
from random import *
"""
program: odulio_program9.py
name: Jobe Odulio
description:powerball sim
date:
notes:
"""






def printIntro():
    print('its gambling time')

def getInputs():
    return eval(input('number of draws: '))
#draw
def draw():
    return randrange(1,69)
#draw non powerballs
def drawForPoint():
    draw1 = draw()
    while draw1 >=26:
          draw1 = draw()
    return draw1 




#check for powerball

def winPowerBall():
    ball = draw()
    if ball <= 26:
        return ball
    else:
        return drawForPoint()

#simulate the game
    
def simNGames(n):
    
    wins = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        for j in range (5):
            if draw() != wins[0] != wins[1] != wins [2] != wins[3] != wins[4] != wins[5]:
                wins[j] = draw()
                j = j +1
                print (wins[j])
            else:    
                continue
        wins[5]= winPowerBall()
        print( 'powerball: ', wins[5])   
      
        




    











def main():
    seed(123456)
    printIntro()
    n = getInputs()
    simNGames(n)
    
    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
if __name__=="__main__": main()

