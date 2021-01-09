# This file contains the main chess board

# Main chess class


class Chess:
    def __init__(self):
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
