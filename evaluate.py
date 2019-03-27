import chess
from math import inf

def evaluate(game):
  game.count += 1

  if game.board.is_checkmate():
    if game.board.turn == chess.BLACK:
      return inf
    else:
      return -inf

  return (
      + material_score(game.board)
      + king_safety(game.board)
      + pawn_promotion(game.board)
      + knight_position(game)
      + castling(game))

def material_score(board):
  white_material = (
      + len(board.pieces(chess.PAWN, chess.WHITE)) * 1
      + len(board.pieces(chess.KNIGHT, chess.WHITE)) * 3
      + len(board.pieces(chess.BISHOP, chess.WHITE)) * 3
      + len(board.pieces(chess.ROOK, chess.WHITE)) * 5
      + len(board.pieces(chess.QUEEN, chess.WHITE)) * 9)

  black_material = (
      + len(board.pieces(chess.PAWN, chess.BLACK)) * 1
      + len(board.pieces(chess.KNIGHT, chess.BLACK)) * 3
      + len(board.pieces(chess.BISHOP, chess.BLACK)) * 3
      + len(board.pieces(chess.ROOK, chess.BLACK)) * 5
      + len(board.pieces(chess.QUEEN, chess.BLACK)) * 9)

  return white_material - black_material

def king_safety(board):

  return 0

def pawn_promotion(board):

  return 0

def knight_position(game):

  return 0

def castling(game):
  if game.is_endgame():
    return 0

  score = 0
  if game.white_castled:
    score += 2
  elif not game.board.has_castling_rights(chess.WHITE):
    score -= 2
  elif not game.board.has_kingside_castling_rights(chess.WHITE):
    score -= 0.5
  elif not game.board.has_queenside_castling_rights(chess.WHITE):
    score -= 0.5

  if game.black_castled:
    score -= 2
  elif not game.board.has_castling_rights(chess.BLACK):
    score += 2
  elif not game.board.has_kingside_castling_rights(chess.BLACK):
    score += 0.5
  elif not game.board.has_queenside_castling_rights(chess.BLACK):
    score += 0.5

  return score

