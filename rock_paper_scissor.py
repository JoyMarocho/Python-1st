# Rock Paper scissors GAME BY USING A STANDARD INPUT FOR THE COMPUTER

# computer_choice = 'scissors'

# user_choice = input('Do you want - rock, paper, or scissors?\n')

# if  computer_choice == user_choice:
#     print('You TIE')
# elif  user_choice == 'rock' and computer_choice == 'scissors':
#     print('You WIN')
# elif  user_choice == 'paper' and computer_choice == 'rock':
#     print('You WIN')
# elif  user_choice == 'scissors' and computer_choice == 'paper':
#     print('You WIN')
# else:
#     print('You lose :( Computer wins :D')



# Rock Paper scissors GAME BY USING A RANDOM MODULE FOR THE COMPUTER
import random

computer_choice = random.choice (['rock', 'paper', 'scissors'])

user_choice = input('Do you want - rock, paper, or scissors?\n')

if  computer_choice == user_choice:
    print('TIE')
elif  user_choice == 'rock' and computer_choice == 'scissors':
    print('You WIN, the Computer had ' + computer_choice)
elif  user_choice == 'paper' and computer_choice == 'rock':
    print('You WIN, the Computer had ' + computer_choice)
elif  user_choice == 'scissors' and computer_choice == 'paper':
    print('You WIN, the Computer had ' + computer_choice)
else:
    print('You lose :( Computer wins :D')
