
import unittest
from unittest.mock import patch, MagicMock
from quiz_game import QuizGame
from player import Player
from quiz import Quiz

class TestQuizGame(unittest.TestCase):

	def setUp(self):
		self.quiz = Quiz()
		self.player = Player()
		self.game = QuizGame(self.player, self.quiz)

	@patch('quiz_game.QuizGame.displayQuestion', return_value=None)
	@patch('quiz_game.QuizGame.updateScore', return_value=None)
	@patch('quiz_game.Player.answer', return_value='exit')
	@patch('quiz_game.Quiz.getNextQuestion', return_value=None)
	def test_exit_before_selecting_category(self, mock_get_next_question, mock_player_answer, mock_update_score, mock_display_question):
		self.game.startQuiz()
		mock_get_next_question.assert_called_once()
		mock_display_question.assert_called_once()
		mock_player_answer.assert_called_once()
		mock_update_score.assert_not_called()

if __name__ == '__main__':
	unittest.main()
