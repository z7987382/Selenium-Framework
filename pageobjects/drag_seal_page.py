# coding=utf-8
from framework.base_page import BasePage
from tools.myconfigparser import MyConfigParser
import os
from framework.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pyautogui


logger = Logger("DragSealDebug").getlog()

class DragSealPage(BasePage):
    btn = "//*[@id=\"root\"]/section/section/main/div/div[2]/div/div[1]/div/div[2]/div/span/div"
    btn_box = (By.XPATH, btn)

    btnnext = "#root > section > section > main > div > div.footer___3wMUj > div > div > button.byted-btn.byted-btn-size-md.byted-btn-type-primary.byted-btn-shape-angle.byted-can-input-grouped"
    btnnext_box = (By.CSS_SELECTOR, btnnext)

    refill = "body > div:nth-child(14) > div > div > div.byted-content-container.byted-modal-content-container.byted-modal.byted-modal-show.pc-captcha__wrapper > div.byted-content-inner.byted-modal-content-inner > div > div > span > label > input"
    refill_box = (By.CSS_SELECTOR, refill)

    apply = "body > div:nth-child(14) > div > div > div.byted-content-container.byted-modal-content-container.byted-modal.byted-modal-show.pc-captcha__wrapper > div.byted-content-footer.byted-modal-content-footer > div > button"
    apply_box = (By.CSS_SELECTOR, apply)

    def refill_number(self):
        self.type("999999", *self.refill_box)
        self.click(*self.apply_box)
        self.sleep(10)


    def next_page(self):
        self.click(*self.btnnext_box)
        self.sleep(2)

    def choose_seal(self):
        self.click(*self.btn_box)
        self.sleep(5)

    def drag_seal(self):
        logger.info("starting drag and drop")
        pyautogui.mouseDown(x=80, y=570)
        pyautogui.moveTo(x=700, y=550, duration=3)
        pyautogui.mouseUp()
        logger.info("ended drag and drop")








