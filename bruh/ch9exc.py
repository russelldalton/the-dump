from random import randrange, seed 

def main():
    seed(123456)
    printIntro()
    n = getInputs()
    #printNumbers(n)
    results = generateSamples(n)
    printSummary(results)

def generateSamples(n):
    results = [0,0,0,0,0,0]
    for i in range(n):
        sample=randrange (0,6)
        results[sample]=results[sample]+1
    return results

def printSummary(results):
    total = sum(results)
    for i in range(0,6):
        print("{}: {:6.2%}".format(i, results[i]/total))

def printIntro():
    print('uniform distribution')

def getInputs():
    return eval(input('number of values to print: '))

#def printNumbers(n):
    #for x in range(n):
        #print('{:0.5f}'.format(randrange()))


if __name__=="__main__": main()
