import pygame


class DirectionButton:

    def __init__(self, screen, gm_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = gm_setting

        # 获取四个按钮的图片,并将图片大小重置为30*30,设置位置
        self.leftButton = pygame.image.load("../images/left.png")
        self.leftButton = pygame.transform.scale(self.leftButton, (30, 30))
        self.leftRect = self.leftButton.get_rect()
        self.leftRect.right = self.screen_rect.right - 130
        self.leftRect.bottom = self.screen_rect.bottom - 30

        self.upButton = pygame.image.load("../images/up.png")
        self.upButton = pygame.transform.scale(self.upButton, (30, 30))
        self.upRect = self.upButton.get_rect()
        self.upRect.right = self.screen_rect.right - 85
        self.upRect.bottom = self.screen_rect.bottom - 75

        self.rightButton = pygame.image.load("../images/right.png")
        self.rightButton = pygame.transform.scale(self.rightButton, (30, 30))
        self.rightRect = self.rightButton.get_rect()
        self.rightRect.right = self.screen_rect.right - 40
        self.rightRect.bottom = self.screen_rect.bottom - 30

        self.downButton = pygame.image.load("../images/down.png")
        self.downButton = pygame.transform.scale(self.downButton, (30, 30))
        self.downRect = self.downButton.get_rect()
        self.downRect.right = self.screen_rect.right - 85
        self.downRect.bottom = self.screen_rect.bottom - 30

    def blitme(self):
        self.screen.blit(self.rightButton, self.rightRect)
        self.screen.blit(self.upButton, self.upRect)
        self.screen.blit(self.downButton, self.downRect)
        self.screen.blit(self.leftButton, self.leftRect)

