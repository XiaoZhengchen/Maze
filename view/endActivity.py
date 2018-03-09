import pygame


class EndActivity:
    """游戏结束时显示的页面"""
    def __init__(self, screen, gm_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting
        self.text_color = (255, 255, 255)

        # 需要绘制三个部分，通知信息，exit按钮，play按钮

        self.gm_end = "Game Over"
        self.gm_end_width = 200
        self.gm_end_height = 50
        self.end_bg_color = (0, 255, 0)
        self.gm_end_font = pygame.font.SysFont('arial', 40)
        # 创建对应的rect对象并确定位置
        self.gm_end_rect = pygame.Rect(0, 0, self.gm_end_width, self.gm_end_height)
        self.gm_end_rect.top = self.screen_rect.top + 250
        self.gm_end_rect.left = self.screen_rect.left + 200
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.gm_end_image = self.gm_end_font.render(self.gm_end, True, self.text_color, self.end_bg_color)
        self.gm_end_image_rect = self.gm_end_image.get_rect()
        self.gm_end_image_rect.center = self.gm_end_rect.center

        self.gm_play = "Play"
        self.gm_play_width = 100
        self.gm_play_height = 50
        self.play_bg_color = (0, 0, 255)
        self.gm_play_font = pygame.font.SysFont('arial', 40)
        # 创建对应的rect对象并确定位置
        self.gm_play_rect = pygame.Rect(0, 0, self.gm_play_width, self.gm_play_height)
        self.gm_play_rect.top = self.screen_rect.top + 300
        self.gm_play_rect.left = self.screen_rect.left + 300
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.gm_play_image = self.gm_play_font.render(self.gm_play, True, self.text_color, self.play_bg_color)
        self.gm_play_image_rect = self.gm_play_image.get_rect()
        self.gm_play_image_rect.center = self.gm_play_rect.center

        self.gm_exit = "Exit"
        self.gm_exit_width = 100
        self.gm_exit_height = 50
        self.exit_bg_color = (255, 0, 0)
        self.gm_exit_font = pygame.font.SysFont('arial', 40)
        # 创建对应的rect对象并确定位置
        self.gm_exit_rect = pygame.Rect(0, 0, self.gm_exit_width, self.gm_exit_height)
        self.gm_exit_rect.top = self.screen_rect.top + 300
        self.gm_exit_rect.left = self.screen_rect.left + 200
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.gm_exit_image = self.gm_exit_font.render(self.gm_exit, True, self.text_color, self.exit_bg_color)
        self.gm_exit_image_rect = self.gm_exit_image.get_rect()
        self.gm_exit_image_rect.center = self.gm_exit_rect.center

    def show_page(self):
        """展示页面"""
        # self.screen.fill(self.gm_setting.bg_color)
        self.screen.fill(self.play_bg_color, self.gm_play_rect)
        self.screen.blit(self.gm_play_image, self.gm_play_image_rect)

        self.screen.fill(self.end_bg_color, self.gm_end_rect)
        self.screen.blit(self.gm_end_image, self.gm_end_image_rect)

        self.screen.fill(self.exit_bg_color, self.gm_exit_rect)
        self.screen.blit(self.gm_exit_image, self.gm_exit_image_rect)
        # 更新屏幕
        pygame.display.flip()