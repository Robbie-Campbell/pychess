class Pawn:
    def __init__(self, letter, y, x):
        self.x = x
        self.y = y
        self.letter = letter
        self.new_y = ""
        self.new_x = ""

    def highlighted(self):
        move_to = input("You have selected the pawn on square {}{} Where would you like to move it to? "
                        "(or 'e' to escape): ".format(self.letter.capitalize(), self.x + 1))
        chosen_place = [char for char in move_to.lower()]
        chosen_place[0] = 7 - (ord(chosen_place[0]) - 97)
        chosen_place[1] = int(chosen_place[1])
        self.new_y = chosen_place[0]
        self.new_x = chosen_place[1]

    def move_pawn(self, enemy_present):
        if self.check_if_possible(self.letter, [self.y, self.x], [self.new_y, self.new_x], enemy_present):
            return self.new_y, self.new_x - 1
        else:
            return self.y, self.x

    def check_if_possible(self, letter, cur_pos, intended_pos, enemy_present):
        if (cur_pos[0] - intended_pos[0]) == 1 and (cur_pos[1] - intended_pos[1]) + 1 == 1 and enemy_present == "Enemy":
            return True
        elif not enemy_present == "Ally":
            print("You have an ally in that pieces place")
            return False
        elif cur_pos[0] - intended_pos[0] == 1 and cur_pos[1] - intended_pos[1] + 1 == 0 and not enemy_present:
            return True
        elif cur_pos[0] - intended_pos[0] <= 2 and cur_pos[1] - intended_pos[1] + 1 == 0 and letter == "b" and not \
                enemy_present:
            return True
        else:
            print("That move was not possible")
            return False

