"""
------------------------------------
@Time : 2019/7/14 19:51
@Auth : linux超
@File : record_log.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import logging
from logging.handlers import RotatingFileHandler

from common.create_dirs import CreateDir
from config.config import LOG_DIR


class Log(object):
    """记录日志"""
    def __init__(self, name=__name__, path='log.log', level='DEBUG'):
        self._name = name
        self._path = path
        self._level = level
        self._logger = logging.getLogger(self._name)
        self._logger.setLevel(self._level)

    def _init_handler(self):
        file_handler = RotatingFileHandler(self._path,
                                           maxBytes=10 * 1024 * 1024,
                                           backupCount=3,
                                           encoding='utf-8')
        return file_handler

    def _set_handler(self, file_handler, level='DEBUG'):
        file_handler.setLevel(level)
        self._logger.addHandler(file_handler)

    @staticmethod
    def _set_formatter(file_handler):
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        file_handler.setFormatter(formatter)

    @staticmethod
    def _close_handler(file_handler):
        file_handler.close()

    @property
    def logger(self):
        file_handler = self._init_handler()
        self._set_handler(file_handler)
        self._set_formatter(file_handler)
        self._close_handler(file_handler)
        return self._logger


log_name = CreateDir.generate_filename('log')
log_dir = CreateDir.create_dir(LOG_DIR)
log = Log(__name__, LOG_DIR + '/' + log_name)
logger = log.logger


if __name__ == '__main__':
        pass
