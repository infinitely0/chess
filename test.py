import unittest

from game import Game
from evaluate import evaluate

class Test(unittest.TestCase):

  def test_castling(self):
    self.assertEqual('foo'.upper(), 'FOO')
    self.assertTrue('FOO'.isupper())
    self.assertFalse('Foo'.isupper())

  def test_white_knight_positions(self):
    game = Game()

    moves = [ "b1a3", "g1h3" ]
    attrs = [ "white_knight_on_edge1", "white_knight_on_edge2" ] 

    for i in range(2):
      move = game.board.parse_uci(moves[i])
      attr = attrs[i]

      game.move(move)
      score = evaluate(game)
      self.assertTrue(getattr(game, attr))
      self.assertEqual(score, -50)

      game.undo()
      score = evaluate(game)
      self.assertFalse(getattr(game, attr))
      self.assertEqual(score, 0)

  def test_black_knight_positions(self):
    game = Game()

    move = game.board.parse_uci("d2d3")
    game.move(move)

    moves = [ "b8a6", "g8h6" ]
    attrs = [ "black_knight_on_edge1", "black_knight_on_edge2" ]

    for i in range(2):
      move = game.board.parse_uci(moves[i])
      attr = attrs[i]

      game.move(move)
      score = evaluate(game)
      self.assertTrue(getattr(game, attr))
      self.assertEqual(score, 50)

      game.undo()
      score = evaluate(game)
      self.assertFalse(getattr(game, attr))
      self.assertEqual(score, 0)


if __name__ == '__main__':
  unittest.main()

