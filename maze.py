import pygame
import time
import sys

from settings import Settings
from pygame.sprite import Group
import game_function as gf
from createmaze import CreateMaze
from directionButton import DirectionButton
from snake import Snake
from game_state import Gamestate
from welcomeActivity import WelcomeActivity
from startActivity import StartActivity
from endActivity import EndActivity


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
    # 设置响应长按键的时间间隔
    pygame.key.set_repeat(100, 100)
    # 实例化游戏状态
    state = Gamestate(gm_setting)
    # 实例化欢迎界面并显示欢迎界面2秒
    welcome_page = WelcomeActivity(screen, gm_setting)
    welcome_page.show_page()
    time.sleep(1)
    # 实例化开始界面
    start_page = StartActivity(screen, gm_setting)
    # 实例化结束页面
    end_page = EndActivity(screen, gm_setting)
    while True:
        # 主循环
        if state.gm_state == gm_setting.gm_run:
            # 进入游戏
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page)
            # 用操作后位置变换的蛇来更新迷宫矩阵
            gf.update_maze(gm_setting, maze, snake, bricks)
            # 检查蛇头是否已经成功逃出迷宫
            gf.check_snake_out(screen, gm_setting, maze, snake, state)

            # 更新屏幕
            gf.update_screen(screen, gm_setting, bricks, dir_button)
        elif state.gm_state == gm_setting.gm_wait:
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page)
            start_page.show_page()
        elif state.gm_state == gm_setting.gm_end:
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page)
            end_page.show_page()


run_game()



