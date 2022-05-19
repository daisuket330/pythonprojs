import random

roll = random.randint(1,6)

guess =int(input('Guess the dice roll:\n'))

# print(" computer rolled a " + str(roll))

if guess == roll:
    print("Correct! they rolled a " + str(roll))
else:
    print("Wrong! they rolled a " + str(roll))