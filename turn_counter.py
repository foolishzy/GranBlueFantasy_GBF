from enum import Enum
from mouse import Mouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from elementfinder import elefinder
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException, WebDriverException
import time
from stage import checker


class turn_counter:
    xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[5]/div[2]/div[1]'
    phrase_str = 'num-turn'

    def __init__(self, chm: webdriver.Chrome, mouse: Mouse):
        self.chm = chm
        self.mouse = mouse
        self.index = 0

    def update(self):
        if checker(self.chm, 3).is_battle_page(5):
            self.get_turn_num()
            print('turn counter updeted')

    def get_turn_num(self):
        if elefinder(By.XPATH, self.xpath, 3, self.chm).is_element_presence():
            try:
                e = self.chm.find_element_by_xpath(self.xpath)
                txt = e.get_attribute('class')
                txt = txt.replace(self.phrase_str, '')
            except NoSuchElementException:
                txt = ""
                pass
            except WebDriverException:
                txt = ""
                pass

            if txt == '':
                num = 0
            else:
                num = int(txt)
            return num
        else:
            return 0
        print('current turn :', self.index)
