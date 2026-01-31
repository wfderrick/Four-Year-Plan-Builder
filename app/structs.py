from enum import Enum

# Card object used to represent cards in a deck. Each card object has three attributes
# which are suit, face, and value. Suit represents the suit of the card (Clubs, Spades, Hearts, Diamonds, None (For use in code in specific cases)). 
# Face represents the face value of the card (Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, None (For use in code in specific cases)).
# Value represent the value of the card in the game cribbage (Ace = 1, Face cards = 10, every other card = to its face value).
class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return f"{self.face.name} of {self.suit.name}"

# Hand object which represents the player's and the computer's hands. There is a single attribute which is the hand attribute which
# is a list of Card objects
class Hand:
    def __init__(self, card1, card2, card3, card4, card5, card6):
        self.hand = [card1, card2, card3, card4, card5, card6]

    def __str__(self):
        track = 1
        for i in self.hand:
            print(f"{track}: {i}")
            track += 1
        return ""

    def remove(self, num1, num2, crib):
        for i in range(len(self.hand)):
            if num1  == i + 1 :
                if num2 == -1:      
                    crib.append(self.hand[i - 1])
                    self.hand.pop(i - 1)
                else:
                    crib.append(self.hand[i])
                    self.hand.pop(i)
                num1 = -1
                
            elif num2 == i + 1:
                if num1 == -1:      
                    crib.append(self.hand[i - 1])
                    self.hand.pop(i - 1)
                else:
                    crib.append(self.hand[i])
                    self.hand.pop(i)
                num2 = -1
class Suit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    NONE = 5


class Face(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    NONE = 14

CONST_CARDS = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
]
