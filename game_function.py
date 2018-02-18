import pygame
import sys

from brick import Brick


def update_show_range(gm_setting, screen, event, head):
    # 更新显示的迷宫区域
    mid = (gm_setting.show_bottom - gm_setting.show_top) / 2
    mid_x = mid + gm_setting.show_top
    mid_y = mid + gm_setting.show_left
    """
    print("head:" + str(head) + ',' + "mid:(" + str(mid_x),str(mid_y) + ")",end=",")
    print("left:" + str(gm_setting.show_left) + ",right:" + str(gm_setting.show_right) +
          ",top:" + str(gm_setting.show_top) + ",bottom:" + str(gm_setting.show_bottom))
    """
    if event.key in [pygame.K_LEFT, pygame.K_a]:
        if head[1] == mid_y - 1 and gm_setting.show_left > 0:
            gm_setting.show_left -= 1
            gm_setting.show_right -= 1
    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
        if head[1] == mid_y - 1 and gm_setting.show_right < 60:
            gm_setting.show_left += 1
            gm_setting.show_right += 1
    elif event.key in [pygame.K_UP, pygame.K_w]:
        if head[0] == mid_x - 1 and gm_setting.show_top > 0:
            gm_setting.show_top -= 1
            gm_setting.show_bottom -= 1
    elif event.key in [pygame.K_DOWN, pygame.K_s]:
        if head[0] == mid_x - 1 < 60 and gm_setting.show_bottom < 60:
            gm_setting.show_bottom += 1
            gm_setting.show_top += 1


def check_keydown(screen, gm_setting, snake, maze, event):
    """响应按键事件"""
    head = snake_head_get(snake, gm_setting)

    if event.key in [pygame.K_LEFT, pygame.K_a]:
        if snake.left(maze.m):
            update_show_range(gm_setting, screen, event, head)
    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
        if snake.right(maze.m):
            update_show_range(gm_setting, screen, event, head)
    elif event.key in [pygame.K_UP, pygame.K_w]:
        if snake.up(maze.m):
            update_show_range(gm_setting, screen, event, head)
    elif event.key in [pygame.K_DOWN, pygame.K_s]:
        if snake.down(maze.m):
            update_show_range(gm_setting, screen, event, head)


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


def check_show(gm_setting, brick):
    """查看当前砖块是否在显示范围"""
    if (brick.pos[1] in range(gm_setting.show_left, gm_setting.show_right) and
               brick.pos[0] in range(gm_setting.show_top, gm_setting.show_bottom)):
        return True
    else:
        return False


def update_screen(screen, gm_setting, bricks, dir_button):

    # 颜色填充屏幕
    screen.fill(gm_setting.bg_color)

    # 绘制砖块
    for new_brick in bricks:
        if check_show(gm_setting, new_brick):
            new_brick.draw_brick(gm_setting)
    # 绘制方向键
    dir_button.blitme()
    # 更新屏幕
    pygame.display.flip()

