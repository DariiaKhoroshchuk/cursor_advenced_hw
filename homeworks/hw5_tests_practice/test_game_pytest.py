from game import TicTacToe
import pytest

game = TicTacToe()
game.board[4] = "X"


def test_available_moves():
    assert 4 not in game.available_moves()
    assert 2 in game.available_moves()
    assert 0 in game.available_moves()
    with pytest.raises(AssertionError):
        assert -5 in game.available_moves()
        assert 12 in game.available_moves()


def test_make_move():
    assert game.make_move(4, "X") is False
    assert game.make_move(5, "X") is True
    assert game.board[5] != " "
    assert game.board[3] == " "
    with pytest.raises(AssertionError):
        assert game.make_move(-5, "X")
        assert game.make_move(12, "X")




