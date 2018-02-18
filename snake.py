from collections import deque


class Snake:

    def __init__(self, gm_setting):
        self.gm_setting = gm_setting
        self.coordinate = deque([(1, 0)])
        self.len = len(self.coordinate)
        self.color = self.gm_setting.snake_color
        # 设置蛇的方向,便于操作双端队列,1头为右,0头为左
        self.dir = self.gm_setting.snake_dir_right

    @staticmethod
    def check_moved(self, m, x, y):
        # 判断这个移动是否合法
        if m[x][y] == self.gm_setting.num_brick:
            return False
        elif m[x][y] == self.gm_setting.num_snake:
            return False
        elif m[x][y] == self.gm_setting.num_road:
            return True

    def head_update(self, head):
        if self.dir == self.gm_setting.snake_dir_right:
            self.coordinate.append(head)
            self.coordinate.popleft()
        else:
            self.coordinate.appendleft(head)
            self.coordinate.pop()

    def get_head(self):
        if self.len == 1:
            # 初始状态下的蛇为一个点,并且默认双端队列的右侧为蛇头
            head = self.coordinate[0]
        elif self.len > 1:
            # 蛇的长度大于1
            if self.dir == self.gm_setting.snake_dir_right:
                # 双端队列的右边为头
                head = self.coordinate[-1]
            else:
                # 双端队列的左边为头
                head = self.coordinate[0]
        return head

    def left(self, m):
        """控制蛇向左行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_y -= 1
        if self.check_moved(self, m, head_x, head_y):
            # 更新头部位置
            self.head_update((head_x, head_y))
            return True
        return False

    def right(self, m):
        """控制蛇向右行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_y += 1
        if self.check_moved(self, m, head_x, head_y):
            # 更新头部位置
            self.head_update((head_x, head_y))
            return True
        return False

    def up(self, m):
        """控制蛇向上行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_x -= 1
        if self.check_moved(self, m, head_x, head_y):
            # 更新头部位置
            self.head_update((head_x, head_y))
            return True
        return False

    def down(self, m):
        """控制蛇向下行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_x += 1
        if self.check_moved(self, m, head_x, head_y):
            # 更新头部位置
            self.head_update((head_x, head_y))
            return True
        return False
