from random import randrange
import time
"""
program: 
name: Jobe Odulio
description:
date:
notes:
"""


def main():
    n = getinputs()
    simgame(n)

def getinputs():
    return eval(input("enter number between 1 and 50: "))

def simgame(input):
    secret = range(51)
    
    if input == secret:
        print ("you win the number was", input)
    elif input < secret:
        print ("higher")
        getinputs(input)
    elif input > secret:
        print ("lower")
        getinputs(input)
            
        
        
        
    
    
    
            

        
        


    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()
