import tools
from structs import Card, Hand
from opponentbrain import discard, pegging
import copy
from pegging import peg_score
from calculate import score

def round(
    player1_hand, player2_hand, cut_card, round_num, player1_score, player2_score, crib
):
    cut_card = tools.deal(player1_hand, player2_hand, cut_card)
    player1_hand = tools.transform_cards(player1_hand, Hand(0, 0, 0, 0, 0, 0))
    player2_hand = tools.transform_cards(player2_hand, Hand(0, 0, 0, 0, 0, 0))
    cut_card = tools.get_card(cut_card, Card(0, 0, 0))
    last_player = 0
    print(
        "X```````````````````````````````````````````````````````````````````````````\n"
        f"X   Your Score: {player1_score[0]}             Opponent's Score: {player2_score[0]}             Goal: 120 \n"
        "X___________________________________________________________________________\n"
    )
    print(f"Begin Round {round_num}:")

    print(
        "This is your hand.\n"
        "       |||        \n"
        "       |||        \n"
        "      \\\\ //       \n"
        "        V         "
    )
    print(f"{player1_hand}\n")
    if round_num % 2 == 0:
        print("Opponents Crib!")
        last_player = 2 
    else:
        print("Your Crib!")
        last_player = 1
    val1 = input("Enter the first number to be discarded. ")
    while not (isinstance(val1, str) and val1.isdigit() and int(val1) > 0 and int(val1) < 7):
        val1 = input("Enter a value between 1 and 6. ")

    val2 = input("Enter the second number to be discarded. ")
    while not (isinstance(val2, str) and val2.isdigit()):
        val2 = input("Enter a value between 1 and 6. ")
    while not (int(val2) > 0 and int(val2) < 7):
        if val2 == val1:
            val2 = input("Enter a different value than you did the first time. ")
        else:
            val2 = input("Enter a value between 1 and 6. ")

    player1_hand.remove(int(val1), int(val2), crib)
    comp_discard = discard(player2_hand.hand, [])
    player2_hand.remove(comp_discard[0], comp_discard[1], crib)
    print(
        "This is your hand.\n"
        "       |||        \n"
        "       |||        \n"
        "      \\\\ //       \n"
        "        V         "
    )
    print(f"{player1_hand}\n")
    empt = input("Press enter to see the cut card.")
    print(cut_card)

    empt = input("Press enter to begin the pegging round!")
    cur_val = 0
    p1_pegging = copy.deepcopy(player1_hand.hand)
    p2_pegging = copy.deepcopy(player2_hand.hand)
    prev_cards = []
    go = False
    can_play = False

    while len(p1_pegging) > 0 or len(p2_pegging) > 0:
        if last_player == 1:
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
                        player2_score[0] += 1
                        go == False
                        cur_val = 0
                        prev_cards = []
                        last_player = 2
                    else:
                        (p2_score, val) = peg_score(prev_cards, card, cur_val)
                        player2_score[0] += p2_score
                        cur_val = val
                        p2_pegging.remove(card)
                else:
                    last_player = 2
                    cur_val = 0
                    go = False
            else:
                if len(p2_pegging) > 0:
                    if len(prev_cards) > 0:
                        card = pegging(cur_val, prev_cards[len(prev_cards) - 1], p2_pegging)
                    else:
                        card = pegging(cur_val, [], p2_pegging)
                    if card == -1:
                        go = True
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
            print(f"The current value is: {cur_val}")
            
        else:
            if cur_val == 31:
                input("31 was reached so the pegging will reset to 0.")
                cur_val = 0
                go = False
            for i in p1_pegging:
                if i.value + cur_val <= 31:
                    can_play = True
                    break
            if can_play:
                if len(p1_pegging) > 0:
                    print(
                        "This is your hand.\n"
                        "       |||        \n"
                        "       |||        \n"
                        "      \\\\ //       \n"
                        "        V         ")
                    track = 1
                    for i in p1_pegging:
                        print(f"{track}: {i}")
                        track += 1
                    card_num = input(f"Enter the number next to the card you would like to peg.")
                    check = False
                    while ((not card_num.isdigit()) or int(card_num) > track or int(card_num) < 1) or check == False:
                        if (not card_num.isdigit()) or int(card_num) > track or int(card_num) < 1:
                            card_num = input(f"Enter a number between 1 and {track - 1}")
                        card = p1_pegging[int(card_num) - 1]
                        if card.value + cur_val <= 31:
                            check = True
                        else:
                            card_num = input(f"Enter a different number for a card that is actually playable:")

                    if go == True:
                            (p1_score, val) = peg_score(prev_cards, card, cur_val)
                            player1_score[0] += p1_score
                            cur_val = val
                            prev_cards.append(card)
                            p1_pegging.remove(card)
                    else:
                            (p1_score, val) = peg_score(prev_cards, card, cur_val)
                            player1_score[0] += p1_score
                            cur_val = val                        
                            prev_cards.append(card)
                            p1_pegging.remove(card) 
                            last_player = 1
                else:
                    if go == True:
                        player1_score[0] += 1
                    last_player = 1
                can_play = False

                input(f"You played a {card} the current value is {cur_val}")
                if cur_val == 31:
                    cur_val = 0
            else:
                if go != True:
                    input("You are unable to play any cards so it's a go for your opponent.")
                    go = True
                else:
                    input("You can't play anymore cards so pegging will restart.")
                    cur_val = 0
                    go = False
                last_player = 1
    
    input(f"Pegging is over the main scoring can begin.")
    player1_val = score(player1_hand.hand, cut_card)
    player2_val = score(player2_hand.hand, cut_card)
    print(f"Your hand is worth {player1_val} points.")
    input(f"The computer's hand is worth {player2_val} points.")
    player1_score[0] += player1_val
    player2_score[0] += player2_val
    print(f"Your current total score is {player1_score[0]}.")
    input(f"The computer's current score is {player2_score[0]}.") 