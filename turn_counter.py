from enum import Enum
from mouse import Mouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from elementfinder import elefinder
from util import util
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException, WebDriverException
import time
from stage import checker


class turn_counter:
    xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[5]/div[2]/div[1]'
    phrase_str = 'num-turn'

    def __init__(self, chm: webdriver.Chrome, mouse: Mouse):
        """__init__.

        :param chm:
        :type chm: webdriver.Chrome
        :param mouse:
        :type mouse: Mouse
        """
        self.chm = chm
        self.mouse = mouse
        self.index = 0

    def update(self):
        if checker(self.chm, 3).is_battle_page(5):
            self.get_turn_num()
            print('turn counter updeted')

    def get_turn_num(self):
        """get_turn_num."""
        #  if elefinder(By.XPATH, self.xpath, 3, self.chm).is_element_presence():
        # 使用full标签判断页面，然后获取数值
        full_bt = util.screen_label_battle_full
        elf = elefinder(full_bt['by'], full_bt['element', 3, self.chm])
        if elf.is_element_clickable():
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
