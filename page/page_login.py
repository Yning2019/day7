"""
页面所有的操作步骤进行装
"""
import page
from base.base_login import BaseLogin


class PageLogin(BaseLogin):
    # 输入用户名
    def page_input_user(self, username):
        self.base_input(page.page_name, username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.page_pwd, pwd)

    # 点击登录
    def page_click(self):
       self.base_click(page.page_click_btn)

    # 组合业务
    def page_login(self):
        pass
