"""
------------------------------------
@Time : 2019/7/13 19:57
@Auth : linux超
@File : parse_config.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from configparser import (
    ConfigParser,
    NoOptionError,
    NoSectionError
)


class ParseConfig(ConfigParser):
    """解析配置文件"""
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(self.filename, encoding='utf-8')

    def get_option_value(self, section, option=None):
        """get value of section with option"""
        try:
            if option is None:
                value = dict(self[section])
                return value
            value = self.get(section, option)
            if '->' in value:
                value = tuple(value.split("->"))
            return value
        except (NoOptionError, NoSectionError) as e:
            raise e

    def __call__(self, *args, **kwargs):
        return self.get_option_value(*args, **kwargs)


if __name__ == '__main__':
    from config.config import LOCATOR_PATH
    config = ParseConfig(LOCATOR_PATH)
    print(config('LoginPage', 'phone_input'))
