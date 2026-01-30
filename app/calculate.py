import structs
import copy


def score(hand_cards, starter):
    total = 0
    for i in range(4):
        if (
            hand_cards[i].face == structs.Face.JACK
            and hand_cards[i].suit == starter.suit
        ):
            total += 1

    val_list = getvals(hand_cards + [starter], [])
    card_list = hand_cards + [starter]
    total += count15s(val_list, 0)
    total += runs(card_list, 0, -1, maxrun(card_list, False), False)
    total += pairs(card_list)
    total += flush(hand_cards, starter)
    return total

def four_score(hand):
    total = 0
    val_list = getvals(hand, [])
    total += count15s(val_list, 0)
    total += runs(hand, 0, -1, maxrun(hand, True), True)
    total += pairs(hand)
    total += flush(hand, structs.Card(structs.Suit.NONE, 0, 0))
    return total

def getvals(cards, vals):
    for i in cards:
        vals.append(i.value)

    return vals


def count15s(cards, sum):
    if sum == 15:
        return 2
    elif len(cards) == 0:
        return 0
    else:
        return count15s(cards[1:], sum) + count15s(cards[1:], sum + cards[0])


def maxrun(cards, four):
    run_len = 0
    runs_list = []
    runs_list = listruns(cards, 0, -1, runs_list, four)
    if max(runs_list) < 3:
        return 3
    else:
        run_len = max(runs_list)
    return run_len


def runs(cards, length, prev, run_len, four):
    if prev == -1:
        if four != True:
            return (
            runs(cards[1:], 1, cards[0], run_len, four)
            + runs([cards[0]] + cards[2:], 1, cards[1], run_len, four)
            + runs(cards[:2] + cards[3:], 1, cards[2], run_len, four)
            + runs(cards[:3] + cards[4:], 1, cards[3], run_len, four)
            )
        else:
            return (
            runs(cards[1:], 1, cards[0], run_len, four)
            + runs([cards[0]] + cards[2:], 1, cards[1], run_len, four)
            + runs(cards[:2] + cards[3:], 1, cards[2], run_len, four)
            )
    elif len(cards) == 0:
        if length >= run_len:
            return length
        else:
            return 0
    else:
        check = False
        add = 0
        for i in range(len(cards)):
            if cards[i].face.value == prev.face.value + 1:
                check = True
                temp_cards = copy.deepcopy(cards)
                next = temp_cards.pop(i)
                add += runs(temp_cards, length + 1, next, run_len)
        if check == False:
            if length >= run_len:
                return length
            else:
                return 0
        else:
            return add


def listruns(cards, length, prev, runs_list, four):
    if prev == -1:
        if four != True:
            return (
            listruns(cards[1:], 1, cards[0], runs_list, four)
            + listruns(cards[2:] + [cards[0]], 1, cards[1], runs_list, four)
            + listruns(cards[:2] + cards[3:], 1, cards[2], runs_list, four)
            + listruns(cards[:3] + cards[4:], 1, cards[3], runs_list, four)
            )
        else:
            return (
            listruns(cards[1:], 1, cards[0], runs_list, four)
            + listruns(cards[2:] + [cards[0]], 1, cards[1], runs_list, four)
            + listruns(cards[:2] + cards[3:], 1, cards[2], runs_list, four)
            )
    elif len(cards) == 0:
        return runs_list + [length]
    else:
        for i in range(len(cards)):
            if (cards[i].face.value) == (prev.face.value + 1):
                temp_cards = copy.deepcopy(cards)
                next = temp_cards.pop(i)
                return listruns(temp_cards, length + 1, next, runs_list)
        return runs_list + [length]


def pairs(cards):
    total = 0
    for i in range(len(cards)):
        for j in range((i + 1), (len(cards))):
            if cards[i].face == cards[j].face:
                total += 2
    return total


def flush(hand, starter):
    if (
        hand[0].suit == hand[1].suit
        and hand[1].suit == hand[2].suit
        and hand[2].suit == hand[3].suit
    ):
        if starter.suit == hand[0].suit:
            return 5
        else:
            return 4
    return 0


example_hand = [
    structs.Card(structs.Suit.CLUBS, structs.Face.JACK, 10),
    structs.Card(structs.Suit.DIAMONDS, structs.Face.FIVE, 5),
    structs.Card(structs.Suit.SPADES, structs.Face.FIVE, 5),
    structs.Card(structs.Suit.HEARTS, structs.Face.FIVE, 5),
]
score(example_hand, structs.Card(structs.Suit.CLUBS, structs.Face.FIVE, 5))
