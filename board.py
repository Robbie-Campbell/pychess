import time
# This file contains the main chess board

# Main chess class


class Board:
    def __init__(self):
        self.board = [
            ["bRo", "bKn", "bBi", "bQu", "bKi", "bBi", "bkn", "bRo", ],
            [" - ", "bPa", "bPa", "bPa", "bPa", "bPa", "bPa", "bPa", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            [" - ", " - ", " - ", "wBi", " - ", " - ", " - ", " - ", ],
            [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", ],
            [" - ", "wPa", "wPa", "wPa", "wPa", "wPa", "wPa", "wPa", ],
            ["wRo", "wKn", "wBi", "wQu", "wKi", "wBi", "wKn", "wRo", ],

        ]

    def show_board(self):
        time.sleep(1)
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        for index, line in enumerate(self.board):
            print("\n" + letters[7 - index] + ":" + str(line))
        print("  " + str([" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 "]) + "\n")
        time.sleep(1)
        player_choice = input("Please select a piece to move: ")
        chosen_place = [char for char in player_choice.lower()]
        chosen_letter = chosen_place[0]
        chosen_place[0] = 7 - (ord(chosen_place[0]) - 97)
        chosen_place[1] = int(chosen_place[1]) - 1
        return chosen_letter, int(chosen_place[0]), int(chosen_place[1])

    def update_board(self, piece, start_y, start_x, new_y, new_x):
        self.board[start_y][start_x] = " - "
        self.board[new_y][new_x] = piece

    def check_for_piece(self, new_pos):
        if self.board[new_pos[0]][new_pos[1]].__contains__("b"):
            return "Enemy"
        elif self.board[new_pos[0]][new_pos[1]].__contains__("w"):
            return "Ally"
        elif self.board[new_pos[0]][new_pos[1]] == " - ":
            return False
        else:
            return True

