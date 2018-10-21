import pygame


class LevelBored:
    # 显示分数
    def __init__(self, screen, gm_setting, level):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting

        self.level = level
        
        self.msg = "level:" + str(int(self.level / 10))
        self.width = 150
        self.height = 50
        self.font = pygame.font.SysFont('arial', 35)
        self.text_color = (255, 255, 255)
        self.bg_color = (103, 189, 170)
        # 创建对应的rect对象并确定位置
        self.level_rect = pygame.Rect(0, 0, self.width, self.height)
        self.level_rect.top = self.screen_rect.top + 75
        self.level_rect.right = self.screen_rect.right - 25
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.level_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.center = self.level_rect.center

    def update_level(self, ilevel):
        self.msg = "level:" + str(int(ilevel / 10))
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.level_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.center = self.level_rect.center

    def show_page(self):
        """展示等级模块"""
        self.screen.fill(self.bg_color, self.level_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        # pygame.display.flip()
