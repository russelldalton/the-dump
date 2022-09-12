import time
"""
program: odulio_program2.py
name: Jobe Odulio
description: calculates time by deviding distance with speed of light 
date:9/12/2022
notes:this program is used to se how long it takes for a rover in mars to send a picture to nasa
"""
def main():
    #introduction
    print('this program calculates the time it takes for a photo taken from curiosity to reach nasa')
    #time calculator
    distance = eval(input("What is the distance in miles? "))
    time =  distance/186000
    #display output
    print("The time it takes for curiosity to reach nasa is", time,'seconds' )
main()




def main():
    print ('Jobe Odulio')
    print ('CIS 110 Program 2')
    print (time.asctime(time.localtime(time.time())))
main()
