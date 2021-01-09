
class Pawn:
    def __init__(self, letter, y, x):
        self.x = x
        self.y = y
        self.letter = letter

    def highlighted(self):
        if self.letter == "b":
            space = input("You have selected the pawn on square {}{} Would you like to move it forward '1' square or "
                          "'2'? (or 'e' to escape): ".format(self.letter.capitalize(), self.x))
            if space == '1':
                return self.y - 1

            elif space == '2':
                return self.y - 2

            else:
                return self.y

        else:
            confirm = input(
                "You have selected the pawn on square {}{}, Type '1' to move it forward 1 square or 'e' to escape: "
                .format(self.letter.capitalize(), self.x))
            if confirm == '1':
                return self.y - 1
            else:
                return self.y
