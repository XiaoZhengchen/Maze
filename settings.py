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

        # 屏幕的背景色
        self.screen_color = (122, 193, 216)
        # 通道的颜色
        self.road_color = (255, 255, 255)
        # 蛇的颜色
        self.snake_color = (206, 193, 122)
        # 蛇头的颜色
        self.snake_head_color = (255, 0, 0)
        # 答案的颜色
        self.ans_color = (100, 186, 187)
        # 障碍果实的颜色
        self.fruit_color = (124, 206, 122)

        # 蛇的头在双端队列的方向
        self.snake_dir_left = -1
        self.snake_dir_right = 1

        # m的值为0则为砖，为1则为通道，为2则为蛇，3为蛇头，4为通路，5为果实使长度增加
        self.num_brick = 0
        self.num_road = 1
        self.num_snake = 2
        self.num_snake_head = 3
        self.num_ans = 4
        self.num_fruit = 5

        # 颜色与方块类型的对应
        self.maze_color = {
            0: self.brick_color,
            1: self.road_color,
            2: self.snake_color,
            3: self.snake_head_color,
            4: self.ans_color,
            5: self.fruit_color
        }

        # 设置迷宫的初始显示范围
        self.show_top = 0
        self.show_left = 0
        self.show_right = 20
        self.show_bottom = 20

        # 设置游戏状态：0表示游戏未开始，1表示游戏进行中，2表示已游戏结束，3表示查看排行榜，4为欢迎界面
        self.gm_wait = 0
        self.gm_run = 1
        self.gm_end = 2
        self.gm_rank = 3
        self.gm_welcome = 4
