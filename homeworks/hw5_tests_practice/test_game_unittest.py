import unittest
from unittest.mock import patch
from game import TicTacToe


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()
        self.game.board[4] = "X"

    def test_available_moves(self):
        self.assertTrue(4 not in self.game.available_moves())

    def test_make_move(self):
        self.assertFalse(self.game.make_move(4, "X"))
        self.assertTrue(self.game.make_move(5, "X"))
        self.assertTrue(self.game.board[5] != " ")

    def test_winner(self):
        self.game.board = ["X", "X", "X", " ", "X", " ", "O", " ", "O"]
        self.assertTrue(self.game.winner(2, "X"))
        self.assertFalse(self.game.winner(4, "X"))

        self.game.board = ["O", "O", "X", "X", " ", "X", " ", " ", "X"]
        self.assertTrue(self.game.winner(8, "X"))
        self.assertFalse(self.game.winner(3, "X"))

        self.game.board = ["X", " ", "O", "X", "O", " ", "O", "X", " "]
        self.assertTrue(self.game.winner(6, "O"))
        self.assertFalse(self.game.winner(7, "X"))

        self.game.board = ["X", " ", "O", "O", "X", " ", "O", "X", "X"]
        self.assertTrue(self.game.winner(8, "X"))
        self.assertFalse(self.game.winner(7, "X"))

    if __name__ == '__main__':
        unittest.main()
