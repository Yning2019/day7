"""
base页面，所有page页面的公共方法类

"""
from selenium.webdriver.support.wait import WebDriverWait


class BaseLogin:
    # 初始化driver对象
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def base_find_el(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self, loc, values):
        el = self.base_find_el(loc)
        el.clear()
        el.send_keys(values)

    # 点击方法
    def base_click(self, el):
        self.base_find_el(el).click()
