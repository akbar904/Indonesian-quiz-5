
from question import Question
from player import Player
from quiz import Quiz

class QuizGame:
	def __init__(self, player, quiz):
		self.player = player
		self.quiz = quiz

	def startQuiz(self):
		while self.quiz.currentQuestionIndex < len(self.quiz.questions):
			question = self.quiz.getNextQuestion()
			self.displayQuestion(question)
			playerAnswer = self.player.answer()
			isCorrect = self.quiz.checkAnswer(question, playerAnswer)
			if isCorrect:
				self.player.score += 1
			self.updateScore(self.player.score)

	def displayQuestion(self, question):
		print(f"Question: {question.question}")
		print(f"A. {question.optionA}")
		print(f"B. {question.optionB}")
		print(f"C. {question.optionC}")
		print(f"D. {question.optionD}")

	def updateScore(self, score):
		print(f"Your current score is: {score}")

	def endQuiz(self):
		print(f"End of the quiz. Your final score is: {self.player.score}")
