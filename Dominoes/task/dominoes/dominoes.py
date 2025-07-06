from utils import generate_domino_set, shuffle_and_split, find_starting_piece
from display import print_game_state
# import title

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

if __name__ == "__main__":
    # title.print_title()
    game_state = setup_game()
    print_game_state(game_state)