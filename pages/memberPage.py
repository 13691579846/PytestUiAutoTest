"""
------------------------------------
@Time : 2019/7/19 21:36
@Auth : linux超
@File : memberPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
# TODO: perfecting the user page class
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH


class MemberPage(Base):

    locator = ParseConfig(LOCATOR_PATH)

    account_remain_amount = locator('MemberPage', 'account_remain_amount')

    @property
    def get_success_text(self):
        """获取投资成功后账户剩余金额"""
        return self.get_element_text(*self.account_remain_amount)


if __name__ == '__main__':
    pass
