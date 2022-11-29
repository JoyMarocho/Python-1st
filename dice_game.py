# import random

# def roll_dice():
#     dice_total = random.randint(1,6) + random.randint(1,6)
#     return dice_total

# player1 = input("Enter players 1's name: ")
# player2 = input("Enter players 2's name: ")

# roll1 = roll_dice()
# roll2 = roll_dice()

# print(player1, 'rolled', roll1)
# print(player2, 'rolled', roll2)

# if roll1 > roll2:
#     print(player1, 'Wins!')
# elif roll2 > roll1:
#     print(player2, 'Wins!')
# else:
#     print('You Tie!')


####### ORGANIZING our main code ###############

import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("Enter players 1's name: ")
    player2 = input("Enter players 2's name: ")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, 'rolled', roll1)
    print(player2, 'rolled', roll2)

    if roll1 > roll2:
        print(player1, 'Wins!')
    elif roll2 > roll1:
        print(player2, 'Wins!')
    else:
        print('You Tie!')

main()