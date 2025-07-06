import random
from domino import Domino

def generate_domino_set():
    return [Domino(i, j) for i in range(7) for j in range(i, 7)]

def shuffle_and_split(domino_set):
    for _ in range(4):
        random.shuffle(domino_set)
    player_pieces = domino_set[:7]
    computer_pieces = domino_set[7:14]
    stock_pieces = domino_set[14:]
    return stock_pieces, computer_pieces, player_pieces

def find_starting_piece(player_pieces, computer_pieces):
    highest_double = None
    starter = None

    for value in reversed(range(7)):  # Check from [6,6] down to [0,0]
        double = Domino(value, value)
        if double in player_pieces:
            highest_double = double
            starter = "player"
            break
        elif double in computer_pieces:
            highest_double = double
            starter = "computer"
            break

    return highest_double, starter
