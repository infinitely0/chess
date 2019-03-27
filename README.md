# Chess game and Python chess engine
Play chess against the computer.

The chess engine is written in Python and uses the minimax algorithm with
alpha-beta pruning to generate moves.

The default search depth is 4 and there's also a time limit of 60 seconds per
move for the computer. You can change these settings in the game setup in
`server.py`.

(I built this to learn Python and some AI concepts -- the chess engine is easy
to beat unless you're a novice.)

Start the server with (requires Flask)

    FLASK_APP=server.py python -m flask run

and play at http://127.0.0.1:5000/ in your browser.


