import pygame
import sys

from brick import Brick


def check_keydown(screen, gm_setting, snake, maze, event):
    if event.key == pygame.K_LEFT:
        snake.left(maze.m)
    elif event.key == pygame.K_RIGHT:
        snake.right(maze.m)
    elif event.key == pygame.K_UP:
        snake.up(maze.m)
    elif event.key == pygame.K_DOWN:
        snake.down(maze.m)

def check_keyup(screen, gm_setting, snake, maze, event):
    return 0


def check_events(screen, gm_setting, snake, maze):
    """响应按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(screen, gm_setting, snake, maze, event)
        elif event.type == pygame.KEYUP:
            check_keyup(screen, gm_setting, snake,maze,  event)


def create_maze(screen, gm_setting, maze, bricks, i, j):
    # 根据迷宫的二维列表来创建单个砖块加入编组
    brick = Brick(gm_setting, screen)
    brick.pos = (i, j)
    brick.rect.bottom = brick.width * (i + 1)
    brick.rect.right = brick.width * (j + 1)
    brick.color = gm_setting.maze_color[maze.m[i][j]]
    bricks.add(brick)


def create_maze_group(screen, gm_setting, maze, bricks):
    # 创建迷宫编组
    for i in range(len(maze.m)):
        for j in range(len(maze.m[i])):
            # 创建单个砖块并加入编组
            create_maze(screen, gm_setting, maze, bricks, i, j)


def snake_head_get(snake, gm_setting):
    # 获得蛇的头部坐标
    if snake.len == 1:
        head = snake.coordinate[0]
    elif snake.dir == gm_setting.snake_dir_right:
        head = snake.coordinate[-1]
    elif snake.dir == gm_setting.snake_dir_left:
        head = snake.coordinate[0]
    return head


def snake_tail_get(snake, gm_setting):
    # 获得蛇的尾部坐标
    if snake.len == 1:
        tail = snake.coordinate[0]
    elif snake.dir == gm_setting.snake_dir_right:
        tail = snake.coordinate[0]
    elif snake.dir == gm_setting.snake_dir_left:
        tail = snake.coordinate[-1]
    return tail


def update_maze(gm_setting, maze, snake, bricks):
    """通过snake来更新maze的值"""
    # 首先先将maze中的snake初始化为空白的道路
    for x in range(len(maze.m)):
        for y in range(len(maze.m[x])):
            if maze.m[x][y] == gm_setting.num_snake or maze.m[x][y] == gm_setting.num_snake_head:
                maze.m[x][y] = gm_setting.num_road

    # 根据snake来更新maze的值
    for point in snake.coordinate:
        maze.m[point[0]][point[1]] = gm_setting.num_snake

    head = snake_head_get(snake, gm_setting)
    maze.m[head[0]][head[1]] = gm_setting.num_snake_head
    # 因为maze改变了，所以对bricks的编组进行更新
    update_brick_group(gm_setting, bricks, maze)


def update_brick_group(gm_setting, bricks, maze):
    """更新砖块的编组"""
    for brick in bricks:
        x = brick.pos[0]
        y = brick.pos[1]
        brick.color = gm_setting.maze_color[maze.m[x][y]]


def update_screen(screen, gm_setting, bricks, dir_button):
    # 颜色填充屏幕
    screen.fill(gm_setting.bg_color)

    # 绘制砖块
    for new_brick in bricks:
        new_brick.draw_brick()
        # if new_brick.color == gm_setting.
    # 绘制方向键
    dir_button.blitme()
    # 更新屏幕
    pygame.display.flip()

