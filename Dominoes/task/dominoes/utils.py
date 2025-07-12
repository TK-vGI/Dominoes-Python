from domino import Domino

def generate_domino_set():
    return [Domino(i, j) for i in range(7) for j in range(i, 7)]

def shuffle_and_split(domino_set):
    import random
    random.shuffle(domino_set)
    return domino_set[:14], domino_set[14:21], domino_set[21:]