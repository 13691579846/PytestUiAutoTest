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
import os

from common.create_dirs import CreateDir
from config.config import REPORT_DIR


def main():
    report_dir = CreateDir.create_dir(REPORT_DIR)
    html_name = report_dir + '/' + CreateDir.generate_filename('html')
    args = r'pytest --reruns 1 --html=' + html_name + ' ' + '--self-contained-html'
    os.system(args)


if __name__ == '__main__':
    main()
