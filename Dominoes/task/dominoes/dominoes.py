import random
# import title

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

def setup_game():
    while True:
        full_set = generate_domino_set()
        stock, computer, player = shuffle_and_split(full_set)
        starting_piece, starter = find_starting_piece(player, computer)

        if starting_piece:
            if starter == "player":
                player.remove(starting_piece)
                first_turn = "computer"
            else:
                computer.remove(starting_piece)
                first_turn = "player"

            return {
                "stock": stock,
                "player": player,
                "computer": computer,
                "snake": [starting_piece],
                "turn": first_turn
            }

class Domino:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def __eq__(self, other):
        return (self.left, self.right) == (other.left, other.right)

    def __hash__(self):
        return hash((self.left, self.right))

if __name__ == "__main__":
    # title.print_title()
    game_state = setup_game()
    print("Stock pieces:", game_state["stock"])
    print("Computer pieces:", game_state["computer"])
    print("Player pieces:", game_state["player"])
    print("Domino snake:", game_state["snake"])
    print("Status:", game_state["turn"])