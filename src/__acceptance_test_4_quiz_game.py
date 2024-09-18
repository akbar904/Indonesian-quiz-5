
import unittest
from unittest.mock import patch
from quiz_game import QuizGame
from player import Player
from quiz import Quiz

class TestScenario5(unittest.TestCase):
    @patch('builtins.input', side_effect=['Science', 'exit'])
    def test_exit_before_answering(self, mock_input):
        # Create a dummy player and quiz for testing
        player = Player('TestPlayer', 0)
        question1 = Question('What is the capital of Indonesia?', 'Jakarta', 'Bali', 'Java', 'Sumatra', 'Jakarta')
        question2 = Question('Who is the first president of Indonesia?', 'Soekarno', 'Suharto', 'Joko Widodo', 'Megawati', 'Soekarno')
        quiz = Quiz([question1, question2], player)
        quiz_game = QuizGame(player, quiz)

        # Start the game and immediately exit
        quiz_game.startQuiz()
        
        # Check if the player's score is still 0 after exiting
        self.assertEqual(player.score, 0)

if __name__ == '__main__':
    unittest.main()
