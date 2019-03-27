import chess
import time
import chess.polyglot

from search import minimax

class Game():

  def __init__(self):
    self.depth = 4
    self.timeout = 60
    self.start_time = time.time()

    self.board = chess.Board()
    self.white_castled = False
    self.black_castled = False

    self.count = 0

  def move(self, move):
    if self.board.turn == chess.WHITE:

      if (not self.is_endgame()
          and not self.white_castled
          and self.board.is_castling(move)):

        self.white_castled = True

    else:

      if (not self.is_endgame()
          and not self.black_castled
          and self.board.is_castling(move)):

        self.black_castled = True

    self.board.push(move)

  def undo(self):
    last_move = self.board.pop()

    if self.board.turn == chess.WHITE:

      if not self.is_endgame() and self.board.is_castling(last_move):

        self.white_castled = False

    else:

      if not self.is_endgame() and self.board.is_castling(last_move):

        self.black_castled = False

  def go(self):
    if not self.board.is_game_over():

      if self.is_opening():
        try:
          move = self.look_up()
          time.sleep(2)
          return move
        except IndexError:
          pass

      self.start_time = time.time()
      best_move = minimax(self,
          self.depth,
          self.board.turn,
          self.timeout)

      return best_move

  def look_up(self):
    with chess.polyglot.open_reader("data/Formula12.bin") as reader:
      return reader.find(self.board).move()

  def is_opening(self):
    return self.board.fullmove_number <= 10

  def is_middlegame(self):
    return (self.board.fullmove_number > 10
        and self.board.fullmove_number >= 20)

  def is_endgame(self):
    return self.board.fullmove_number > 20

