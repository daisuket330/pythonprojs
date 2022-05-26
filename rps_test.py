import unittest
from game_method import game



class GameTestClass(unittest.TestCase):
    def test_Game_loss(self):
        human_choice = "rock"
        computer_choice = "paper"

        result=game(computer_choice,human_choice)
        self.assertEqual(result,"Lose!")


    def test_Game_win(self):
         human_choice = "rock"
         computer_choice = "scissors" 

         result=game(computer_choice,human_choice)
         self.assertEqual(result,"Win!")


    def test_Game(self):
        human_choice = ''
        computer_choice = ''
        result = game(computer_choice,human_choice)
        self.assertEqual(result,"Tie!")

