#! /usr/bin/env python
# coding=utf-8

import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import *
from pageobjects.login_page import *
from pageobjects.upload_file_page import *
from pageobjects.fill_contractor_page import *
from pageobjects.drag_seal_page import *
from pageobjects.sign_page import *


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
        time.sleep(10)
        cls.driver.quit()


    def test_A_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.enter_the_page()
        loginpage.login()


    def test_B_upload_file(self):
        uploadpage = UploadPage(self.driver)
        uploadpage.enter_the_page()
        uploadpage.upload_file()
        uploadpage.next_page()

    def test_C_fill_contractor(self):
        fillpage = FillPage(self.driver)
        fillpage.next_page()

    def test_D_Drag_Seal(self):
        dragsealpage = DragSealPage(self.driver)
        dragsealpage.choose_seal()
        dragsealpage.drag_seal()
        dragsealpage.next_page()
        dragsealpage.refill_number()
        time.sleep(5)

    def test_E_sign(self):
        signpage = SignPage(self.driver)
        signpage.choose_seal()
        signpage.next_page()
        signpage.refill_number()






if __name__ == '__main__':
    unittest.main()