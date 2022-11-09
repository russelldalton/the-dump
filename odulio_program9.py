import time
from random import randrange, seed 
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

def simNGames(n):
    wins = [0,0,0,0,0,0]
    for i in range(n):
        for h in range (5):
            wins[h] = draw()
            
                
            
            
        wins[5]= winPowerBall()
            
      
        print (wins)
def draw():
    return randrange(1,69)
def winPowerBall():
    ball = draw()
    if ball <= 26:
        return ball
    elif ball >26:
        return ball
    else:
        return drawForPoint()
def drawForPoint(point):
    draw = draw()
    while draw != 70 and draw != point:
          draw = draw()
    return draw == point


def printResults(wins, n):
    print('\nthe player wins', wins)
    print(' the probability of winning is {0:0.2%}'. format(wins/n))








def main():
    seed(123456)
    printIntro()
    n = getInputs()
    wins = simNGames(n)
    printResults(wins, n)
    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
if __name__=="__main__": main()
