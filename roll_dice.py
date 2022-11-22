# USING THE RANDOM MODULE

import random
# i need to import the module so that i can use it 

roll = random.randint(1,6) 
# This function will return a random number between 1 and 6

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))