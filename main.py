from chess import Chess

# Runs the main program

if __name__ == '__main__':
    game = Chess()
    for line in (game.board):
        print(str(line) + "\n")