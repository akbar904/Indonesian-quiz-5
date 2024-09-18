
import unittest
from unittest.mock import patch
from quiz_game import QuizGame
from player import Player
from quiz import Quiz
from question import Question

class TestScenario2(unittest.TestCase):

	def setUp(self):
		questions = [
			Question('Question 1', 'Option A', 'Option B', 'Option C', 'Option D', 'Option E'),
			Question('Question 2', 'Option A', 'Option B', 'Option C', 'Option D', 'Option E'),
		]
		self.quiz = Quiz(questions)
		self.player = Player('Test Player')
		self.game = QuizGame(self.player, self.quiz)

	@patch('builtins.input', side_effect=['Option A', 'Option B'])
	@patch('builtins.print')
	def test_startQuiz(self, mock_print, mock_input):
		self.game.startQuiz()
		self.assertEqual(self.player.score, 0)
		self.game.endQuiz()
		mock_print.assert_called_with('End of the quiz. Your final score is: 0')

if __name__ == "__main__":
	unittest.main()
