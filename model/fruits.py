import random


class Fruits:
    """果实类，吃了之后蛇的长度会增加"""
    def __init__(self, maze, ans):
        self.pos = []
        self.ans = ans

    def update(self):
        self.pos = random.sample(self.ans, 10)
        # self.pos.append([1, 1])
        self.pos.reverse()