from board import Board
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.bishop import Bishop


def update_board():
    game_board = Board()
    while(True):
        letter, y_pos, x_pos = game_board.show_board()
        if game_board.board[y_pos][x_pos] == "wPa":
            pawn = Pawn(letter, y_pos, x_pos)
            pawn.highlighted()
            check_for_enemies = game_board.check_for_piece([pawn.new_y, pawn.new_x])
            new_y, new_x = pawn.move_pawn(check_for_enemies)
            game_board.update_board("wPa", y_pos, x_pos, new_y, new_x)
        elif game_board.board[y_pos][x_pos] == "wRo":
            rook = Rook(letter, y_pos, x_pos)
            rook.highlighted()
            new_y, new_x, direction = rook.move_rook()
            in_the_way = False
            if direction == "x_change":
                step = -1 if x_pos - new_x < 0 else 1

                for i in range(x_pos, x_pos - new_x, step):
                    if not i == 0:
                        if game_board.board[y_pos][i].__contains__("w"):
                            in_the_way = True
                        elif game_board.board[y_pos][i].__contains__("b"):
                            game_board.update_board("wRo", y_pos, x_pos, y_pos, i)
                            return
            elif direction == "y_change":
                step = -1 if y_pos - new_y < 0 else 1
                for i in range(new_y, y_pos - new_y, step):
                    if not i == 0:
                        if game_board.board[7 - i][x_pos].__contains__("w"):
                            in_the_way = True
                        elif game_board.board[7 - i][x_pos].__contains__("b"):
                            game_board.update_board("wRo", y_pos, x_pos, 7 - i, x_pos)
                            return
            if not in_the_way:
                game_board.update_board("wRo", y_pos, x_pos, new_y, new_x)
            else:
                print("Allied piece in the way")
        elif game_board.board[y_pos][x_pos] == "wBi":
            bishop = Bishop(letter, y_pos, x_pos)
            bishop.highlighted()
            new_y, new_x, direction = bishop.move_bishop()
            game_board.update_board("wBi", y_pos, x_pos, new_y, new_x)


update_board()
