class Pawn:
    def __init__(self, letter, y, x):
        self.x = x
        self.y = y
        self.letter = letter

    def highlighted(self):
        move_to = input("You have selected the pawn on square {}{} Where would you like to move it to? "
                        "(or 'e' to escape): ".format(self.letter.capitalize(), self.x + 1))
        chosen_place = [char for char in move_to.lower()]
        chosen_place[0] = 7 - (ord(chosen_place[0]) - 97)
        chosen_place[1] = int(chosen_place[1])
        if self.check_if_possible(self.letter, [self.y, self.x], [chosen_place[0], chosen_place[1]]):
            return chosen_place[0], chosen_place[1] - 1
        else:
            return self.y, self.x

    def check_if_possible(self, letter, cur_pos, intended_pos):
        if cur_pos[0] - intended_pos[0] == 1 and cur_pos[1] - intended_pos[1] == 1:
            return True
        elif cur_pos[0] - intended_pos[0] == 1:
            return True
        elif cur_pos[0] - intended_pos[0] <= 2 and letter == "b":
            return True
        else:
            print("That move was not possible")
            return False

