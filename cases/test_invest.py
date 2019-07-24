"""
------------------------------------
@Time : 2019/7/13 20:01
@Auth : linux超
@File : test_invest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import inspect
import pytest

from common.record_log import logger
from datas.invest_datas import InvestData
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.loanPage import LoanPage
from pages.memberPage import MemberPage


class TestInvest(object):
    """投资用例"""
    logger = logger
    t_data = InvestData

    @pytest.fixture(scope='function')
    def setup_teardown_function(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        loan_page = LoanPage(driver)
        member_page = MemberPage(driver)
        login_page.open_url()
        login_page.login(self.t_data.user_password['phone'],
                         self.t_data.user_password['pwd'])
        home_page.click_knock_invest_button()
        yield loan_page, member_page
        driver.delete_all_cookies()

    @pytest.mark.parametrize('amount, expect', t_data.invest_amount_singular)
    def test_amount_singular(self, setup_teardown_function, amount, expect):
        loan_page = setup_teardown_function[0]
        loan_page.invest(amount)
        actual = loan_page.get_error_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            loan_page.save_screen_shot('invest_fail')
            raise e
        self.logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    @pytest.mark.parametrize('amount, expect', t_data.invest_amount_error)
    def test_amount_error(self, setup_teardown_function, amount, expect):
        loan_page = setup_teardown_function[0]
        loan_page.invest(amount)
        actual = loan_page.get_error_alert
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            loan_page.save_screen_shot('invest_fail')
            raise e
        self.logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    @pytest.mark.parametrize('amount, expect', t_data.invest_success)
    def test_invest_success(self, setup_teardown_function, amount, expect):
        loan_page, member_page = setup_teardown_function
        account_remain_amount = int(float(loan_page.get_account_remain_amount) * 100)
        loan_page.invest(amount)
        result = loan_page.get_invest_success_info
        assert expect in result, '断言失败'
        loan_page.click_check_detail()
        actual = int(float(member_page.get_success_text[:-1]) * 100)
        expected = account_remain_amount - int(amount * 100)
        try:
            assert expected == actual, '断言失败'
        except AssertionError as e:
            self.logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            loan_page.save_screen_shot('invest_fail')
            raise e
        self.logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))


if __name__ == '__main__':
    pytest.main()
