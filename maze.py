import pygame

from settings import Settings
from pygame.sprite import Group
import game_function as gf
from createmaze import CreateMaze
from directionButton import DirectionButton
from snake import Snake


def run_game():
    """
    主程序负责执行游戏
    """
    pygame.init()
    # 实例化设置类
    gm_setting = Settings()
    # 初始化屏幕
    screen = pygame.display.set_mode(
        (gm_setting.screen_width, gm_setting.screen_height)
    )
    pygame.display.set_caption("Maze")
    # 获取迷宫数组
    maze = CreateMaze()
    # 生成迷宫
    maze.prim()
    # 实例化砖块,创建基本迷宫编组
    bricks = Group()
    gf.create_maze_group(screen, gm_setting, maze, bricks)
    # 创建四个方向键
    dir_button = DirectionButton(screen, gm_setting)
    # 实例化一条蛇
    snake = Snake(gm_setting)
    while True:
        # 主循环

        # 响应事件
        gf.check_events(screen, gm_setting, snake, maze)
        # 用操作后位置变换的蛇来更新迷宫矩阵
        gf.update_maze(gm_setting, maze, snake, bricks)
        # 更新屏幕
        gf.update_screen(screen, gm_setting, bricks, dir_button)


run_game()



