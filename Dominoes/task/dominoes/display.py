def print_snake(snake):
    if len(snake) <= 6:
        print("".join(str(domino) for domino in snake))
    else:
        print("".join(str(domino) for domino in snake[:3]) + "..." + "".join(str(domino) for domino in snake[-3:]))

def print_game_state(game_state):
    print("=" * 70)
    print(f"Stock size: {len(game_state['stock'])}")
    print(f"Computer pieces: {len(game_state['computer'])}")
    print()
    print_snake(game_state['snake'])
    print()
    print("Your pieces:")
    for i, piece in enumerate(game_state['player'], 1):
        print(f"{i}:{piece}")
    print()
    if game_state['status'] == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    elif game_state['status'] == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print(f"Status: The game is over. {game_state['status']}")