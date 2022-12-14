from random import randrange, seed 

def main():
    printIntro()
    n = getInputs()
    wins = simNGames(n)
    printResults(wins, n)



def printIntro():
    print('its gambling time')

def getInputs():
    return eval(input('number of games: '))

def simNGames(n):
    wins = 0 
    for i in range(n):
        if winCraps():
            wins = wins +1
    return wins

def winCraps():
    roll = rollDice()
    if roll == 7 or roll == 11:
        return True
    elif roll == 2 or roll == 3 or roll == 12:
        return False
    else:
        return rollForPoint(roll)

def rollForPoint(point):
    roll = rollDice()
    while roll != 7 and roll != point:
        roll = roll = rollDice()
    return roll == point

def rollDice():
    return randrange(1,7) + randrange(1,7)

def printResults(wins, n):
    print('\nthe player wins', wins)
    print(' the probability of winning is {0:0.2%}'. format(wins/n))




if __name__=="__main__": main()
