from pieces.piecessuper import PiecesSuper


class Pawn(PiecesSuper):
    def __init__(self, letter, y, x):
        super().__init__(letter, y, x)
        self.unit_type = "pawn"

    def move_pawn(self, enemy_present):
        if self.check_if_possible(self.letter, [self.y, self.x], [self.new_y, self.new_x], enemy_present):
            return self.new_y, self.new_x - 1
        else:
            return self.y, self.x

    def check_if_possible(self, letter, cur_pos, intended_pos, enemy_present):
        if (cur_pos[0] - intended_pos[0]) == 1 and (cur_pos[1] - intended_pos[1]) + 1 == 1 and enemy_present == "Enemy":
            return True
        elif enemy_present == "Ally":
            print("You have an ally in that pieces place")
            return False
        elif cur_pos[0] - intended_pos[0] == 1 and cur_pos[1] - intended_pos[1] + 1 == 0 and not enemy_present:
            return True
        elif cur_pos[0] - intended_pos[0] <= 2 and cur_pos[1] - intended_pos[1] + 1 == 0 and letter == "b" and \
                not enemy_present:
            return True
        else:
            print("That move was not possible")
            return False
