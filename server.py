from flask import Flask
from flask import render_template
from flask import request
from time import process_time

from game import Game
import evaluate

app = Flask(__name__)

game = Game()

@app.route("/")
def main():
  global game
  game = Game()
  game.depth = 4
  game.timeout = 60

  return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
  return send_from_directory('static', path)

@app.route('/move/', methods=['POST'])
def move():
  data = request.json

  move = game.board.parse_san(data['san'])
  game.move(move)

  t0 = process_time()
  best_move = game.go()
  t1 = process_time() - t0

  san = game.board.san(best_move)
  game.move(best_move)

  print("Time:\t\t" + str(round(t1, 3)))
  print("Positions:\t" + str(game.count))
  print("Positions/s:\t" + str(round(game.count/t1)))
  print("Score:\t\t" + str(evaluate.evaluate(game)))
  print("Board:\n" + str(game.board))

  game.count = 0

  return san

