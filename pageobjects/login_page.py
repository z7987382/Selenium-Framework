# coding=utf-8
from framework.base_page import BasePage
from tools.myconfigparser import MyConfigParser
import os
from framework.logger import Logger
from selenium.webdriver.common.by import By
logger = Logger("LoginDebug").getlog()

class LoginPage(BasePage):

    def login(self):
        # 读取配置文件
        config = MyConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        cookie = config.items("cookie")
        localstorage = config.items("localstorage")
        # 添加cookie和localstorage
        self.add_cookie(cookie)
        self.add_localstorage(localstorage)
        self.refresh()


    def enter_the_page(self):
        url = "https://letsign-boe.bytedance.net/v2/saas/login"
        self.driver.get(url)
        logger.info("enter the page:%s" % url)




