import math

class Card: 
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def value(self):
        if self.getRank()<10:
            return self.rank
        else: 
            return 10
    def __str__(self):
        ranks = [None, "ace", "two", "three","four","five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
        rankStr = ranks[self.rank]
        if self.suit == 'c':
            suitStr = "clubs"
        elif self.suit == 'd':
            suitStr = "diamonds"
        elif self.suit == 'h':
            suitStr = "hearts"
        else:
            suitStr = "spades"
        return "{0} of {1}".format(rankStr, suitStr)
from random import randrange 

def main():
    print('testing card classes')
    n = int(input('how many cards'))
    for i in range(n):
        rank = randrange(1,14)
        suit = "dchs"[randrange(4)]
        randCard = Card(rank,suit)
        print(randCard, "counts", randCard.value())
if __name__ == '__main__':
    main()
