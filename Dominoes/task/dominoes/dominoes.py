from game import setup_game, check_game_over, is_valid_move, get_computer_move, apply_move
from display import print_game_state

def game_loop():
    game_state = setup_game()
    while True:
        result = check_game_over(game_state["player"], game_state["computer"], game_state["snake"])
        if result:
            game_state["status"] = result
            print_game_state(game_state)
            break
        print_game_state(game_state)
        if game_state["turn"] == "player":
            while True:
                move = input()
                try:
                    move = int(move)
                    if abs(move) > len(game_state["player"]):
                        print("Invalid input. Please try again.")
                        continue
                    if not is_valid_move(move, game_state["player"], game_state["snake"]):
                        print("Illegal move. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
                    continue
            apply_move(move, game_state["player"], game_state["snake"], game_state["stock"])
            game_state["turn"] = "computer"
            game_state["status"] = "computer"
        else:
            input()
            move = get_computer_move(game_state["computer"], game_state["snake"])
            apply_move(move, game_state["computer"], game_state["snake"], game_state["stock"])
            game_state["turn"] = "player"
            game_state["status"] = "player"

if __name__ == "__main__":
    import random
    random.seed()
    game_loop()