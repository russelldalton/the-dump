import random
import time
"""
program: 
name: Jobe Odulio
description:
date:
notes:
"""





def getinput():
    return int(input("enter number between 1 and 50: "))

def simgame(x):
    secret = random.randrange(0,50)
    
    
    
   
    while x != secret:
        if x<secret:
            print ('higher')
            x = getinput()
        elif x>secret:
            print ('lower')
            x = getinput()
        else:
            break
    print('you win the number was', x)
def main():
    n = getinput()
    simgame(n)

    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()        
        
        
        
    
    
    
            

        
        


    
