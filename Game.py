import Card
import Deck
import Player
import random
#declare a new instance of deck class
#wardeck object
warDeck = Deck.Deck

#randomizing the cards in the deck of the wardeck object
random.shuffle(warDeck.deck)
def comparecards(a,b):
    print("\n------------------------")
    if a.number > b.number:
        print("Player 1 WINS")
        PlayerOne.deck.append(a)
        PlayerOne.deck.append(b)
        printResults()
    elif b.number > a.number:
        print("Player 2 WINS")
        PlayerTwo.deck.append(a)
        PlayerTwo.deck.append(b)
        printResults()
    else:
        print("Tie")
        PlayerOne.deck.append(a)
        PlayerTwo.deck.append(b)
        printResults()
    print("------------------------\n")


def printResults():
    print(PlayerOne.name + "'s Deck Size: " + str(len(PlayerOne.deck)))
    print(PlayerTwo.name + " 's Two Deck Size: " + str(len(PlayerTwo.deck)))

# Split the deck in half and assign each to a new player (2 Players)
#constructing two player objects
PlayerOne = Player.Player("Ikponwonsa", warDeck.deck[:26])
PlayerTwo = Player.Player("Akash", warDeck.deck[26:])

#new variable called prompt
prompt = input("Would you like to play a round of war?: ")

while prompt == "y" or prompt == "Y" or prompt == "yes" or prompt == "YES":
    random.shuffle(PlayerOne.deck)
    random.shuffle(PlayerTwo.deck)
    commit = input("\nPlayerOne Hit A to play: ")
    if commit == "A" or commit == "a":
        current_card1 = PlayerOne.deck.pop()
        print("P1's Card: " + str(current_card1.number) + current_card1.suit)

    commit = input("\nPlayerTwo Hit B to play: ")
    if commit == "B" or commit == "b":
        current_card2 = PlayerTwo.deck.pop()
        print("P2's Card: " + str(current_card2.number) + current_card2.suit)

    comparecards(current_card1, current_card2)

    prompt = input("Would you like to play again? ")

# 'play a round of war' = take the top two cards from each player's deck and compare them. the winner gets both cards
# print out total number of cards in each players deck (after round, to see who's winning)

print("\n---------------------------------------------------------\n")
print("Exiting Game\n")
print("Results:\n")
printResults()
print()
if len(PlayerOne.deck) > len(PlayerTwo.deck):
    print("Player One Wins!!")
elif len(PlayerOne.deck) == len(PlayerTwo.deck):
    print("It's a TIE!")
else:
    print("Player Two Wins!!")


# declare winner (print out how many card each player has, and print the WINNER's NAME, i.e. winner: ik)


