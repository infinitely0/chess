var game = new Chess();

var board;

var boardEl = $('#board');

// do not pick up pieces if the game is over
// only pick up pieces for the side to move
var onDragStart = function(source, piece, position, orientation) {
  if (game.in_checkmate() === true
      || game.in_draw() === true
      || (game.turn() === 'w' && piece.search(/^b/) !== -1)
      || (game.turn() === 'b' && piece.search(/^w/) !== -1)) {

    return false;
  }
};

var onDrop = function(source, target) {
  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q'
    // NOTE: always promote to a queen for example simplicity
  });

  // illegal move
  if (move === null) return 'snapback';

  addHighlights(move.from, move.to);

  board.position(game.fen());

  sendMove(move);
};

// update the board position after the piece snap
// for castling, en passant, pawn promotion
var onSnapEnd = function() {
  board.position(game.fen());
};

var removeHighlights = function() {
  boardEl.find('.square-55d63').removeClass('highlight-white');
};

var addHighlights = function(from, to) {
  removeHighlights();
  boardEl.find('.square-' + from).addClass('highlight-white');
  boardEl.find('.square-' + to).addClass('highlight-white');
}

var pieceTheme = function(piece) {
  return '/static/img/pieces/' + piece + '.png';
}

var cfg = {
  draggable: true,
  position: 'start',
  onDragStart: onDragStart,
  onDrop: onDrop,
  onSnapEnd: onSnapEnd,
  pieceTheme: pieceTheme
};

board = ChessBoard('board', cfg);

function sendMove(move) {
  $.ajax({
    type: 'POST',
    url: "/move/",
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify(move)
  })
  .done(function(san) {
    game.move(san);

    // Move history has bug - undo and redo move
    move = game.undo()
    game.move(san);

    addHighlights(move.to, move.from);

    fen = game.fen()
    board.position(fen);
  });
}

