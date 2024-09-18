
import unittest
from player import Player

class TestPlayer(unittest.TestCase):

	def setUp(self):
		self.player = Player("Test Player")

	def test_player_initialization(self):
		self.assertEqual(self.player.name, "Test Player", "The name of the player is incorrect")
		self.assertEqual(self.player.score, 0, "The initial score is not zero")

	def test_score_update(self):
		self.player.update_score(10)
		self.assertEqual(self.player.score, 10, "The score update is incorrect")

	def test_score_reset(self):
		self.player.reset_score()
		self.assertEqual(self.player.score, 0, "The score reset is incorrect")

	def test_score_negative_update(self):
		with self.assertRaises(ValueError):
			self.player.update_score(-10)

	def test_score_non_integer_update(self):
		with self.assertRaises(TypeError):
			self.player.update_score("10")

if __name__ == "__main__":
	unittest.main()
