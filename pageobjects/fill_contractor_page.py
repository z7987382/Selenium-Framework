# coding=utf-8
from framework.base_page import BasePage
from tools.myconfigparser import MyConfigParser
import os
from framework.logger import Logger
from selenium.webdriver.common.by import By



logger = Logger("UploadDebug").getlog()

class FillPage(BasePage):
    btn = "#root > section > section > main > div > div.footer___3wMUj > div > div > button.byted-btn.byted-btn-size-md.byted-btn-type-primary.byted-btn-shape-angle.byted-can-input-grouped"
    btn_box = (By.CSS_SELECTOR, btn)

    def next_page(self):
        self.click(*self.btn_box)
        self.sleep(5)
    def enter_the_page(self):
        url = "https://letsign-boe.bytedance.net/v2/saas/start-sign/fill"
        self.driver.get(url)
        logger.info("enter the page:%s" % url)







