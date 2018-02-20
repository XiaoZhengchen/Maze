class Settings:
    """
    包含所有的基本设置
    """
    def __init__(self):
        """一些游戏开始时不会改变的静态设置"""
        # 设置窗口的高宽,背景色
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 设置迷宫范围
        self.maze_width = 600
        self.maze_height = 600

        # 设置砖块的高宽,颜色
        self.brick_width = 30
        self.brick_height = 30
        self.brick_color = (0, 0, 0)

        # 通道的颜色
        self.road_color = (255, 255, 255)

        # 蛇的颜色
        self.snake_color = (0, 255, 0)
        # 蛇头的颜色
        self.snake_head_color = (255, 0, 0)
        # 蛇的头在双端队列的方向
        self.snake_dir_left = 0
        self.snake_dir_right = 1

        # m的值为0则为砖，为1则为通道，为2则为蛇
        self.num_brick = 0
        self.num_road = 1
        self.num_snake = 2
        self.num_snake_head = 3

        # 颜色与方块类型的对应
        self.maze_color = {
            0: self.brick_color,
            1: self.road_color,
            2: self.snake_color,
            3: self.snake_head_color
        }

        # 设置迷宫的初始显示范围
        self.show_top = 0
        self.show_left = 0
        self.show_right = 20
        self.show_bottom = 20

        # 设置游戏状态：0表示游戏未开始，1表示游戏进行中，2表示已游戏结束
        self.gm_wait = 0
        self.gm_run = 1
        self.gm_end = 2
