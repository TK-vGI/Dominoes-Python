from domino import Domino
from utils import generate_domino_set, shuffle_and_split

def find_starting_piece(player_pieces, computer_pieces):
    for value in range(6, -1, -1):
        double = Domino(value, value)
        if double in player_pieces:
            return double, "computer"
        if double in computer_pieces:
            return double, "player"
    return None, None

def setup_game():
    while True:
        full_set = generate_domino_set()
        stock, computer, player = shuffle_and_split(full_set)
        starting_piece, starter = find_starting_piece(player, computer)
        if starting_piece:
            if starter == "computer":
                player.remove(starting_piece)
            else:
                computer.remove(starting_piece)
            return {
                "stock": stock,
                "computer": computer,
                "player": player,
                "snake": [starting_piece],
                "status": starter,
                "turn": starter
            }

def check_game_over(player, computer, snake):
    if not player:
        return "You won!"
    if not computer:
        return "The computer won!"
    if len(snake) >= 2:
        left_end = snake[0].left
        right_end = snake[-1].right
        if left_end == right_end:
            count = sum(1 for domino in snake for num in (domino.left, domino.right) if num == left_end)
            if count >= 8:
                return "It's a draw!"
    return None

def is_valid_move(index, hand, snake):
    if index == 0:
        return True
    if abs(index) > len(hand):
        return False
    domino = hand[abs(index) - 1]
    left_end = snake[0].left
    right_end = snake[-1].right
    if index > 0:
        return domino.left == right_end or domino.right == right_end
    else:
        return domino.right == left_end or domino.left == left_end

def get_computer_move(hand, snake):
    number_counts = {i: 0 for i in range(7)}
    for domino in hand:
        number_counts[domino.left] += 1
        number_counts[domino.right] += 1
    for domino in snake:
        number_counts[domino.left] += 1
        number_counts[domino.right] += 1

    domino_scores = []
    for i, domino in enumerate(hand, 1):
        score = number_counts[domino.left] + number_counts[domino.right]
        domino_scores.append((domino, score, i))

    domino_scores.sort(key=lambda x: x[1], reverse=True)

    for domino, _, index in domino_scores:
        if is_valid_move(index, hand, snake):
            return index
        if is_valid_move(-index, hand, snake):
            return -index

    return 0

def apply_move(index, hand, snake, stock):
    if index == 0:
        if stock:
            hand.append(stock.pop())
        return
    domino = hand.pop(abs(index) - 1)
    if index > 0:
        if domino.left != snake[-1].right:
            domino = domino.flipped()
        snake.append(domino)
    else:
        if domino.right != snake[0].left:
            domino = domino.flipped()
        snake.insert(0, domino)