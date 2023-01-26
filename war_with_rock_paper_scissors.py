import random
import time


class COLORS:
    BLUE = '\033[94m'
    RED = '\033[91m'
    FACTORY = '\033[0m'


def invalid():
    global player_move
    if player_move != "r" and player_move != "p" and player_move != "s":
        invalid_move = True
        print(f"{COLORS.FACTORY}Try again and be serious! It is a game of life or death!")
        while invalid_move:
            player_move = input(f'{COLORS.FACTORY}That was a invalid move!!!\n{COLORS.RED}Choose >? ')
            if player_move == "r" or player_move == "p" or player_move == "s":
                invalid_move = False


player = input(f"{COLORS.FACTORY}Enter your name, please: ")
print(f"{COLORS.FACTORY}Excellent name! After 5 seconds the computer will show up.")

time.sleep(5)

print(f"{COLORS.BLUE}Hi player, with excellent name.\n\
I'm the computer. Let's play!!!\n\
This is gonna be war with three battles.\n\
Choose [r], [p] or [s].\n\
[r] is for rock, [p] is for paper, [s] is for scissors.")

computer_win = 0
player_win = 0
count_battles = 1

while count_battles <= 3:
    print(f"\n{COLORS.FACTORY}<<< BATTLE № {count_battles} >>>\n")

    player_move = input(f"{COLORS.RED}Choose >? ")

    invalid()

    list_characters = ["r", "p", "s"]

    computer_move = random.choice(list_characters)

    print(f"{COLORS.BLUE}My move is: {computer_move}\n")

    if player_move == computer_move:
        result = "Draw!"
        while result == "Draw!":
            print(f"{COLORS.FACTORY}{result}")
            print(f"{COLORS.BLUE}Let's try again!\n")
            player_move = input(f"{COLORS.RED}Choose >? ")

            invalid()

            computer_move = random.choice(list_characters)
            print(f"{COLORS.BLUE}I chose: {computer_move}\n")
            if player_move == computer_move:
                result = "Draw!"
            else:
                break

    if (player_move == "r" and computer_move == "p") or \
            (player_move == "p" and computer_move == "s") or \
            (player_move == "s" and computer_move == "r"):
        computer_win += 1
        print(f"{COLORS.BLUE}You lose the battle! HaHa")

    elif (player_move == "r" and computer_move == "s") or \
            (player_move == "p" and computer_move == "r") or \
            (player_move == "s" and computer_move == "p"):
        player_win += 1
        print(f"{COLORS.BLUE}Damn it, you win the battle!")

    count_battles += 1

if player_win > computer_win:
    print(f"\n{COLORS.FACTORY}{player.upper()} WIN THE WAR.\n\
CONGRATULATION, {player.upper()}")

else:
    print(f"\n{COLORS.FACTORY}THE COMPUTER WIN THE WAR.\n\
THE FUTURE IS CLOSE!")
