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
        possible = self.new_y - self.new_x
        also_possible = self.new_x + self.new_y
        print(self.x)
        if possible == 0:
            return True, "left_diag"
        if also_possible == 0:
            return True, "right_diag"
        else:
            print("That move was not possible")
            return False
