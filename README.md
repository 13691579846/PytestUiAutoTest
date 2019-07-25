# PytestUiAutoTest
Pytest框架实现的WebUi自动化测试

项目目录

    1.cases: 测试用例存放目录
    2.Cases->unit_test->unit_test.py: 所有用例均继承此文件中的自定义unittest
    3.common: 项目公共方法
    4.Config->config.py：存放项目所有目录的路径信息
    5.Datas：存放了测试用例所需的测试数据，两种形式：1.py文件保存2.excel文件保存
    6.pages: 根据page object 设计模式，本目录存放被测项目每个页面的元素操作及业务流程
    7.Pages->base ->base.py: 对selenium webdriver api部分功能的二次封装(所有页面的通用方法)
    8.Pages->locator->locator.ini: ui对象库，存放所有页面的操作元素定位表达式
    9.log：自动生成目录及生成项目执行日志
    10.log->img目录存放项目执行时的错误截图，包括用例执行失败时的截图
    11.report：自动生成目录及生成项目测试HTML报告(报告包含用例统计饼图及失败用例的截图)
ui对象库

    Locator.ini
    使用配置文件作为UI对象库，存放被测项目中的元素定位方式及定位表达式，方便项目维护，做到定位与代码分离，
    元素变动时只需修改对应定位方式及表达式即可，不用修改代码逻辑
测试数据

    *Datas.py
    项目使用两种存放与读取测试数据的方式
    1.使用普通py文件管理数据，读取方便，个人认为UI测试使用这种方式更加简单

项目设计

    1.整个代码编写方式采用python面向对象程序设计思想，重复的操作及代码使用类粉装，增强代码的结构，增加代码的复用性，及代码可维护性
    2.使用selenium 3自动化测试工具对测试页面的操作
    3.结合pytest单元测试框架编辑及组织测试用例
    4.使用pytest.parametrize参数化技术，实现同一个测试用例执行不同的测试数据，提高测试覆盖率，测试准确性，及减少部分重复测试代码
    5.采用ui对象库的思想，保存被测试项目所有的定位表达式，保证代码与定位分离，易维护，当项目页面变动时，只需要修改本文件指定的定位即可
    6.项目整个结构使用Page Object设计模式，把元素和业务逻辑按照页面抽象出来，分离成一定的对象，为每个页面的属性和操作构建模型，增加代码复用性，增强代码结构，当对数据或者元素修改时不会影响业务的流程及用例的执行
    7.使用pytest-html插件生成测试报告
    8.自动截取失败用例图片保存到测试报告中
    9.运用loggin模快，自动生成用例执行过程的日志
    10.使用pytest-rerunfailures插件，执行失败用例重跑，增加测试的准确性
环境准备

    1.Windows 10 
    2.Python 3.6
    3.pip install selenium
    4.pip install pytest
    4.pip install pytest-html插件
    5.pip install pytest-rerunfailures插件
    5.Firefox或Chrome浏览器(需包含对应驱动程序)
项目执行

    1.Cd PytestUiAutoTest
    2.Python run.py
项目扩展

    可以自定义修改pytest.ini 文件配置，及修改执行测试用例时的命令

测试结果
    整体测试报告展示
    ![Image](https://github.com/13691579846/PytestUiAutoTest/blob/master/img/%E6%8A%A5%E5%91%8A%E6%88%AA%E5%9B%BE1.png)
    ![Image](https://github.com/13691579846/PytestUiAutoTest/blob/master/img/%E6%8A%A5%E5%91%8A%E6%88%AA%E5%9B%BE2.png)
    失败用例截图展示
    ![Image](https://github.com/13691579846/PytestUiAutoTest/blob/master/img/%E9%94%99%E8%AF%AF%E7%94%A8%E4%BE%8B%E6%88%AA%E5%9B%BE.png)
    
用例进度

    1.登录功能测试用例已经完成
    2.投资功能测试用例已经完成
博客地址

    https://www.cnblogs.com/linuxchao/

