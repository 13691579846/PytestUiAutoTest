"""
------------------------------------
@Time : 2019/7/23 20:22
@Auth : linux超
@File : conftest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.memberPage import MemberPage
from pages.loanPage import LoanPage
from datas.invest_datas import InvestData


# @pytest.fixture(scope='function')
# def login(driver):
#     login_page = LoginPage(driver)
#     login_page.open_url()
#     yield login_page
#     driver.delete_all_cookies()
#
#
# @pytest.fixture(scope='function')
# def invest(driver):
#     login_page = LoginPage(driver)
#     home_page = HomePage(driver)
#     loan_page = LoanPage(driver)
#     member_page = MemberPage(driver)
#     login_page.open_url()
#     login_page.login(InvestData.user_password['phone'],
#                      InvestData.user_password['pwd'])
#     home_page.click_knock_invest_button()
#     yield loan_page, member_page
#     driver.delete_all_cookies()
@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    loan_page = LoanPage(driver)
    member_page = MemberPage(driver)
    yield driver, login_page, home_page, loan_page, member_page


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    login_page.open_url()
    yield login_page
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def login(ini_pages):
    driver, login_page, home_page, loan_page, member_page = ini_pages
    login_page.open_url()
    login_page.login(InvestData.user_password['phone'],
                     InvestData.user_password['pwd'])
    yield login_page, home_page, loan_page, member_page
    driver.delete_all_cookies()
