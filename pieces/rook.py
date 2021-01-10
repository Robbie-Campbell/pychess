from pieces.piecessuper import PiecesSuper


class Rook(PiecesSuper):
    def __init__(self, letter, y, x):
        super().__init__(letter, y, x)
        self.unit_type = "rook"

    def move_rook(self):
        if self.check_if_possible(self.letter, [self.y, self.x]):
            booler, direction = self.check_if_possible(self.letter, [self.y, self.x])
            return self.new_y, self.new_x - 1, direction
        else:
            return self.y, self.x, None

    def check_if_possible(self, cur_pos, intended_pos):
        if cur_pos[0] == intended_pos[0]:
            return True, "x_change"
        elif cur_pos[1] == intended_pos[1] - 1:
            return True, "y_change"
        else:
            print("That move was not possible")
            return False
