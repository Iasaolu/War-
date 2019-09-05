# A playing card object that has a value and a suit
from collections import deque

class Player(object):
    # instance variable
    # constructor
    def __init__(self,name,deck):
        self.deck = deque()
        self.name = name
        # for every card in THE DECK we are TAKING IN AS INPUT
        for x in deck:
            self.deck.append(x)