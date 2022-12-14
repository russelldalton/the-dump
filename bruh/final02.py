import time
"""
program: 
name: Jobe Odulio
description:
date:
notes:
"""





def main():
    n = []
    #sentinal loop
    while n == []:
        for i in range (7):
            prompt = str(input("enter a word "))
            n = [prompt.upper(), prompt.lower(), prompt[len(prompt)-1]]
            print(n)
        
    
    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()
