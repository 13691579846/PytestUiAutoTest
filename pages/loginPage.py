"""
------------------------------------
@Time : 2019/7/13 19:55
@Auth : linux超
@File : loginPage.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from pages.base.base import Base
from common.parse_config import ParseConfig
from config.config import LOCATOR_PATH


class LoginPage(Base):

    locator = ParseConfig(LOCATOR_PATH)

    url = locator('TestUrl', 'url')
    phone_input = locator('LoginPage', 'phone_input')  # 用户名输入框
    password_input = locator('LoginPage', 'password_input')  # 密码输入框
    login_button = locator('LoginPage', 'login_button')  # 登录按钮

    login_success_info = locator('LoginPage', 'login_success_info')
    format_error_info = locator('LoginPage', 'format_error_info')  # 帐号或密码格式错误
    phone_password_error = locator('LoginPage', 'phone_password_error')  # 帐号或密码错误

    def login(self, phone: str, password: str):
        self.logger.info("开始登录")
        self.input_user(phone)
        self.input_password(password)
        self.click_login()

    def open_url(self):
        self.open(self.url)

    def input_user(self, phone: str):
        self.logger.info("输入用户名:{}".format(phone))
        self.send_keys(*self.phone_input, value=phone)

    def input_password(self, password: str):
        self.logger.info("输入密码:{}".format(password))
        self.send_keys(*self.password_input, value=password)

    def click_login(self):
        self.logger.info("点击登录按钮")
        self.click(*self.login_button)

    @property
    def get_phone_pwd_format_info(self):
        value = self.get_element_text(*self.format_error_info)
        self.logger.info("获取登录失败断言信息:{}".format(value))
        return value

    @property
    def get_phone_pwd_error_info(self):
        value = self.get_element_text(*self.phone_password_error)
        self.logger.info("获取登陆失败断言信息:{}".format(value))
        return value

    @property
    def get_login_success_info(self):
        value = self.get_element_text(*self.login_success_info)
        self.logger.info("获取登录成功断言信息:{}".format(value))
        return value


if __name__ == '__main__':
    pass
