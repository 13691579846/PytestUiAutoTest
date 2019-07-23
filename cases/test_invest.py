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

from datas.invest_datas import InvestData


class TestInvest(object):
    """投资用例"""
    t_data = InvestData

    def setUp(self):
        self.login_page.open_url()
        self.login_page.login(self.t_data.user_password['phone'],
                              self.t_data.user_password['pwd'])
        self.home_page.click_knock_invest_button()

    def test_amount_singular(self, value):
        self.loan_page.invest(value['amount'])
        actual = self.loan_page.get_error_info
        try:
            self.assertEqual(value['expect'], actual)
        except AssertionError as e:
            self.logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            self.loan_page.save_screen_shot('invest_fail')
            raise e
        self.logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    def test_amount_error(self, value):
        self.loan_page.invest(value['amount'])
        actual = self.loan_page.get_error_alert
        try:
            self.assertEqual(value['expect'], actual)
        except AssertionError as e:
            self.logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            self.loan_page.save_screen_shot('invest_fail')
            raise e
        self.logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    def test_invest_success(self, value):
        account_remain_amount = int(float(self.loan_page.get_account_remain_amount) * 100)
        self.loan_page.invest(value['amount'])
        result = self.loan_page.get_invest_success_info
        self.assertIn(value['expect'], result)
        self.loan_page.click_check_detail()
        actual = int(float(self.member_page.get_success_text[:-1]) * 100)
        expect = account_remain_amount - int(value['amount'] * 100)
        try:
            self.assertEqual(expect, actual)
        except AssertionError as e:
            self.logger.error("投资用例{}测试失败{}".format(inspect.stack()[0][1], e))
            self.loan_page.save_screen_shot('invest_fail')
            raise e
        self.logger.info("投资用例{}测试通过".format(inspect.stack()[0][1]))

    def tearDown(self):
        self.driver.delete_all_cookies()


if __name__ == '__main__':
    import unittest
    unittest.main()
