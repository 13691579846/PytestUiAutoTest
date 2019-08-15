"""
------------------------------------
@Time : 2019/7/17 23:02
@Auth : linux超
@File : invest_datas.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""


class InvestData(object):
    """投资功能测试数据"""

    # 正确的用户名和密码
    user_password = {
            'phone': '18684720553',
            'pwd': '****'
        }

    # 测试金额非100倍数
    invest_amount_singular = [
        (
            '1',
            '请输入10的整数倍'
        ),
        (
            '10.1',
            '请输入10的整数倍'
        ),
        (
            '-1',
            '请输入10的整数倍'
        ),
        (
            '101',
            '请输入10的整数倍'
        ),
    ]

    # 测试金额为0，小于100整数，及大于标的剩余金额
    invest_amount_error = [
        (
            '0',
            '请正确填写投标金额'
        ),
        (
            '10',
            '投标金额必须为100的倍数'
        ),
        (
            ' ',
            '请正确填写投标金额'
        )
    ]

    invest_success = [
        (
            '100',
            '投标成功'
        )
    ]
