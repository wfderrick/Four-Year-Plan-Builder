import copy

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
    pair = cards[0].rank.value
    for i in cards[1:]:
        if i.rank.value == pair:
            points += 2
        else:
            return points
    return points


def peg_score(prev_cards, new_card, cur_val):
    info = [0, 0]
    peg_len = len(prev_cards)
    prev_cards.append(new_card)
    combined = copy.deepcopy(prev_cards)
    if cur_val + new_card.value == 15 or cur_val + new_card.value == 31:
        info[0] += 2

    if peg_len >= 3:
        info[0] += seq_pairs(combined[peg_len - 4 :])
    elif peg_len >= 2:
        info[0] += seq_pairs(combined[peg_len - 3 :])
    elif peg_len == 1:
        info[0] += seq_pairs(combined[peg_len - 2 :])
    additive = [] 
    for i in combined[::-1]:
        score = 0
        additive.append(i)
        if len(additive) > 2:
            check = seq_pairs(additive)
            if check > score:
                score = check
    info[0] += score

    
    info[1] = cur_val + new_card.value

    return info

