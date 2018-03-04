import random


class Fruits:
    """果实类，吃了之后蛇的长度会增加"""
    def __init__(self, maze, ans):
        self.pos = []

        self.pos = random.sample(ans, 10)
        # self.pos.append([1, 1])
        self.pos.reverse()