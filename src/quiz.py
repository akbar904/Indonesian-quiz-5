
class Quiz:
    def __init__(self):
        self.questions = []
        self.currentQuestionIndex = -1

    def startQuiz(self, player):
        self.player = player
        self.currentQuestionIndex = 0

    def getNextQuestion(self):
        if self.currentQuestionIndex < len(self.questions):
            return self.questions[self.currentQuestionIndex]
        else:
            return None

    def checkAnswer(self, answer):
        current_question = self.questions[self.currentQuestionIndex]
        if current_question.correctAnswer == answer:
            return True
        else:
            return False

    def updateScore(self, player):
        if not isinstance(player.score, int):
            raise TypeError('Score must be a number')
        if self.checkAnswer:
            player.score += 1
