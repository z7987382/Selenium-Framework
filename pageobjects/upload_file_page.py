# coding=utf-8
from framework.base_page import BasePage
from tools.myconfigparser import MyConfigParser
import os
from framework.logger import Logger
from selenium.webdriver.common.by import By

logger = Logger("UploadDebug").getlog()

class UploadPage(BasePage):
    path = "//*[@id=\"root\"]/section/section/main/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/span/input"
    input_box = (By.XPATH, path)
    btn = "//*[@id=\"root\"]/section/section/main/div/div[3]/div/div/button"
    btn_box = (By.XPATH, btn)
    def upload_file(self):
        file = "/Users/bytedance/Documents/pdf/A3-房屋租赁合同文本.pdf".decode("utf-8")
        self.upload(file, *self.input_box)

    def enter_the_page(self):
        url = "https://letsign-boe.bytedance.net/v2/saas/start-sign/upload"
        self.driver.get(url)
        logger.info("enter the page:%s" % url)

    def next_page(self):
        self.click(*self.btn_box)
        self.sleep(4)







