"""
------------------------------------
@Time : 2019/7/13 20:54
@Auth : linux超
@File : base.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (NoSuchElementException,
                                        TimeoutException,
                                        NoAlertPresentException,
                                        InvalidArgumentException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

from common.record_log import logger
from common.create_dirs import CreateDir
from config.config import ERROR_IMG_DIR


class Base(object):

    c_dir = CreateDir
    logger = logger

    def __init__(self, driver: webdriver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.base_url = 'http://120.78.128.25:8765'

    def _open(self, url=None):
        try:
            url = url or self.base_url
            self.driver.get(url)
        except InvalidArgumentException as e:
            self.logger.error('加载测试地址{}失败:{}'.format(url, e))
            self.save_screen_shot("url")
            raise e
        else:
            self.logger.info('加载测试地址:{}'.format(url))

    def open(self, url=None):
        self._open(url)

    def find_element(self, by: str, location: str) -> WebElement:
        """
        find element by location
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: WebElement
        :Usage:
            locator = ("xpath", //*[@id="location"])
            element = driver.find_element(*locator)
        """
        by = by.lower()
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(lambda driver: driver.find_element(by, location))
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error('通过定位表达式{}定位元素失败:{}'.format(location, e))
            self.save_screen_shot("find_element")
            raise e
        else:
            return element

    def find_elements(self, by: str, location: str) -> list:
        """
        find elements with location
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: list of WebElement
        :Usage:
            locator = ("xpath", //*[@id="location"])
            elements = driver.find_elements(*locator)
        """
        by = by.lower()
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            elements = wait.until(lambda driver: driver.find_elements(by, location))
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error('通过定位表达式{}定位一组元素失败:{}'.format(location, e))
            self.save_screen_shot("find_elements")
            raise e
        else:
            return elements

    def is_element_exist(self, by: str, location: str) -> bool:
        """
        return True if element is exist else False
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: bool
        """
        self.timeout = 10
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(ec.visibility_of_element_located((by, location)))
        except (NoSuchElementException, TimeoutException):
            return False
        return True

    @property
    def is_alert_switch_to_it(self):
        """
        switch to alert if alert is present
        :return: alert object if alert is present else False
        """
        self.timeout = 10
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            alert = wait.until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            self.save_screen_shot("alert")
            return False
        return alert

    def is_clickable(self, by: str, location: str):
        """
        return element if element is clickable else False
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return:
        """
        by = by.lower()
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(ec.element_to_be_clickable((by, location)))
        except (TimeoutException, NoSuchElementException):
            return False
        return element

    @property
    def get_alert_text(self) -> str:
        """
        get test of alert
        :return: text of alert
        """
        alert = self.is_alert_switch_to_it
        if alert:
            return alert.text
        else:
            self.logger.error("获取alert文本失败")
            raise NoAlertPresentException("没有alert抛出")

    def switch_to_iframe(self, by: str, location: str) -> bool:
        """
        switch to iframe
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: bool
        """
        by = by.lower()
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until(ec.frame_to_be_available_and_switch_to_it((by, location)))
        except (TimeoutException, NoSuchElementException):
            self.logger.error("切换iframe{}失败".format(location))
            self.save_screen_shot("iframe")
            return False
        else:
            return True

    @property
    def switch_default_iframe(self):
        """切换到默认的iframe"""
        return self.driver.switch_to.default_content()

    def click(self, by: str, location: str):
        """
        click element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: None
        """
        element = self.is_clickable(by, location)
        if element:
            element.click()
        else:
            self.logger.error('元素{}不可点击'.format(location))

    def send_keys(self, by: str, location: str, value) -> None:
        """
        input the value to input box of element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :param value: 输入的数据
        :return: None
        """
        try:
            element = self.find_element(by, location)
            element.clear()
            element.send_keys(value)
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error("输入框:{}, 输入数据{}失败:{}".format(location, value, e))
            self.save_screen_shot("send_keys")
            raise e

    def get_element_text(self, by: str, location: str) -> (str, None):
        """
        get text of element
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: str or bool
        """
        by = by.lower()
        element = self.find_element(by, location)
        try:
            value = element.text
        except AttributeError:
            value = element.get_attribute('value')
        self.logger.info("获取元素文本内容:{}".format(value))
        return value

    def get_element_attribute(self, by: str, location: str, attribute: str):
        element = self.find_element(by, location)
        try:
            return element.get_attribute(attribute)
        except Exception as e:
            self.logger.error("获取元素的{}属性失败{}".format(attribute, e))
            raise e

    def move_to_element_click(self, by: str, location: str):
        """
        move mouse to element and click
        :param by: xpath, id, name, class with str
        :param location: //*[@by="location"]
        :return: action
        """

        element = self.find_element(by, location)
        action = ActionChains(self.driver)
        action.move_to_element(element).click(element).perform()
        return action

    def execute_window_scroll(self, x: str, y: str):
        """滚动窗口"""
        try:
            js = 'window.scrollTo(' + x + ',' + y + ')'
            self.driver.execute_script(js)
        except InvalidArgumentException as e:
            self.logger.error("执行JS脚本失败{}".format(e))
            raise e

    def save_screen_shot(self, info: str = ''):
        """
        屏幕截图
        :param info:
        :return:
        """
        current_time = self.c_dir.get_current_time()
        img_path = self.c_dir.create_dir(ERROR_IMG_DIR)
        filename = img_path + '/' + current_time + info + '.png'
        return self.driver.save_screenshot(filename)

    # TODO: perfecting function
    def switch_to_window(self, new_window=None):
        """
        切换新窗口
        :param new_window: 新窗口句柄
        :return: 当前窗口句柄
        """
        if new_window is None:
            current_handle = self.driver.window_handles
            try:
                wait = WebDriverWait(self.driver, self.timeout)
                wait.until(ec.new_window_is_opened(current_handle))
                all_handles = self.driver.window_handles
                self.driver.switch_to.window(all_handles[-1])
                return current_handle
            except TimeoutException as e:
                self.logger.error("切换窗口失败或无新窗口被打开, 无需切换窗口")
                self.save_screen_shot("switch_window")
                raise e
        else:
            self.driver.switch_to.window(new_window)


if __name__ == '__main__':
    d = webdriver.Firefox()
    b = Base(d)
    b.open('https://www.baidu.com')
    b.find_element('id', 'kw').send_keys('linux超')
    b.find_element('id', 'su').click()
    b.find_elements('xpath', '//a[@class="c-showurl"]')[0].click()
    b.switch_to_window()
    print(b.find_element('xpath', '//a[@id="Header1_HeaderTitle"]').text)
    b.save_screen_shot('pass')
