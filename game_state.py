from collections import deque
import datetime


class Gamestate:
    """记录游戏状态"""
    def __init__(self, gm_setting):
        self.gm_setting = gm_setting
        """
        初始化游戏状态
        """
        self.gm_state = self.gm_setting.gm_welcome
        self.gm_start_time = datetime.datetime.now()
        self.gm_end_time = datetime.datetime.now()
        self.show_ans = True
        self.gm_score = (self.gm_end_time - self.gm_start_time).seconds

    def restart(self, snake, gm_setting, state):
        # 重置蛇的位置以及长度
        snake.coordinate.clear()
        snake.coordinate = deque([(1, 0)])
        # 重置屏幕的显示范围
        gm_setting.show_top = 0
        gm_setting.show_left = 0
        gm_setting.show_right = 20
        gm_setting.show_bottom = 20
        # 重置游戏开始时间
        state.gm_start_time = datetime.datetime.now()
        state.gm_end_time = datetime.datetime.now()
        # 重置游戏状态
        state.show_ans = False