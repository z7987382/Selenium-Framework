#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import *
from pageobjects.login_page import *


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # cls.driver.quit()
        pass


    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.enter_the_page()
        loginpage.login()


if __name__ == '__main__':
    unittest.main()