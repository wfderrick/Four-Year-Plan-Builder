import structs
from calculate import getvals, four_score

def keep_cards(cards, card_list):
    if len(card_list) == 4:
        
        return [four_score(card_list)] + card_list
    elif len(cards) == 0:
        return [-1, -1, -1, -1, -1]
    else:
        opt1 = keep_cards(cards[1:], card_list + [cards[0]])
        opt2 = keep_cards(cards[1:], card_list)
        if opt1[0] > opt2[0]:
            return opt1
        else:
            return opt2


def discard(cards, discard):
    keep = keep_cards(cards, [])[1:]
    for i in range(6):
        if cards[i] not in keep:
            discard.append(i + 1)

    return discard

def pegging(cur_val, prev, hand):
    vals = getvals(hand)
    if cur_val == 0:
        val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = next((x for x in vals if x == 10), None)
        if val == None:
            val = vals[0]
    elif cur_val <= 4:
        val = next((x for x in vals if x == prev), None)
        if val == None:
            val = next((x for x in vals if x == 10), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = vals[0]
    elif cur_val == 5:
        val = next((x for x in vals if x == 10 or x == 5), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = vals[0]
    elif cur_val < 10:
        val = next((x for x in vals if x + cur_val == 15), None)
        if val == None:
            val = next((x for x in vals if x == prev), None)
        if val == None:
            val = next((x for x in vals if x == 10), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = vals[0]
    elif cur_val == 10:
        val = next((x for x in vals if x == 5), None)
        if val == None:
            val = next((x for x in vals if x == prev), None)
        if val == None:
            val = next((x for x in vals if x == 10), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = vals[0]
    elif cur_val < 21:
        val = next((x for x in vals if x + cur_val == 15), None)
        if val == None:
            val = next((x for x in vals if x == prev), None)
        if val == None:
            val = next((x for x in vals if x == 10), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = vals[0]
    elif cur_val < 31:
        val = next((x for x in vals if x + cur_val == 31), None)
        if val == None:
            val = next((x for x in vals if x == prev), None)
        if val == None:
            val = next((x for x in vals if x == 10), None)
        if val == None:
            val = next((x for x in vals if x <= 9 and x > 5), None)
        if val == None:
            val = next((x for x in vals if x == 4 or x == 3), None)
        if val == None:
            val = next((x for x in vals if x == 2), None)
        if val == None:
            val = vals[0]


example_hand = [
    structs.Card(structs.Suit.SPADES, structs.Face.EIGHT, 8),
    structs.Card(structs.Suit.CLUBS, structs.Face.TEN, 10),
    structs.Card(structs.Suit.CLUBS, structs.Face.NINE, 9),
    structs.Card(structs.Suit.CLUBS, structs.Face.EIGHT, 8),
    structs.Card(structs.Suit.SPADES, structs.Face.JACK, 10),
    structs.Card(structs.Suit.HEARTS, structs.Face.EIGHT, 8),
]

