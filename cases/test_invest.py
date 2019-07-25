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
import pytest

from common.record_log import logger
from datas.invest_datas import InvestData


class TestInvest(object):
    """投资用例"""
    logger = logger
    t_data = InvestData

    @pytest.mark.fail
    @pytest.mark.parametrize('amount, expect', t_data.invest_amount_singular)
    def test_amount_singular(self, invest, amount, expect):
        """投资:投资金额异常"""
        loan_page = invest[0]
        loan_page.invest(amount)
        actual = loan_page.get_error_info
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}测试失败\n{}".format(
                self.test_amount_singular.__name__,
                amount,
                e))
            loan_page.save_screen_shot('invest_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}测试通过".format(
                self.test_amount_singular.__name__,
                amount))

    @pytest.mark.fail
    @pytest.mark.parametrize('amount, expect', t_data.invest_amount_error)
    def test_amount_error(self, invest, amount, expect):
        """投资:投资金额异常"""
        loan_page = invest[0]
        loan_page.invest(amount)
        actual = loan_page.get_error_alert
        try:
            assert expect == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}测试失败\n{}".format(
                self.test_amount_singular.__name__,
                amount,
                e))
            loan_page.save_screen_shot('invest_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}测试通过".format(
                self.test_amount_error.__name__,
                amount))

    @pytest.mark.success
    @pytest.mark.parametrize('amount, expect', t_data.invest_success)
    def test_invest_success(self, invest, amount, expect):
        """投资:投资成功"""
        loan_page, member_page = invest
        account_remain_amount = int(float(loan_page.get_account_remain_amount) * 100)
        loan_page.invest(amount)
        result = loan_page.get_invest_success_info
        assert expect in result, '断言失败'
        loan_page.click_check_detail()
        actual = int(float(member_page.get_success_text[:-1]) * 100)
        expected = account_remain_amount - int(int(amount) * 100)
        try:
            assert expected == actual, '断言失败'
        except AssertionError as e:
            self.logger.info("测试用例{}-{}测试失败\n{}".format(
                self.test_amount_singular.__name__,
                amount,
                e))
            loan_page.save_screen_shot('invest_fail')
            raise e
        else:
            self.logger.info("测试用例{}-{}测试通过".format(
                self.test_invest_success.__name__,
                amount))


if __name__ == '__main__':
    pytest.main()
