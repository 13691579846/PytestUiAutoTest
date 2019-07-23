"""
------------------------------------
@Time : 2019/7/17 22:14
@Auth : linux超
@File : homePage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH


class HomePage(Base):
    """首页"""
    locator = ParseConfig(LOCATOR_PATH)
    knock_invest_button = locator('HomePage', 'knock_invest_button')

    @property
    def invest_button(self):
        """抢投标按钮"""
        return self.find_elements(*self.knock_invest_button)[0]

    def click_knock_invest_button(self):
        """点击抢投标按钮"""
        self.execute_window_scroll('0', '300')
        self.invest_button.click()


if __name__ == '__main__':
    pass
