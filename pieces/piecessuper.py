class PiecesSuper:
    def __init__(self, letter, y, x):
        self.x = x
        self.y = y
        self.letter = letter
        self.unit_type = ""
        self.new_y = ""
        self.new_x = ""

    def highlighted(self):
        move_to = input("You have selected the {} on square {}{} Where would you like to move it to? "
                        "(or 'e' to escape): ".format(self.unit_type, self.letter.capitalize(), self.x + 1))
        chosen_place = [char for char in move_to.lower()]
        chosen_place[0] = 7 - (ord(chosen_place[0]) - 97)
        chosen_place[1] = int(chosen_place[1])
        self.new_y = chosen_place[0]
        self.new_x = chosen_place[1]

