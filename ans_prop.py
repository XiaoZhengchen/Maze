from prop import Prop


class AnsProp(Prop):
    """获得答案的道具"""
    def __init__(self, screen, gm_setting, state):
        self.state = state
        self.msg = "get_ans"
        self.top = 400
        self.left = 600 + 30
        self.color = (145, 148, 189)
        super(AnsProp, self).__init__(screen, gm_setting, state, self.msg, self.top, self.left, self.color)

    def effect(self):
        """重载每个函数的效果"""
        if not self.state.show_ans:
            self.state.show_ans = True

    def show(self):
        super().show()



