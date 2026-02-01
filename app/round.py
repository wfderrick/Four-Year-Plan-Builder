import tools
import structs
from opponentbrain import discard
import copy
def round(
    player1_hand, player2_hand, cut_card, round_num, player1_score, player2_score, crib
):
    cut_card = tools.deal(player1_hand, player2_hand, cut_card)
    player1_hand = tools.transform_cards(player1_hand, structs.Hand(0, 0, 0, 0, 0, 0))
    player2_hand = tools.transform_cards(player2_hand, structs.Hand(0, 0, 0, 0, 0, 0))
    cut_card = tools.get_card(cut_card, structs.Card(0, 0, 0))
    last_player = 0
    print(
        "X```````````````````````````````````````````````````````````````````````````\n"
        f"X   Your Score: {player1_score}             Opponent's Score: {player2_score}             Goal: 120 \n"
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

    while len(player1_hand.hand) > 0 or len(player2_hand.hand) > 0:
        if last_player == 1 and len(player2_hand.hand) > 0:
            play = 