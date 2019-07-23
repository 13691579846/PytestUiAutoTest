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
from selenium import webdriver
import pytest


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
