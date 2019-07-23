"""
------------------------------------
@Time : 2019/7/13 20:31
@Auth : linux超
@File : create_dirs.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import os
from datetime import datetime, date


class CreateDir(object):

    def __init__(self):
        pass

    @staticmethod
    def get_current_time():
        """获取当前时间"""
        current_time = datetime.now().strftime(str(date.today()) + '-' + '%H-%M-%S')
        return current_time

    @staticmethod
    def get_current_date():
        """获取当前日期"""
        current_date = datetime.now().strftime(str(date.today()))
        return current_date

    @staticmethod
    def generate_filename(file_type):
        """日志与HTML报告文件名"""
        current_time = CreateDir.get_current_time()
        if 'HTML' == file_type.upper():
            current_time = CreateDir.get_current_time()
            filename = current_time + '.' + file_type
            return filename
        elif 'LOG' == file_type.upper():
            current_time = CreateDir.get_current_date()
            filename = current_time + 'testing' + '.' + file_type
            return filename
        else:
            return current_time + '.' + file_type

    @staticmethod
    def create_dir(path):
        """创建HTML报告与日志文件存放目录"""
        if not os.path.exists(path):
            os.makedirs(path)
        return path


if __name__ == '__main__':
    print(CreateDir.get_current_time())
    print(CreateDir.get_current_date())
