import time

from pieces.pawn import Pawn
# This file contains the main chess board


# Main chess class
class Chess:
    def __init__(self):
        self.first_move = True
        self.board = [
            ["bRo", "bKn", "bBi", "bQu", "bKi", "bBi", "bkn", "bRo", ],
            ["bPa", "bPa", "bPa", "bPa", "bPa", "bPa", "bPa", "bPa", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            ["wPa", "wPa", "wPa", "wPa", "wPa", "wPa", "wPa", "wPa", ],
            ["wRo", "wKn", "wBi", "wQu", "wKi", "wBi", "bKn", "bRo", ],
        ]

    def show_board(self):
        time.sleep(1)
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for index, line in enumerate(self.board):
            print("\n" + letters[7 - index] + ":" + str(line))
        print("  " + str([" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "]) + "\n")
        time.sleep(1)

    def play(self):
        self.show_board()
        player_choice = input("What piece would you like to move?: ")
        chosen_place = [char for char in player_choice.lower()]
        chosen_letter = chosen_place[0]
        chosen_place[0] = 7 - (ord(chosen_place[0]) - 97)
        chosen_place[1] = int(chosen_place[1]) - 1
        chosen_piece = self.board[int(chosen_place[0])][int(chosen_place[1])]
        if chosen_piece != " - ":
            if chosen_piece == "wPa":
                pawn = Pawn(chosen_letter, chosen_place[0], chosen_place[1] + 1)
                new_y = pawn.highlighted()
                if self.board[new_y][chosen_place[1]] == " - ":
                    self.board[chosen_place[0]][chosen_place[1]] = " - "
                    self.board[new_y][chosen_place[1]] = "wPa"
                else:
                    print("A piece is already here")
        else:
            print("No piece has been selected")
            self.play()
        self.play()

    def check_board(self):

