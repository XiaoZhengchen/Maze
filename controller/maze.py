import datetime
import sys

import pygame
from model.directionButton import DirectionButton
from controller.game_state import Gamestate
from pygame.sprite import Group
from view.startActivity import StartActivity
from view.welcomeActivity import WelcomeActivity

from controller import game_function as gf
from model.ans_prop import AnsProp
from model.createmaze import CreateMaze
from model.fruits import Fruits
from model.passageway import PassageWay
from model.ranklist import RankList
from model.scorebored import ScoreBored
from model.levelboard import LevelBored
from model.lenboard import LenBored
from model.snake import Snake
from controller.settings import Settings
from view.endActivity import EndActivity
from view.descriptionActivity import DescriptionActivity


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
    # 生成迷宫的答案
    ans = PassageWay(gm_setting, maze.m)
    ans.get_path()
    ans.get_level()
    # print("ans.level", ans.level)
    # 实例化砖块,创建基本迷宫编组
    bricks = Group()
    gf.create_maze_group(screen, gm_setting, maze, bricks)
    # 创建四个方向键
    dir_button = DirectionButton(screen, gm_setting)
    # 实例化一条蛇
    snake = Snake(gm_setting)
    # 实例化果实障碍
    fruits = Fruits(maze, ans.path)
    # print(fruits.pos)
    # 设置响应长按键的时间间隔
    pygame.key.set_repeat(100, 100)
    # 实例化游戏状态
    state = Gamestate(gm_setting)
    # 实例化分数
    score = ScoreBored(screen, gm_setting, state)
    # 实例化等级面板
    level = LevelBored(screen, gm_setting, ans.level)
    # 实例化长度面板
    lenBoard = LenBored(screen, gm_setting, len(snake.coordinate))
    # 实例化排行榜
    ranklist = RankList(screen, gm_setting)
    # 实例化各种道具
    ans_prop = AnsProp(screen, gm_setting, state)

    # 实例化开始界面
    start_page = StartActivity(screen, gm_setting)
    # 实例化结束页面
    end_page = EndActivity(screen, gm_setting)
    # 实例化说明界面
    description_page = DescriptionActivity(screen, gm_setting)

    # 读取存档
    gf.init(ranklist)
    while True:
        # 主循环
        if state.gm_state == gm_setting.gm_welcome:
            # 实例化欢迎界面并显示欢迎界面1秒
            welcome_page = WelcomeActivity(screen, gm_setting)
            welcome_page.show_page()
            for event in pygame.event.get():
                if event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                    state.gm_state = gm_setting.gm_wait
                if event.type == pygame.QUIT:
                    sys.exit()
        elif state.gm_state == gm_setting.gm_run:
            # 进入游戏获取当前时间
            state.gm_end_time = datetime.datetime.now()
            ans.level = 0
            ans.get_level()
            level.update_level(ans.level)
            # 更新分数
            score.update_score(state)
            # 更新长度
            lenBoard.update_len(len(snake.coordinate))
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page, ranklist, fruits, dir_button, ans_prop)
            # 使蛇的尾部每隔10秒就自增一格
            snake.tail_update(score.score, maze.m)
            # 用操作后位置变换的蛇、通路、障碍果实来更新迷宫矩阵
            gf.update_maze(gm_setting, maze, snake, bricks, state, fruits, ans.path)
            # 检查蛇头是否已经成功逃出迷宫,若成功逃脱则更新排行榜
            gf.check_snake_out(screen, gm_setting, maze, snake, state, ranklist, score)

            # 更新屏幕
            gf.update_screen(screen, gm_setting, bricks, dir_button, score, ans_prop, level, lenBoard)
        elif state.gm_state == gm_setting.gm_wait:
            # 生成迷宫
            maze.prim()
            # 生成迷宫的答案
            ans = PassageWay(gm_setting, maze.m)
            ans.get_path()
            ans.get_level()
            fruits = Fruits(maze, ans.path)
            snake.Flag_Score = []
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page, ranklist, fruits)
            start_page.show_page()
        elif state.gm_state == gm_setting.gm_end:
            snake.Flag_Score = []
            
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page, ranklist, fruits)
            end_page.show_page()
        elif state.gm_state == gm_setting.gm_rank:
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page, ranklist)
            ranklist.show_page()
        elif state.gm_state == gm_setting.gm_descr:
            # 响应事件
            gf.check_events(screen, gm_setting, snake, maze, state, start_page, end_page, ranklist, fruits)
            description_page.show_page()

run_game()



