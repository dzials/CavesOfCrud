class Entity:
    """
    A generic object to represent players, items, enemies, etc...
    """

    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move the entity by dx,dy amount
        self.x += dx
        self.y += dy
