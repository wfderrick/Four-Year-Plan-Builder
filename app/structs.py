from enum import Enum


class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return f"{self.face.name} of {self.suit.name}"


class Hand:
    def __init__(self, card1, card2, card3, card4, card5, card6):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5
        self.card6 = card6

    def __str__(self):
        track = 1
        for i in range(1, 7):
            match i:
                case 1:
                    if self.card1 != -1:
                        print(f"{track}: {self.card1}")
                        track += 1
                case 2:
                    if self.card2 != -1:
                        print(f"{track}: {self.card2}")
                        track += 1
                case 3:
                    if self.card3 != -1:
                        print(f"{track}: {self.card3}")
                        track += 1
                case 4:
                    if self.card4 != -1:
                        print(f"{track}: {self.card4}")
                        track += 1
                case 5:
                    if self.card5 != -1:
                        print(f"{track}: {self.card5}")
                        track += 1
                case 6:
                    if self.card6 != -1:
                        print(f"{track}: {self.card6}")
                        track += 1
        return ""

    def remove(self, num1, num2, crib):
        for i in range(1, 7):
            match i:
                case 1:
                    if num1 == 1 or num2 == 1:
                        crib.append(self.card1)
                        self.card1 = -1
                case 2:
                    if num1 == 2 or num2 == 2:
                        crib.append(self.card2)
                        self.card2 = -1
                case 3:
                    if num1 == 3 or num2 == 3:
                        crib.append(self.card3)
                        self.card3 = -1
                case 4:
                    if num1 == 4 or num2 == 4:
                        crib.append(self.card4)
                        self.card4 = -1
                case 5:
                    if num1 == 5 or num2 == 5:
                        crib.append(self.card5)
                        self.card5 = -1
                case 6:
                    if num1 == 6 or num2 == 6:
                        crib.append(self.card6)
                        self.card6 = -1


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
