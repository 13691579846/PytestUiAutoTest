"""
------------------------------------
@Time : 2019/7/13 20:01
@Auth : linux超
@File : test_login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest

from datas.login_datas import LoginData
from common.record_log import logger


class TestLogin(object):
    """登录测试用例"""
    logger = logger
    t_data = LoginData

    @pytest.mark.success
    @pytest.mark.parametrize('user, pwd, expect', t_data.login_success_data)
    def test_login_success(self, login, user, pwd, expect):
        """登录:登录成功"""
        login_page = login
        login_page.login(user, pwd)
        actual = login_page.get_login_success_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}-{}测试失败\n{}".format(
                self.test_login_success.__name__,
                user,
                pwd,
                e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}-{}测试通过".format(
                self.test_login_success.__name__,
                user,
                pwd))

    @pytest.mark.fail
    @pytest.mark.parametrize('user, pwd, expect', t_data.login_format_data)
    def test_login_format_error(self, login, user, pwd, expect):
        """登录:帐号或密码格式错误"""
        login_page = login
        login_page.login(user, pwd)
        actual = login_page.get_phone_pwd_format_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}-{}测试失败\n{}".format(
                self.test_login_format_error.__name__,
                user,
                pwd,
                e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}-{}测试通过".format(
                self.test_login_format_error.__name__,
                user,
                pwd))

    @pytest.mark.fail
    @pytest.mark.parametrize('user, pwd, expect', t_data.login_account_error_data)
    def test_login_account_error(self, login, user, pwd, expect):
        """登录:帐号或密码错误"""
        login_page = login
        login_page.login(user, pwd)
        actual = login_page.get_phone_pwd_error_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}-{}测试失败\n{}".format(
                self.test_login_account_error.__name__,
                user,
                pwd,
                e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}-{}测试通过".format(
                self.test_login_account_error.__name__,
                user,
                pwd))


if __name__ == '__main__':
    pytest.main()
