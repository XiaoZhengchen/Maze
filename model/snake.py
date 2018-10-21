from collections import deque


class Snake:

    def __init__(self, gm_setting):
        self.gm_setting = gm_setting
        self.coordinate = deque([[1, 0]])
        self.len = len(self.coordinate)
        self.color = self.gm_setting.snake_color
        # 设置蛇的方向,便于操作双端队列,1头为右,0头为左
        self.dir = self.gm_setting.snake_dir_right
        # 标记已经被自增的长度值，因为每一帧的刷新次数高于一秒
        self.Flag_Score = [0]
        
    def check_moved(self, m, x, y, flag=True):
        # 判断这个移动是否合法
        if y in range(len(m)) and x in range(len(m)):
            if m[x][y] == self.gm_setting.num_brick:
                return False
            elif m[x][y] == self.gm_setting.num_snake:
                if flag:
                    self.dir *= -1
                return False
            elif m[x][y] == self.gm_setting.num_road:
                return True
            elif m[x][y] == self.gm_setting.num_ans:
                return True
            elif m[x][y] == self.gm_setting.num_fruit:
                return True
        else:
            return False

    def head_update(self, head, fruits):
        flag = True
        if head in fruits.pos:
            fruits.pos.remove(head)
            flag = False
        if self.dir == self.gm_setting.snake_dir_right:
            self.coordinate.append(head)
            if flag:
                self.coordinate.popleft()
        else:
            self.coordinate.appendleft(head)
            if flag:
                self.coordinate.pop()

    def tail_update(self, score, m):
        """尾自增"""
        if len(self.coordinate) == 1:
            return
        mov = {
            0: [0, 1],
            1: [0, -1],
            2: [1, 0],
            3: [-1, 0]
        }
        tail = self.get_tail(self.gm_setting)
        if score % 10 == 0:
            if score in self.Flag_Score:
                pass
            else:
                # print("score", score)
                # print("ScoreFlag", self.Flag_Score)
                self.Flag_Score.append(score)
                for i in range(4):
                    x = tail[0] + mov[i][0]
                    y = tail[1] + mov[i][1]
                    if self.check_moved(m, x, y, False):
                        if self.dir == self.gm_setting.snake_dir_right:
                            self.coordinate.appendleft([x, y])
                        else:
                            self.coordinate.append([x, y])
                        # print(self.dir, self.coordinate)
                        break
        
    def get_head(self):
        self.len = len(self.coordinate)
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

    def get_tail(self, gm_setting):
        # 获得蛇的尾部坐标
        if self.len == 1:
            tail = self.coordinate[0]
        elif self.dir == gm_setting.snake_dir_right:
            tail = self.coordinate[0]
        elif self.dir == gm_setting.snake_dir_left:
            tail = self.coordinate[-1]
        return tail

    def left(self, m, fruits):
        """控制蛇向左行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        
        head_y = head[1]
        head_y -= 1
        if self.check_moved(m, head_x, head_y):
            # 更新头部位置
            self.head_update([head_x, head_y], fruits)
            return True
        return False

    def right(self, m, fruits):
        """控制蛇向右行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_y += 1
        if self.check_moved(m, head_x, head_y):
            # 更新头部位置
            self.head_update([head_x, head_y], fruits)
            return True
        return False

    def up(self, m, fruits):
        """控制蛇向上行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_x -= 1
        if self.check_moved(m, head_x, head_y):
            # 更新头部位置
            self.head_update([head_x, head_y], fruits)
            return True
        return False

    def down(self, m, fruits):
        """控制蛇向下行走,m为迷宫数组"""
        head = self.get_head()
        head_x = head[0]
        head_y = head[1]
        head_x += 1
        if self.check_moved(m, head_x, head_y):
            # 更新头部位置
            self.head_update([head_x, head_y], fruits)
            return True
        return False
