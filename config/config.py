"""
------------------------------------
@Time : 2019/7/13 20:03
@Auth : linux超
@File : config.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import os
import platform


"""
All dirs of the project
"""
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
DATA_DIR = os.path.join(ROOT_DIR, 'datas')
LOG_DIR = os.path.join(ROOT_DIR, 'log')
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
CASE_DIR = os.path.join(ROOT_DIR, 'cases')
PAGES_DIR = os.path.join(ROOT_DIR, 'pages')
LOCATOR_DIR = os.path.join(PAGES_DIR, 'locator')
ERROR_IMG_DIR = os.path.join(LOG_DIR, 'img')
"""
Test path of data and config file
"""
OBJECT_LIBRARY_PATH = os.path.join(CONFIG_DIR, 'locator.ini')
PROJECT_CONFIG_PATH = os.path.join(CONFIG_DIR, 'config.ini')
DATA_PATH = os.path.join(DATA_DIR, 'test_cases.xlsx')
LOCATOR_PATH = os.path.join(LOCATOR_DIR, 'locator.ini')
"""
Test environment info
"""
ENVIRONMENT = \
    "Windows Version:" + \
    platform.system() + \
    platform.version() + \
    platform.release() + \
    "Python Version" + \
    platform.python_build()[0]


if __name__ == '__main__':
    print(ERROR_IMG_DIR)
    pass
