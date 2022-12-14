from random import random, seed 

def main():
    seed(123456)
    printIntro()
    n = getInputs()
    printNumbers(n)

def printIntro():
    print('seeds')

def getInputs():
    return eval(input('number of values to print: '))

def printNumbers(n):
    for x in range(n):
        print('{:0.5f}'.format(random()))


if __name__=="__main__": main()

