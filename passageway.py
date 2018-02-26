import sys
from collections import deque

from createmaze import CreateMaze
from settings import Settings


class PassageWay:
    """生成迷宫通路self.path"""
    def __init__(self, gm_setting, m):
        self.m = m  # 获得迷宫数组
        self.x = len(m)    # 行
        self.y = len(m[1]) # 列
        self.gm_setting = gm_setting
        self.maze = [[0 for row in range(self.y)]for line in range(self.x)]
        self.vis = [[0 for i in range(self.y)] for i in range(self.x)]
        sys.setrecursionlimit(3600)

    def check_in_maze(self, x, y, flag=False):
        if 0 < x < self.x and 0 <= y < self.y and self.vis[x][y] == 0 and self.m[x][y] == self.gm_setting.num_road:
            return True
        return False

    def check_in_vis(self, x, y, flag=False):
        if 0 < x < self.x and 0 <= y < self.y and self.vis[x][y] != 0:
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
        for line in self.vis:
            for num in line:
                print("%4d"% num,end="")
            print()
        print("max step is:" + str(step))

    def dfs(self, now, dir):
        next = [0, 0]
        for i in range(4):
            x = next[0] = now[0] + dir[i][0]
            y = next[1] = now[1] + dir[i][1]
            if next == [1, 0]:
                return
            if self.check_in_vis(x, y) and self.maze[x][y] < self.maze[now[0]][now[1]]:
                self.path.append(next)
                self.dfs(next, dir)

    def get_path(self):
        """生成具体路径并将之从右到左存在列表path中"""
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






