
import unittest
from quiz import Quiz
from question import Question
from player import Player

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz()
        self.player = Player("Test Player")
        self.question1 = Question("What year did Indonesia gain independence?", "1945", "1946", "1947", "1948", "1945")
        self.question2 = Question("Who was the first president of Indonesia?", "Sukarno", "Suharto", "Joko Widodo", "Megawati Sukarnoputri", "Sukarno")

    def test_start_quiz(self):
        self.quiz.startQuiz(self.player)
        self.assertEqual(self.quiz.currentQuestionIndex, 0)

    def test_next_question(self):
        self.quiz.questions.append(self.question1)
        self.quiz.questions.append(self.question2)
        next_question = self.quiz.getNextQuestion()
        self.assertEqual(next_question, self.question1)

    def test_check_answer(self):
        self.quiz.questions.append(self.question1)
        is_correct = self.quiz.checkAnswer("1945")
        self.assertTrue(is_correct)

    def test_update_score(self):
        self.quiz.questions.append(self.question1)
        self.quiz.checkAnswer("1945")
        with self.assertRaises(TypeError) as context:
            self.player.score = "not a number"
            self.quiz.updateScore(self.player)
        self.assertTrue('Score must be a number' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
