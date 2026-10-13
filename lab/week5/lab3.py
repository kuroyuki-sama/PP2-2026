# Card와 Deck (p.572)

class Card:
    suitNames = ['클럽', '다이아몬드', '스페이드', '하트']
    rankNames = [None,'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, rank):
        self.suit, self.rank = suit, rank   

    def __str__(self):
        return self.suitNames[self.suit] + " " + self.rankNames[self.rank]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        lst = [str(cards) for cards in self.cards] 
        return str(lst)

deck = Deck()
print(deck)
    