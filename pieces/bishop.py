from pieces.piecessuper import PiecesSuper


class Bishop(PiecesSuper):
    def __init__(self, letter, y, x):
        super().__init__(letter, y, x)
        self.unit_type = "bishop"

    def move_bishop(self):
        if self.check_if_possible():
            booler, direction = self.check_if_possible()
            return self.new_y, self.new_x - 1, direction
        else:
            return self.y, self.x, None

    def check_if_possible(self):
        possible = abs(self.new_x - self.x) - abs(self.new_y - self.y)
        print(possible)
        if possible == 1:
            return True, "left_diag"
        elif possible == -1:
            return True, "right_diag"
        else:
            print("That move was not possible")
            return False
