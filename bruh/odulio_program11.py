
from ch11ex15 import Deck 
from ch10ex11 import Card
from random import randrange, seed
import time
"""
program: odulio_program11.py
name: Jobe Odulio
description:blackjack
date:
notes:
"""


#player hand
def dealplayer(deck):
    hand = []
    for j in range(5):
        rank = randrange(1,14)
        suit = "dchs" [randrange(4)]
        randCard = Card(rank,suit)
        return randCard
        return randCard.value
    for i in range(2):
        deck = Deck()
        hand.append(deck)
    return hand
#dealer hand
def dealdealer(deck):
    hand2 = []
    for j in range(5):
        rank = randrange(1,14)
        suit = "dchs" [randrange(4)]
        randCard = Card(rank,suit)
        return randCard
        return randCard.value
    for j in range(2):
        deck2 = Deck()
        hand2.append(deck)
    return hand2



    



def simgames(hand, hand2):
    wins = 0 
    for i in range(5):
        if winblackjack():
            wins = wins +1
    return wins





#win condition 
def winblackjack():
    
    
    
    print ("player hand", dealplayer(Deck))
        
        
    print ("Dealer hand", dealdealer(Deck))
        
    #if dealplayer(Deck) >= dealdealer(Deck):
        #print ('winner')
    #else:
        #print ('youre done')
    
    
    
    







def main():
    player = 0
    dealer = 0
    print (simgames(player, dealer))
    n  = eval(input("hit(1) or stand(2)?: "))
    if n == 1:
        for i in range(1):
            print ('new card', dealplayer(player))
    if n == 2:
        print ('done')
    
    print ('Jobe Odulio')
    print ('CIS 110 Program ')
    print (time.asctime(time.localtime(time.time())))
main()
