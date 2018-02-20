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

    def restart(self, snake, gm_setting):
        # 重置蛇的位置以及长度
        snake.coordinate.clear()
        snake.coordinate = deque([(1, 0)])
        # 重置屏幕的显示范围
        gm_setting.show_top = 0
        gm_setting.show_left = 0
        gm_setting.show_right = 20
        gm_setting.show_bottom = 20

