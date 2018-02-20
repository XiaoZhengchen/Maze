from collections import deque


class Gamestate():
    """记录游戏状态"""
    def __init__(self, gm_setting):
        self.gm_setting = gm_setting
        """
        初始化游戏状态
        """
        self.gm_state = self.gm_setting.gm_wait
        self.gm_score = 0

    @staticmethod
    def restart(snake):
        # 重置游戏状态
        snake.coordinate.clear()
        snake.coordinate = deque([(1, 0)])

