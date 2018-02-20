import pygame
import pygame.font


class WelcomeActivity:
    """绘制欢迎界面的类"""
    def __init__(self, screen, gm_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting

        self.bg_color = (0, 0, 255)
        self.text_color = (255, 255, 255)

        # 需要展示的两个信息
        self.gm_name = "Snake in Maze"
        self.gm_name_width = 440
        self.gm_name_height = 100
        self.gm_name_font = pygame.font.SysFont('arial', 80)
        # 创建对应的rect对象并使之居中
        self.gm_name_rect = pygame.Rect(0, 0, self.gm_name_width, self.gm_name_height)
        self.gm_name_rect.center = self.screen_rect.center
        # 将字符串渲染为图像并使其在所需显示的图像上居中
        self.gm_name_image = self.gm_name_font.render(self.gm_name, True, self.text_color, self.bg_color)
        self.gm_name_image_rect = self.gm_name_image.get_rect()
        self.gm_name_image_rect.center = self.gm_name_rect.center

        self.gm_auth = "Created by xzc"
        self.gm_auth_width = 130
        self.gm_auth_height = 30
        self.gm_auth_font = pygame.font.SysFont('arial', 25)
        # 创建对应的rect对象并使之居中
        self.gm_auth_rect = pygame.Rect(0, 0, self.gm_auth_width, self.gm_auth_height)
        self.gm_auth_rect.right = self.screen_rect.right - 30
        self.gm_auth_rect.bottom = self.screen_rect.bottom - 30
        # 将字符串渲染为图像并使其在所需显示的图像上居中
        self.gm_auth_image = self.gm_auth_font.render(self.gm_auth, True, self.text_color, self.bg_color)
        self.gm_auth_image_rect = self.gm_auth_image.get_rect()
        self.gm_auth_image_rect.center = self.gm_auth_rect.center

    def show_page(self):
        """展示页面"""
        self.screen.fill(self.bg_color, self.gm_name_rect)
        self.screen.blit(self.gm_name_image, self.gm_name_image_rect)

        self.screen.fill(self.bg_color, self.gm_auth_rect)
        self.screen.blit(self.gm_auth_image, self.gm_auth_image_rect)
        # 更新屏幕
        pygame.display.flip()

