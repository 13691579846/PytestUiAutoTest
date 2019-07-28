"""
------------------------------------
@Time : 2019/7/23 20:18
@Auth : linux超
@File : run.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import pytest

from common.create_dirs import CreateDir
from config.config import REPORT_DIR


def main():
    CreateDir.create_dir(REPORT_DIR)
    html_name = CreateDir.generate_filename('html')
    args = ['--reruns', '1', '--html=' + './report/' + html_name]
    pytest.main(args)


if __name__ == '__main__':
    main()
