import time
"""
program: final 1
name: Jobe Odulio
description:
date:
notes:
"""





def main():
    #user input
    n= eval(input("enter number "))
    r = range(1,11)
    print()
    print(    n,   n)
    print('------------------------')
    #print table 
    for i in r:
        for j in r:
            m = n * j 
            print(i * j, end="\t")

       

    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()
