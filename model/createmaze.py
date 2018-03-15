import random


class CreateMaze:
    """
    创建一个迷宫数组
    """
    # 1:up 2:down 3:left 4:right
    operation = {
        1: (0, -1),
        2: (0, 1),
        3: (-1, 0),
        4: (1, 0)
    }
    direction = [1, 2, 3, 4]

    def __init__(self):
        """
            m的值为0则为砖，为1则为通道，为2则为蛇
            设置迷宫的基本属性; x为行，y为高，m为一个表示迷宫的列表
        """
        self.x = 60
        self.y = 60
        self.m = [[0 for line in range(self.y)] for raw in range(self.x)]

    def prim(self):

        num_rows = 20
        num_cols = 20
        M = [[[0 for num in range(5)] for row in range(num_rows)] for col in range(num_cols)]
        # 设置开始位置
        r = 0
        c = 0
        history = [(r, c)]  # 标记已经使用过的数组
        while history:
            # 从已使用过的数组中随机选出一个坐标点
            r, c = random.choice(history)
            M[r][c][4] = 1  # 标记改点已被打通
            history.remove((r, c))
            check = []
            # If the randomly chosen cell has multiple edges
            # that connect it to the existing maze,
            if c > 0:
                if M[r][c - 1][4] == 1:
                    check.append('L')
                elif M[r][c - 1][4] == 0:
                    history.append((r, c - 1))
                    M[r][c - 1][4] = 2
            if r > 0:
                if M[r - 1][c][4] == 1:
                    check.append('U')
                elif M[r - 1][c][4] == 0:
                    history.append((r - 1, c))
                    M[r - 1][c][4] = 2
            if c < num_cols - 1:
                if M[r][c + 1][4] == 1:
                    check.append('R')
                elif M[r][c + 1][4] == 0:
                    history.append((r, c + 1))
                    M[r][c + 1][4] = 2
            if r < num_rows - 1:
                if M[r + 1][c][4] == 1:
                    check.append('D')
                elif M[r + 1][c][4] == 0:
                    history.append((r + 1, c))
                    M[r + 1][c][4] = 2

                    # select one of these edges at random.
            if len(check):
                move_direction = random.choice(check)
                if move_direction == 'L':
                    M[r][c][0] = 1
                    c = c - 1
                    M[r][c][2] = 1
                if move_direction == 'U':
                    M[r][c][1] = 1
                    r = r - 1
                    M[r][c][3] = 1
                if move_direction == 'R':
                    M[r][c][2] = 1
                    c = c + 1
                    M[r][c][0] = 1
                if move_direction == 'D':
                    M[r][c][3] = 1
                    r = r + 1
                    M[r][c][1] = 1

        # Open the walls at the start and finish
        M[0][0][0] = 1
        M[num_rows - 1][num_cols - 1][2] = 1

        prime_maze = [[0 for i in range(num_cols * 3)] for j in range(num_rows * 3)]
        for i in range(num_rows):
            for j in range(num_cols):
                direct = M[i][j]
                x = i * 3 + 1
                y = j * 3 + 1
                prime_maze[x][y] = 1
                if direct[0] == 1:
                    prime_maze[x][y - 1] = 1
                if direct[1] == 1:
                    prime_maze[x - 1][y] = 1
                if direct[2] == 1:
                    prime_maze[x][y + 1] = 1
                if direct[3] == 1:
                    prime_maze[x + 1][y] = 1

        self.m = prime_maze
