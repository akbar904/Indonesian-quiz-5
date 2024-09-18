
import unittest
from question import Question

class TestQuestion(unittest.TestCase):

	def setUp(self):
		self.question = Question()

	def test_question_initialization(self):
		self.assertEqual(self.question.question, '')
		self.assertEqual(self.question.optionA, '')
		self.assertEqual(self.question.optionB, '')
		self.assertEqual(self.question.optionC, '')
		self.assertEqual(self.question.optionD, '')
		self.assertEqual(self.question.correctAnswer, '')

	def test_question_assignment(self):
		self.question.question = 'What is the capital of Indonesia?'
		self.question.optionA = 'Jakarta'
		self.question.optionB = 'Bandung'
		self.question.optionC = 'Surabaya'
		self.question.optionD = 'Bali'
		self.question.correctAnswer = 'Jakarta'
		self.assertEqual(self.question.question, 'What is the capital of Indonesia?')
		self.assertEqual(self.question.optionA, 'Jakarta')
		self.assertEqual(self.question.optionB, 'Bandung')
		self.assertEqual(self.question.optionC, 'Surabaya')
		self.assertEqual(self.question.optionD, 'Bali')
		self.assertEqual(self.question.correctAnswer, 'Jakarta')

	def test_question_correct_answer(self):
		self.question.correctAnswer = 'Jakarta'
		self.assertEqual(self.question.correctAnswer, 'Jakarta')

if __name__ == '__main__':
	unittest.main()
