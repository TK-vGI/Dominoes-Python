def print_game_state(game_state):
    print("=" * 70)
    print(f"Stock size: {len(game_state['stock'])}")
    print(f"Computer pieces: {len(game_state['computer'])}")
    print()

    # Print the domino snake
    snake = game_state["snake"]
    if len(snake) == 1:
        print(snake[0])
    else:
        print("".join(str(d) for d in snake))
    print()

    # Print player's pieces
    print("Your pieces:")
    for idx, domino in enumerate(game_state["player"], 1):
        print(f"{idx}:{domino}")
    print()

    # Print status
    if game_state["turn"] == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")
