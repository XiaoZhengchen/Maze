import pygame


class ScoreBored:
    # 显示分数
    def __init__(self, screen, gm_setting, state):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting

        self.score = state.gm_score

        self.msg = "score:" + str(self.score)
        self.width = 150
        self.height = 50
        self.font = pygame.font.SysFont('arial', 35)
        self.text_color = (255, 255, 255)
        self.bg_color = (164, 167, 204)
        # 创建对应的rect对象并确定位置
        self.score_rect = pygame.Rect(0, 0, self.width, self.height)
        self.score_rect.top = self.screen_rect.top + 25
        self.score_rect.right = self.screen_rect.right - 25
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.score_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.center = self.score_rect.center

    def update_score(self, state):
        """更新分数的图像"""
        self.score = (state.gm_end_time - state.gm_start_time).seconds

        self.msg = "score:" + str(self.score)
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.score_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.center = self.score_rect.center

    def show_page(self):
        """展示分数模块"""
        self.screen.fill(self.bg_color, self.score_rect)
        self.screen.blit(self.score_image, self.score_image_rect)

