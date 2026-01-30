import calculate
import structs
def discard(cards, card_list):
    if len(card_list) == 4:
        return [calculate.four_score(card_list)] + card_list
    elif len(cards) == 0:
        return [-1, -1, -1, -1, -1]
    else:
        opt1 = discard(cards[1:], card_list + [cards[0]])
        opt2 = discard(cards[1:], card_list)
        if opt1[0] > opt2[0]:
            opt1[1:]
        else:
            opt2[2:]
    


example_hand = [
    structs.Card(structs.Suit.CLUBS, structs.Face.JACK, 10),
    structs.Card(structs.Suit.DIAMONDS, structs.Face.FIVE, 5),
    structs.Card(structs.Suit.SPADES, structs.Face.FIVE, 5),
    structs.Card(structs.Suit.HEARTS, structs.Face.FIVE, 5), structs.Card(structs.Suit.SPADES, structs.Face.FOUR, 5),structs.Card(structs.Suit.HEARTS, structs.Face.FOUR, 5)
]
print(discard(example_hand, []))