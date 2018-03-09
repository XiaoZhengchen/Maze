import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    """
    组成迷宫的砖块的设置
    """
    def __init__(self, gm_setting, screen):
        super(Brick, self).__init__()
        self.screen = screen
        # 设置砖块的宽高颜色
        self.height = gm_setting.brick_height
        self.width = gm_setting.brick_width
        self.color = gm_setting.brick_color

        # 设置砖块的矩形位置
        self.rect = pygame.Rect(0, 0, self.height, self.width)
        self.rect.right = 0
        self.rect.bottom = self.screen.get_rect().bottom

        # 砖块在迷宫中的位置
        self.pos = (0, 0)

    def __str__(self):
        print(self.color, self.rect.right, self.rect.bottom)

    def draw_brick(self, gm_setting):
        # 画出每一个单元格
        i = self.pos[0]
        j = self.pos[1]
        self.rect.top = self.width * (i - gm_setting.show_top)
        self.rect.left = self.width * (j - gm_setting.show_left)
        pygame.draw.rect(self.screen, self.color, self.rect)
