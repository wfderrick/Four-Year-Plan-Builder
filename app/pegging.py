import copy
from structs import Card, Suit, Rank


def full_run(cards):
    cards.sort(key=lambda card: card.rank.value)
    last = cards[0].rank.value
    for i in cards[1:]:
        if i.rank.value != last + 1:
            return False
        else:
            last += 1
    return True


def seq_pairs(cards):
    points = 0
    og = cards[0].rank
    mult = 1
    for i in cards[1:]:
        if i.rank == og:
            points += (2 * mult)
            mult += 1
        else:
            return points
    return points


def peg_score(prev_cards, new_card, cur_val):
    info = [0, 0]
    peg_len = len(prev_cards)
    combined = copy.deepcopy(prev_cards)
    combined.append(new_card)
    if cur_val + new_card.value == 15 or cur_val + new_card.value == 31:
        info[0] += 2

    
    info[0] += seq_pairs(combined[::-1])

    additive = [] 
    for i in combined[::-1]:
        score = 0
        additive.append(i)
        if len(additive) > 2:
            check = full_run(additive)
            if check:
                score = len(additive)

    info[0] += score

    
    info[1] = cur_val + new_card.value

    return info

print(peg_score([Card(Suit.HEARTS, Rank.SIX, 6)], Card(Suit.SPADES, Rank.SIX, 6), 12))


"""def computer_pegging():
    if cur_val == 31:
                input("31 was reached so the pegging will reset to 0.")
                cur_val = 0
                go = False
            if go == True:
                if len(p2_pegging) > 0:
                    if len(prev_cards) > 0:
                        card = pegging(cur_val, prev_cards[len(prev_cards) -1], p2_pegging)
                    else:
                        card = pegging(cur_val, [], p2_pegging)
                    if card == -1:
                        go == False
                        cur_val = 0
                        prev_cards = []
                        last_player = 2
                    else:
                        (p2_score, val) = peg_score(prev_cards, card, cur_val)
                        player2_score[0] += p2_score + 1
                        cur_val = val
                        p2_pegging.remove(card)
                else:
                    last_player = 2
                    cur_val = 0
                    prev_cards = []
                    go = False
            else:
                if len(p2_pegging) > 0:
                    if len(prev_cards) > 0:
                        card = pegging(cur_val, prev_cards[len(prev_cards) - 1], p2_pegging)
                    else:
                        card = pegging(cur_val, [], p2_pegging)
                    if card == -1:
                        go = True
                        p1_peg_score += 1
                        last_player = 2
                    else:
                        (p2_score, val) = peg_score(prev_cards, card, cur_val)
                        player2_score[0] += p2_score
                        cur_val = val
                        p2_pegging.remove(card)
                        last_player = 2
                else:
                    last_player = 2
                    go = False
            if card == -1:
                print(f"The computer couldn't play.")
            else:
                print(f"Computer Played: {card}")
            print(f"The current value is: {cur_val}")"""
            