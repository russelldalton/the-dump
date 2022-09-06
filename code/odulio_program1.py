import time
"""
program: odulio_program1.py
name: Jobe Odulio
description:prints hello world
date:9/1/2022
notes:uses import time
"""
#print "hello world"
print('hello world')



def main():
    #print name and class
    print ('Jobe Odulio')
    print ('CIS 110 Program 1')
    #print local time
    print (time.asctime(time.localtime(time.time())))
main()
