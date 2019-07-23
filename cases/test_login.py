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
import inspect
import pytest

from datas.login_datas import LoginData
from pages.loginPage import LoginPage
from common.record_log import logger


class TestLogin(object):
    """登录测试用例"""
    t_data = LoginData  # 可以从py文件获取测试数据

    @pytest.fixture(scope='function')
    def setup_teardown_function(self, driver):
        login_page = LoginPage(driver)
        yield login_page
        driver.delete_all_cookies()

    @pytest.mark.parametrize('user, pwd, expect', t_data.login_success_data)
    def test_login_success(self, setup_teardown_function, user, pwd, expect):
        login_page = setup_teardown_function
        login_page.open_url()
        login_page.login(user, pwd)
        actual = login_page.get_login_success_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))

    @pytest.mark.parametrize('user, pwd, expect', t_data.login_format_data)
    def test_login_format_error(self, setup_teardown_function, user, pwd, expect):
        login_page = setup_teardown_function
        login_page.open_url()
        login_page.login(user, pwd)
        actual = login_page.get_phone_pwd_format_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))

    @pytest.mark.parametrize('user, pwd, expect', t_data.login_account_error_data)
    def test_login_account_error(self, setup_teardown_function, user, pwd, expect):
        login_page = setup_teardown_function
        login_page.open_url()
        login_page.login(user, pwd)
        actual = login_page.get_phone_pwd_error_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            logger.error("测试{}失败:{}".format(inspect.stack()[0][3], e))
            login_page.save_screen_shot('login_fail')
            raise e
        else:
            logger.info("测试{}通过".format(inspect.stack()[0][3]))


if __name__ == '__main__':
    pytest.main()
