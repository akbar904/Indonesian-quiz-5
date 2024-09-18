
import unittest
from unittest.mock import patch
from io import StringIO

from quiz_game import QuizGame
from quiz import Quiz
from player import Player
from question import Question

class TestQuizGame(unittest.TestCase):

	def setUp(self):
		self.player = Player('Test Player')
		self.questions = [
			Question('Who is the first president of Indonesia?', 'Sukarno', 'Suharto', 'Joko Widodo', 'Megawati', 'A'),
			Question('When did Indonesia proclaim its independence?', '1940', '1945', '1950', '1955', 'B')
		]
		self.quiz = Quiz(self.questions)
		self.game = QuizGame(self.player, self.quiz)

	@patch('sys.stdout', new_callable=StringIO)
	@patch('builtins.input', side_effect=['A', 'B'])
	def test_quiz_game(self, mock_input, mock_stdout):
		self.game.startQuiz()
		expected_output = (
			'Question: Who is the first president of Indonesia?\n'
			'A. Sukarno\n'
			'B. Suharto\n'
			'C. Joko Widodo\n'
			'D. Megawati\n'
			'Your current score is: 1\n'
			'Question: When did Indonesia proclaim its independence?\n'
			'A. 1940\n'
			'B. 1945\n'
			'C. 1950\n'
			'D. 1955\n'
			'Your current score is: 2\n'
		)
		self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
	unittest.main()
