import sys
from collections import deque


class PassageWay:
    """生成迷宫通路self.path"""
    def __init__(self, gm_setting, m):
        self.m = m  # 获得迷宫数组
        self.x = len(m)    # 行
        self.y = len(m[1]) # 列
        self.gm_setting = gm_setting
        self.level = 0
        self.maze = [[0 for row in range(self.y)]for line in range(self.x)]
        self.vis = [[0 for i in range(self.y)] for i in range(self.x)]
        sys.setrecursionlimit(3600)

    def check_in_maze(self, x, y, flag=False):
        if 0 < x < self.x and 0 <= y < self.y and self.vis[x][y] == 0 and self.m[x][y] == self.gm_setting.num_road:
            return True
        return False

    def check_in_vis(self, x, y):
        if 0 < x < self.x and 0 < y < self.y and self.vis[x][y] != 0:
            return True
        return False

    def answer(self):
        """生成标记数组"""
        # 使用一个双端队列来实现队列的功能,左进右出
        queue = deque([])

        now = (1, 0)
        self.vis[now[0]][now[1]] = 1
        dir = {
            0: (0, 1),   # 右
            1: (1, 0),   # 下
            2: (0, -1),  # 左
            3: (-1, 0),  # 上
        }
        queue.appendleft(now)
        step = 0
        while len(queue) != 0:
            now = queue.pop()
            for i in range(4):
                next = [0, 0]
                next[0] = now[0] + dir[i][0]
                next[1] = now[1] + dir[i][1]
                if self.check_in_maze(next[0], next[1]):
                    queue.appendleft(next)
                    self.vis[next[0]][next[1]] = self.vis[now[0]][now[1]] + 1
                    if next[0] == self.x - 2 and next[1] == self.y - 1:
                        step = max(self.vis[next[0]][next[1]], step)
                        break
        self.maze = self.vis

    def dfs(self, now, dir):
        for i in range(4):
            x = now[0] + dir[i][0]
            y = now[1] + dir[i][1]
            if self.check_in_vis(x, y) and self.maze[x][y] < self.maze[now[0]][now[1]]:
                self.path.append([x, y])
                if [x, y] == [1, 0]:
                    return
                self.dfs([x, y], dir)

    def get_path(self):
        """生成具体路径并将之从右到左存在列表path中"""
        self.answer()
        self.path = []
        x = self.x - 2
        y = self.y - 1
        now = [x, y]
        dir = {
            0: (0, 1),  # 右
            1: (1, 0),  # 下
            2: (0, -1),  # 左
            3: (-1, 0),  # 上
        }
        self.path.append(now)
        self.dfs(now, dir)
        self.path.reverse()

    def get_level(self):
        # 读取难度级别
        dir = {
            0: (0, 1),  # 右
            1: (1, 0),  # 下
            2: (0, -1),  # 左
            3: (-1, 0),  # 上
        }
        # print("x,y", self.x, self.y)
        for x, y in self.path:
            # print(x, y)
            branch = 0
            for i in range(4):
                nextx = x + dir[i][0]
                nexty = y + dir[i][1]
                # print(nextx, nexty, end=",")
                if 0 < nextx < self.x and 0 <= nexty < self.y:
                    # print(self.m[nextx][nexty])
                    if self.m[nextx][nexty] == self.gm_setting.num_road:
                        branch += 1
            if branch > 2:
                self.level += 1
            print("")




