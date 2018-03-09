import json
import sys

import pygame

from mould.brick import Brick


def init(ranklist):
    """
    在游戏开始时运行，读取存档内容
    :return:
    """
    try:
        filename = "rank_file.json"
        with open(filename) as rankfile:
            ranklist.rank = json.load(rankfile)
    except FileNotFoundError:
        filename = "rank_file.json"
        with open(filename, "w") as rankfile:
            json.dump(0, rankfile)


def update_show_range(gm_setting, screen, event, head, dir=False):
    # 更新显示的迷宫区域
    now_left = head[1] - 10
    now_right = head[1] + 10
    now_top = head[0] - 10
    now_bottom = head[0] + 10
    if 0 <= now_left <= 40:
        gm_setting.show_left = now_left
        gm_setting.show_right = now_right
    if 0 <= now_top <= 40:
        gm_setting.show_top = now_top
        gm_setting.show_bottom = now_bottom


def check_keydown(screen, gm_setting, snake, maze, event, fruits):
    """响应按键事件"""
    head = snake_head_get(snake, gm_setting)

    if event.key in [pygame.K_LEFT, pygame.K_a]:
        if snake.left(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head)
    elif event.key in [pygame.K_RIGHT, pygame.K_d]:
        if snake.right(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head)
    elif event.key in [pygame.K_UP, pygame.K_w]:
        if snake.up(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head)
    elif event.key in [pygame.K_DOWN, pygame.K_s]:
        if snake.down(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head)


def check_keyup(screen, gm_setting, snake, maze, event):
    return 0


def check_play_button(screen, gm_setting, snake, maze, state, page, mouse_x, mouse_y, fruits):
    """检测鼠标点击事件"""
    # 玩家单击play按钮开始游戏
    button_clicked = page.gm_play_rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # 重置游戏状态
        state.restart(snake, gm_setting, state, fruits, maze)
        state.gm_state = gm_setting.gm_run


def check_rank_button(screen, gm_setting, snake, maze, state, page, mouse_x, mouse_y):
    # 玩家单击Rank按钮查看排行榜
    button_clicked = page.gm_rank_rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # 重置游戏状态
        state.gm_state = gm_setting.gm_rank


def check_exit_button(screen, gm_setting, snake, maze, state, page, mouse_x, mouse_y):
    """检测鼠标点击事件"""
    # 玩家单击exit按钮结束游戏
    button_clicked = page.gm_exit_rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        # 重置游戏状态
        state.gm_state = gm_setting.gm_wait
        state.restart(snake, gm_setting, state)


def check_dir_button(screen, gm_setting, event, snake, maze, mouse_x, mouse_y, dir_button, fruits):
    """响应方向按键"""
    head = snake_head_get(snake, gm_setting)
    left_clicked = dir_button.leftRect.collidepoint(mouse_x, mouse_y)
    up_clicked = dir_button.upRect.collidepoint(mouse_x, mouse_y)
    right_clicked = dir_button.rightRect.collidepoint(mouse_x, mouse_y)
    down_clicked = dir_button.downRect.collidepoint(mouse_x, mouse_y)
    if left_clicked and snake.left(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head, True)
    if right_clicked and snake.right(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head, True)
    if up_clicked and snake.up(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head, True)
    if down_clicked and snake.down(maze.m, fruits):
            update_show_range(gm_setting, screen, event, head, True)


def check_prop(ans_prop, mouse_x, mouse_y):
    """响应道具的点击事件    """
    prop_checked = ans_prop.prop_rect.collidepoint(mouse_x, mouse_y)
    if prop_checked:
        ans_prop.effect()


def check_events(screen, gm_setting, snake, maze, state, start_page, end_page, ranklist, fruits="", dir_button="", ans_prop=""):
    """响应按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出并存档
            filename = "rank_file.json"
            with open(filename, 'w') as rankfile:
                json.dump(ranklist.rank, rankfile)
            sys.exit()
        if state.gm_state == gm_setting.gm_run:
            # 开始游戏后需要响应的事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state.gm_state = gm_setting.gm_wait
                    return
                check_keydown(screen, gm_setting, snake, maze, event, fruits)
            elif event.type == pygame.KEYUP:
                check_keyup(screen, gm_setting, snake, maze,  event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_dir_button(screen, gm_setting, event, snake, maze, mouse_x, mouse_y, dir_button, fruits.pos)
                check_prop(ans_prop, mouse_x, mouse_y)

        elif state.gm_state == gm_setting.gm_wait:
            # 等待游戏开始时需要响应的事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(screen, gm_setting, snake, maze, state, start_page, mouse_x, mouse_y, fruits)
                check_rank_button(screen, gm_setting, snake, maze, state, start_page, mouse_x, mouse_y)
        elif state.gm_state == gm_setting.gm_end:
            # 游戏结束时需要响应的事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(screen, gm_setting, snake, maze, state, end_page, mouse_x, mouse_y, fruits)
                check_exit_button(screen, gm_setting, snake, maze, state, end_page, mouse_x, mouse_y)
        elif state.gm_state == gm_setting.gm_rank:
            # 排行榜界面响应esc键回到开始界面
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state.gm_state = gm_setting.gm_wait


def check_snake_out(screen, gm_setting, maze, snake, state, ranklist, score):
    head = snake_head_get(snake, gm_setting)
    if head[0] == len(maze.m) - 2 and head[1] == len(maze.m[1]) - 1:
        state.gm_state = gm_setting.gm_end
        # 更新排行榜
        ranklist.update_rank(score.score)


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
    if len(snake.coordinate) == 1:
        head = snake.coordinate[0]
    else:
        if snake.dir == gm_setting.snake_dir_right:
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


def update_maze(gm_setting, maze, snake, bricks, state, fruits, ans=[]):
    """通过snake来更新maze的值"""
    # 首先先将maze中的snake初始化为空白的道路
    for x in range(len(maze.m)):
        for y in range(len(maze.m[x])):
            if maze.m[x][y] != gm_setting.num_brick:
                maze.m[x][y] = gm_setting.num_road

    # 根据ans来更新矩阵
    if state.show_ans:
        # print("path:", ans)
        for point in ans:
            maze.m[point[0]][point[1]] = gm_setting.num_ans

    for fruit in fruits.pos:
        x = fruit[0]
        y = fruit[1]
        maze.m[x][y] = gm_setting.num_fruit

    # 根据snake来更新maze的值
    # head = snake_head_get(snake, gm_setting)
    head = snake.get_head()
    for point in snake.coordinate:
        if point == head:
            continue
        maze.m[point[0]][point[1]] = gm_setting.num_snake


    maze.m[head[0]][head[1]] = gm_setting.num_snake_head
    # 因为maze改变了，所以对bricks的编组进行更新
    update_brick_group(gm_setting, bricks, maze)


def update_brick_group(gm_setting, bricks, maze):
    """更新砖块的编组"""
    for brick in bricks:
        x = brick.pos[0]
        y = brick.pos[1]
        brick.color = gm_setting.maze_color[maze.m[x][y]]


def update_score(score, state):
    score.score = (state.gm_end_time - state.gm_start_time).seconds


def check_show(gm_setting, brick):
    """查看当前砖块是否在显示范围"""
    if (brick.pos[1] in range(gm_setting.show_left, gm_setting.show_right) and
               brick.pos[0] in range(gm_setting.show_top, gm_setting.show_bottom)):
        return True
    else:
        return False


def update_screen(screen, gm_setting, bricks, dir_button, score, ans_prop):

    # 颜色填充屏幕
    screen.fill(gm_setting.bg_color)

    # 绘制砖块
    for new_brick in bricks:
        if check_show(gm_setting, new_brick):
            new_brick.draw_brick(gm_setting)

    # 绘制道具
    ans_prop.show()
    # 绘制方向键
    dir_button.blitme()
    # 绘制分数
    score.show_page()
    # 更新屏幕
    pygame.display.flip()

