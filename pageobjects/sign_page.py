# coding=utf-8
from framework.base_page import BasePage
from tools.myconfigparser import MyConfigParser
import os
from framework.logger import Logger
from selenium.webdriver.common.by import By



logger = Logger("SignDebug").getlog()

class SignPage(BasePage):
    btn = "//*[@id=\"root\"]/section/section/main/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/div"
    btn_box = (By.XPATH, btn)

    btnnext = "//*[@id=\"root\"]/section/section/main/div/div[4]/div/div/button[2]"
    btnnext_box = (By.XPATH, btnnext)

    refill = "body > div:nth-child(11) > div > div > div.byted-content-container.byted-modal-content-container.byted-modal.byted-modal-show.pc-captcha__wrapper > div.byted-content-inner.byted-modal-content-inner > div > div > span > label > input"
    refill_box = (By.CSS_SELECTOR, refill)

    apply = "body > div:nth-child(11) > div > div > div.byted-content-container.byted-modal-content-container.byted-modal.byted-modal-show.pc-captcha__wrapper > div.byted-content-footer.byted-modal-content-footer > div > button"
    apply_box = (By.CSS_SELECTOR, apply)

    def next_page(self):
        self.click(*self.btnnext_box)
        self.sleep(5)

    def choose_seal(self):
        self.sleep(5)
        self.click(*self.btn_box)

    def refill_number(self):
        self.type("999999", *self.refill_box)
        self.sleep(1)
        self.click(*self.apply_box)







