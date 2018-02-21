import pygame


class RankList:
    """显示前十名的得分排行榜"""
    def __init__(self, screen, gm_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting

        self.rank = []
        for i in range(10):
            self.rank.append(0)
        self.text_color = (191, 54, 54)
        self.bg_color_1 = (121, 169, 182)
        self.bg_color_2 = (192, 195, 35)
        self.font = pygame.font.SysFont('arial', 35)

        self.width = 200
        self.height = 50

    def update_rank(self, score):
        self.rank.append(score)
        self.rank.sort(reverse=True)

    def show_page(self):
        num = -1
        self.screen.fill(self.gm_setting.bg_color)
        print(self.rank)
        for score in self.rank:
            num += 1
            if num == 10:
                break
            if num % 2 == 1:
                bg_color = self.bg_color_1
            else:
                bg_color = self.bg_color_2
            msg = "Rank " + str(num) + ":  " + str(score)
            score_rect = pygame.Rect(0, 0, self.width, self.height)
            score_rect.top = self.screen_rect.top + 50 * (num + 1)
            score_rect.left = self.screen_rect.left + 300
            # 将字符串渲染为图像并使其在所需显示的矩形上居中
            score_image = self.font.render(msg, True, self.text_color, bg_color)
            score_image_rect = score_image.get_rect()
            score_image_rect.center = score_rect.center

            self.screen.fill(bg_color, score_rect)
            self.screen.blit(score_image, score_image_rect)

        pygame.display.flip()





