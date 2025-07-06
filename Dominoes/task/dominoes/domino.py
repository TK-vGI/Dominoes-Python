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