import random
import game_method
moves = ['rock', 'paper', 'scissors']
computer_choice = moves[random.randint(0,2)]
user_choice = input('choose rock, paper, scissors\n')
print("computer picked " + computer_choice)


game_method.game(user_choice,computer_choice)


# 

