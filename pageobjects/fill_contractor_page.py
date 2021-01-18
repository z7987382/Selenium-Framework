# coding=utf-8
from framework.base_page import BasePage
from tools.myconfigparser import MyConfigParser
import os
from framework.logger import Logger
from selenium.webdriver.common.by import By



logger = Logger("UploadDebug").getlog()

class FillPage(BasePage):
    btn = "//*[@id=\"root\"]/section/section/main/div/div[3]/div/div/button[2]"
    btn_box = (By.XPATH, btn)

    def next_page(self):
        self.click(*self.btn_box)
        self.sleep(5)
    def enter_the_page(self):
        url = "https://letsign-boe.bytedance.net/v2/saas/start-sign/fill"
        self.driver.get(url)
        logger.info("enter the page:%s" % url)







