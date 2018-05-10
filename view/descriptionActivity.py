import pygame


class DescriptionActivity():
    
    def __init__(self, screen, gm_setting):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gm_setting = gm_setting

        self.bg_color_1 = (121, 169, 182)
        self.bg_color_2 = (192, 195, 35)
        self.text_color = (255, 255, 255)
        # 设置每一个选项的长宽,字体大小及之间的空隙
        self.width = 600
        self.height = 50
        self.font = pygame.font.SysFont('arial', 20)
        Name = "Description"
        rule0 = "1. Each time you enter the game,you will generate a different maze."
        rule1 = "2. When unable to continue the game, click ESC key to exit."
        rule2 = "3. You can view the top 20 of your history score at the rank interface."
        rule3 = "4. Click ESC to exit the interface."
        self.gm_description = [Name, rule0, rule1, rule2, rule3]
       
    def show_page(self):
        """展示页面"""
        num = 0
        self.screen.fill(self.gm_setting.bg_color)
        for rule in self.gm_description:
            # 创建对应的rect对象并确定位置
            if num % 2 == 1:
                bg_color = self.bg_color_1
            else:
                bg_color = self.bg_color_2
            if num == 0:
                bg_color = (95, 135, 222)
            msg = str(rule)
            gm_description_rect = pygame.Rect(0, 0, self.width, self.height)
            gm_description_rect.top = self.screen_rect.top + 50 * num
            gm_description_rect.left = self.screen_rect.left + 100
            # 将字符串渲染为图像并使其在所需显示的矩形上居中
            gm_description_image = self.font.render(msg, True, self.text_color, bg_color)
            gm_description_image_rect = gm_description_image.get_rect()
            gm_description_image_rect.center = gm_description_rect.center
            
            self.screen.fill(bg_color, gm_description_rect)
            self.screen.blit(gm_description_image, gm_description_image_rect)
            num += 1
        # 更新屏幕
        pygame.display.flip()
        