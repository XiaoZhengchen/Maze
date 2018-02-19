import pygame


class StartActivity():
    """显示开始界面"""
    def __init__(self, screen, gm_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting

        self.bg_color = (0, 0, 255)
        self.text_color = (255, 255, 255)

        # 绘制play按钮，store按钮，description按钮
        
        self.gm_play = "Play"
        self.gm_play_width = 440
        self.gm_play_height = 100
        self.gm_play_font = pygame.font.SysFont('arial', 80)
        # 创建对应的rect对象并确定位置
        self.gm_play_rect = pygame.Rect(0, 0, self.gm_play_width, self.gm_play_height)
        self.gm_play_rect.top = self.screen_rect.top + 100
        self.gm_play_rect.centerx = self.screen_rect.centerx
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.gm_play_image = self.gm_play_font.render(self.gm_play, True, self.text_color, self.bg_color)
        self.gm_play_image_rect = self.gm_play_image.get_rect()
        self.gm_play_image_rect.center = self.gm_play_rect.center

        self.gm_store = "Store"
        self.gm_store_width = 440
        self.gm_store_height = 100
        self.gm_store_font = pygame.font.SysFont('arial', 80)
        # 创建对应的rect对象并确定位置
        self.gm_store_rect = pygame.Rect(0, 0, self.gm_store_width, self.gm_store_height)
        self.gm_store_rect.top = self.screen_rect.top + 250
        self.gm_store_rect.centerx = self.screen_rect.centerx
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.gm_store_image = self.gm_store_font.render(self.gm_store, True, self.text_color, self.bg_color)
        self.gm_store_image_rect = self.gm_store_image.get_rect()
        self.gm_store_image_rect.center = self.gm_store_rect.center

        self.gm_description = "Description"
        self.gm_description_width = 440
        self.gm_description_height = 100
        self.gm_description_font = pygame.font.SysFont('arial', 80)
        # 创建对应的rect对象并确定位置
        self.gm_description_rect = pygame.Rect(0, 0, self.gm_description_width, self.gm_description_height)
        self.gm_description_rect.top = self.screen_rect.top + 400
        self.gm_description_rect.centerx = self.screen_rect.centerx
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.gm_description_image = self.gm_description_font.render(self.gm_description, True, self.text_color, self.bg_color)
        self.gm_description_image_rect = self.gm_description_image.get_rect()
        self.gm_description_image_rect.center = self.gm_description_rect.center

    def show_page(self):
        """展示页面"""
        self.screen.fill(self.gm_setting.bg_color)

        self.screen.fill(self.bg_color, self.gm_play_rect)
        self.screen.blit(self.gm_play_image, self.gm_play_image_rect)

        self.screen.fill(self.bg_color, self.gm_store_rect)
        self.screen.blit(self.gm_store_image, self.gm_store_image_rect)

        self.screen.fill(self.bg_color, self.gm_description_rect)
        self.screen.blit(self.gm_description_image, self.gm_description_image_rect)

        # 更新屏幕
        pygame.display.flip()