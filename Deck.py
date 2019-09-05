import Card

# A standard deck that contains cards with four suits (spades (s), clubs (c), hearts (h), diamonds (d))
# and values ranging from 2 to 14 (11 is Jack, 12 is Queen, 13 is King, 14 is Ace)


class Deck:
    deck = []
    for x in range(52):
        if x <= 12:
            deck.append(Card.Card(x % 13 + 2, 's'))
        elif x <= 25:
            deck.append(Card.Card(x % 13 + 2, 'c'))
        elif x <= 38:
            deck.append(Card.Card(x % 13 + 2, 'h'))
        else:
            deck.append(Card.Card(x % 13 + 2, 'd'))
