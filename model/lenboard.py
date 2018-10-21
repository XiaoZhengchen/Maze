import pygame


class LenBored:
    # 显示分数
    def __init__(self, screen, gm_setting, len):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting
        
        self.len = len
        
        self.msg = "len:" + str(self.len)
        self.width = 150
        self.height = 50
        self.font = pygame.font.SysFont('arial', 35)
        self.text_color = (255, 255, 255)
        self.bg_color = (135, 189, 94)
        # 创建对应的rect对象并确定位置
        self.len_rect = pygame.Rect(0, 0, self.width, self.height)
        self.len_rect.top = self.screen_rect.top + 125
        self.len_rect.right = self.screen_rect.right - 25
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.len_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.len_image_rect = self.len_image.get_rect()
        self.len_image_rect.center = self.len_rect.center
    
    def update_len(self, ilen):
        self.msg = "len:" + str(ilen)
        # 将字符串渲染为图像并使其在所需显示的矩形上居中
        self.len_image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.len_image_rect = self.len_image.get_rect()
        self.len_image_rect.center = self.len_rect.center
        
    def show_page(self):
        """展示等级模块"""
        self.screen.fill(self.bg_color, self.len_rect)
        self.screen.blit(self.len_image, self.len_image_rect)
