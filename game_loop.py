from board import Board
from pieces.pawn import Pawn


def update_board():
    game_board = Board()
    while(True):
        letter, y_pos, x_pos = game_board.show_board()
        if game_board.board[y_pos][x_pos] == "wPa":
            pawn = Pawn(letter, y_pos, x_pos)
            new_y, new_x = pawn.highlighted()
            game_board.update_board("wPa", y_pos, x_pos, new_y, new_x)


update_board()
