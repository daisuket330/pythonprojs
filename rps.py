import random
moves = ['rock', 'paper', 'scissors']
computer_choice = moves[random.randint(0,2)]
user_choice = input('choose rock, paper, scissors\n')
print("computer picked " + computer_choice)

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Win')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('Win')
else:
    print('You lose :(Computer Wins:D')