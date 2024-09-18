
import unittest
from unittest.mock import patch
from player import Player
from quiz import Quiz
from question import Question
from quiz_game import QuizGame

class TestQuizGame(unittest.TestCase):
    
    def setUp(self):
        question1 = Question('When did Indonesia gain independence?', '1945', '1946', '1947', '1948', '1945')
        question2 = Question('Who was the first President of Indonesia?', 'Soekarno', 'Suharto', 'BJ Habibie', 'Joko Widodo', 'Soekarno')
        self.questions = [question1, question2]
        self.quiz = Quiz(self.questions)
        self.player = Player('TestPlayer')
        self.game = QuizGame(self.player, self.quiz)

    @patch('builtins.input', side_effect=['1945', 'Soekarno'])
    def test_play_quiz(self, mock_input):
        self.game.startQuiz()
        self.assertEqual(self.player.score, 2)
        with self.assertRaises(StopIteration):
            self.game.quiz.getNextQuestion()

    @patch('builtins.input', side_effect=['1948', 'Suharto'])
    def test_play_quiz_wrong_answers(self, mock_input):
        self.game.startQuiz()
        self.assertEqual(self.player.score, 0)
        with self.assertRaises(StopIteration):
            self.game.quiz.getNextQuestion()

if __name__ == "__main__":
    unittest.main()
