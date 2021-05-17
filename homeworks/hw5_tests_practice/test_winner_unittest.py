import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_raw(self):
        self.game.board = ["X", "X", "X", " ", "X", " ", "O", " ", "O"]
        self.assertTrue(self.game.winner(2, "X"))
        self.assertFalse(self.game.winner(4, "X"))

    def test_column(self):
        self.game.board = ["O", "O", "X", "X", " ", "X", " ", " ", "X"]
        self.assertTrue(self.game.winner(8, "X"))
        self.assertFalse(self.game.winner(3, "X"))

    def test_diagonal1(self):
        self.game.board = ["X", " ", "O", "X", "O", " ", "O", "X", " "]
        self.assertTrue(self.game.winner(6, "O"))
        self.assertFalse(self.game.winner(7, "X"))

    def test_diagonal2(self):
        self.game.board = ["X", " ", "O", "O", "X", " ", "O", "X", "X"]
        self.assertTrue(self.game.winner(8, "X"))
        self.assertFalse(self.game.winner(7, "X"))

    if __name__ == '__main__':
        unittest.main()
