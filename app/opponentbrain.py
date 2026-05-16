import structs
from calculate import four_score


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
    val = -1
    if cur_val == 0:
        val = next((x for x in hand if x.value == 4 or x.value == 3), None)
        if val == None:
            val = next((x for x in hand if x.value <= 9 and x.value > 5), None)
        if val == None:
            val = next((x for x in hand if x.value == 2), None)
        if val == None:
            val = next((x for x in hand if x.value == 10), None)
        if val == None:
            val = hand[0]
    elif cur_val <= 4:
        val = next((x for x in hand if x.rank == prev.rank), None)
        if val == None:
            val = next((x for x in hand if x.value == 10), None)
        if val == None:
            val = next((x for x in hand if x.value <= 9 and x.value > 5), None)
        if val == None:
            val = next((x for x in hand if x.value == 4 or x.value == 3), None)
        if val == None:
            val = next((x for x in hand if x.value == 2), None)
        if val == None:
            val = hand[0]
    elif cur_val == 5:
        val = next((x for x in hand if x.value == 10 or x.rank == prev.rank), None)
        if val == None:
            val = next((x for x in hand if x.value <= 9 and x.value > 5), None)
        if val == None:
            val = next((x for x in hand if x.value == 4 or x.value == 3), None)
        if val == None:
            val = next((x for x in hand if x.value == 2), None)
        if val == None:
            val = hand[0]
    elif cur_val < 10:
        val = next((x for x in hand if x.value + cur_val == 15), None)
        if val == None:
            val = next((x for x in hand if x.rank == prev.rank), None)
        if val == None:
            val = next((x for x in hand if x.value == 10), None)
        if val == None:
            val = next((x for x in hand if x.value <= 9 and x.value > 5), None)
        if val == None:
            val = next((x for x in hand if x.value == 4 or x.value == 3), None)
        if val == None:
            val = next((x for x in hand if x.value == 2), None)
        if val == None:
            val = hand[0]
    elif cur_val == 10:
        val = next((x for x in hand if x.value == 5), None)
        if val == None:
            val = next((x for x in hand if x.rank == prev.rank), None)
        if val == None:
            val = next((x for x in hand if x.value == 10), None)
        if val == None:
            val = next((x for x in hand if x.value <= 9 and x.value > 5), None)
        if val == None:
            val = next((x for x in hand if x.value == 4 or x.value == 3), None)
        if val == None:
            val = next((x for x in hand if x.value == 2), None)
        if val == None:
            val = hand[0]
    elif cur_val < 21:
        val = next((x for x in hand if x.value + cur_val == 15), None)
        if val == None:
            val = next((x for x in hand if x.rank == prev.rank), None)
        if val == None:
            val = next((x for x in hand if x.value == 10), None)
        if val == None:
            val = next((x for x in hand if x.value <= 9 and x.value > 5), None)
        if val == None:
            val = next((x for x in hand if x.value == 4 or x.value == 3), None)
        if val == None:
            val = next((x for x in hand if x.value == 2), None)
        if val == None:
            val = hand[0]
    elif cur_val < 31:
        val = next((x for x in hand if x.value + cur_val == 31), None)
        if val == None:
            val = next((x for x in hand if x.rank == prev.rank and cur_val + prev.rank.value <= 31), None)
        if val == None:
            val = next((x for x in hand if x.value == 10 and cur_val + 10 <= 31), None)
        if val == None:
            val = next(
                (
                    x
                    for x in hand
                    if x.value <= 9 and x.value > 5 and cur_val + x.value <= 31
                ),
                None,
            )
        if val == None:
            val = next(
                (
                    x
                    for x in hand
                    if (x.value == 4 or x.value == 3) and cur_val + x.value <= 31
                ),
                None,
            )
        if val == None:
            val = next(
                (
                    x
                    for x in hand
                    if (x.value == 2 or x.value == 1) and cur_val + x.value <= 31
                ),
                None,
            )
    if val == None:
        val = -1
    return val


example_hand = [
    structs.Card(structs.Suit.SPADES, structs.Rank.EIGHT, 8),
    structs.Card(structs.Suit.CLUBS, structs.Rank.TEN, 10),
    structs.Card(structs.Suit.CLUBS, structs.Rank.NINE, 9),
    structs.Card(structs.Suit.CLUBS, structs.Rank.EIGHT, 8),
    structs.Card(structs.Suit.SPADES, structs.Rank.JACK, 10),
    structs.Card(structs.Suit.HEARTS, structs.Rank.EIGHT, 8),
]

