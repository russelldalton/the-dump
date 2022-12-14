from random import randrange
from ch10ex11 import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in "cdhs":
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))

    def shuffle(self):
        n = len(self.cards)
        cards = self.cards
        for pos in range(n):
            randpos = randrange(pos, n)
            cards[pos], cards[randpos] = cards[randpos], cards[pos]
    
    def dealCard(self):
        return self.cards.pop()

    def cardsLeft(self):
        return len(self.cards)

def main():
    n = int(input('how many cards'))
    d =Deck()
    d.shuffle()
    hand = []
    for i in range(n):
        hand.append(d.dealCard())
    for card in hand:
        print(card,card.value())
if __name__=='__main__':
    main()
    
