import chess
from math import inf
from time import time

from evaluate import evaluate

def minimax(game, depth, player, timeout):
  moves = game.board.legal_moves
  best_move = None

  if player == chess.WHITE:
    best_score = -inf
    for move in moves:
      game.move(move)
      score = minimiser(game, depth, inf, -inf, timeout)
      if score > best_score:
        best_score = score
        best_move = move
      game.undo()
  else:
    best_score = inf
    for move in moves:
      game.move(move)
      score = maximiser(game, depth, -inf, inf, timeout)
      if score < best_score:
        best_score = score
        best_move = move
      game.undo()

  return best_move

def minimiser(game, depth, alpha, beta, timeout):
  if depth == 0 or game.board.is_game_over() or is_timeout(game, timeout):
    return evaluate(game)

  score = inf
  for move in game.board.legal_moves:
    game.move(move)
    score = min(maximiser(game, depth - 1, alpha, beta, timeout), score)
    game.undo()

    if score <= alpha:
      return score
    beta = min(beta, score)

  return score

def maximiser(game, depth, alpha, beta, timeout):
  if depth == 0 or game.board.is_game_over() or is_timeout(game, timeout):
    return evaluate(game)

  score = -inf
  for move in game.board.legal_moves:
    game.move(move)
    score = max(minimiser(game, depth - 1, alpha, beta, timeout), score)
    game.undo()

    if score >= beta:
      return score
    alpha = max(alpha, score)
  
  return score

def is_timeout(game, timeout):
  return time() - game.start_time > timeout

