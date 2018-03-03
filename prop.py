import pygame


class Prop:
    """
    道具类
    msg:道具名称
    top,left:确定道具的位置
    """
    def __init__(self, screen, gm_setting, state, msg, top, left, color):
        self.screen = screen
        self.screen_rect = screen
        self.gm_setting = gm_setting
        self.gm_state = state.gm_state
        self.msg = msg
        self.color = color
        self.font = pygame.font.SysFont('arial', gm_setting.brick_height - 5)

        self.text_color = (255, 255, 255)
        self.bg_color = (164, 167, 204)
        # 设置道具的位置
        self.prop_rect = pygame.Rect(0, 0, gm_setting.brick_width, gm_setting.brick_height)
        self.prop_rect.top = top
        self.prop_rect.left = left
        # 将道具名msg转化为图像并将之放在道具后
        self.image = self.font.render(self.msg, True, self.text_color, self.bg_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.top = self.prop_rect.top
        self.image_rect.left = self.prop_rect.right + 20

    def effect(self):
        """道具相应的效果"""
        pass

    def show(self):
        self.screen.fill(self.color, self.prop_rect)
        self.screen.blit(self.image, self.image_rect)










