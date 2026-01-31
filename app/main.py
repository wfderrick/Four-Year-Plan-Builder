import tools
import structs
from round import round


def main():
    print("Welcome to my homemade Cribbage game!")
    print("I hope you enjoy!")
    play = input("Press enter to start: ")
    round_num = 1
    player1_hand = []
    player2_hand = []
    cut_card = 0
    player1_score = 0
    player2_score = 0
    crib = []
    # print("|----------------------------------------------------|\n| Your Score: 0                   Opponent's Score: 0|\n|                                                    |\n|                                                    |\n|                                                    |\n|----------------------------------------------------|")

    while player1_score < 121 and player2_score < 121:
        round(
        player1_hand,
        player2_hand,
        cut_card,
        round_num,
        player1_score,
        player2_score,
        crib,
        )
        round_num += 1


if __name__ == "__main__":
    main()
