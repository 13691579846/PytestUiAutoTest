"""
------------------------------------
@Time : 2019/7/16 9:56
@Auth : linux超
@File : login_datas.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class LoginData(object):
    """登录功能测试数据"""

    login_success_data = [
        (
            '18684720553',
            '***',
            '***'
        )
    ]

    login_format_data = [
        (
            '',
            'python',
            '请输入手机号'
        ),
        (
            '18684720553',
            '',
            '请输入密码'
        ),
        (
            '',
            '',
            '请输入手机号'
        ),
        (
            '12345678901',
            'python',
            '请输入正确的手机号'
        )
    ]

    login_account_error_data = [
        (
            '18684720551',
            'python',
            '帐号或密码错误!'
        ),
        (
            '18684720553',
            'pwd_error',
            '帐号或密码错误!'
        ),
        (
            '13691579846',
            '123456',
            '用户不存在!'
        )
    ]


if __name__ == '__main__':
    login = LoginData()
    print(login.login_account_error_data)
