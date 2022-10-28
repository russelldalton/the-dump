import time
"""
program:odulio_program7.py 
name: Jobe Odulio
description:prints table of wind chill values
date:10/27/2022
notes:
"""
#calculate windchill
def windchill(temp, velocity):
    if (velocity <= 3):
        return temp
    elif (velocity > 3):

        windtemp = 35.74 + 0.6215 * temp - 35.75*(velocity**0.16) + 0.4275*temp*(velocity**0.16)
        return windtemp



def main():
    temp = 0
    velocity = 0
    print ('{temp:^}'.format(temp = 'temperature'))
    print ('{mph:<}{a:<}{b:<}{c:<}{d:<}{e:<}{f:<}{g:<}{h:<}{i:<}'.format(mph = 'MPH|', a= ' -20', b=' -10', c=' 0', d=' 10', e=' 20', f= ' 30', g= ' 40', h = ' 50', i = ' 60'))
    for i in range(3):
        for j in range(3):
            
            
            print('{mph:<}{a:<f}{b:<f}{c:<f}{d:<f}{e:<f}{f:<f}{g:<f}{h:<f}{i:<f}'.format(mph = str(temp)+'|', a= windchill(temp, -20), b= windchill(temp, -10), c= windchill(temp, 0), d= windchill(temp, 10), e= windchill(temp, 20), f= windchill(temp, 30), g= windchill(temp, 40) , h = windchill(temp, 50), i = windchill(temp, 60)))
            temp += 5
    print()


    print ('Jobe Odulio')
    print ('CIS 110 Program 7')
    print (time.asctime(time.localtime(time.time())))
main()
