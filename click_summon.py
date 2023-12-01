import re
from enum import Enum
from mouse import Mouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from elementfinder import elefinder
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time


class summon:
    brief_element_xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[11]/div[2]/div'
    summon_okbt_dialog_xpath = '//*[@id="wrapper"]/div[3]/div[14]'

    def __init__(self, index: int, chm: webdriver.Chrome, mouse: Mouse):

        self.index = index
        self.chm = chm
        self.mouse = mouse
        self.element = self.get_brief_element()
        self.state = self.get_state()
        self.name = self.get_summon_name()
        self.cold_down = self.get_cd()
        print('summon ' + str(self.index) + ' init...  ' +
              self.state.name + '  cd: ' + self.cold_down +
              " " + self.name)

    def get_cd(self):
        if self.element:
            return self.element.get_attribute('summon-recast')

    def get_summon_name(self):
        if self.element:
            return self.element.get_attribute('summon-name')

    def get_brief_element(self):
        summons_xpath = self.brief_element_xpath
        summon_xpath = './div[' + str(self.index + 1) + ']'
        elf = elefinder(By.XPATH, summons_xpath, 5, self.chm)
        if elf.is_element_presence():
            e = self.chm.find_element_by_xpath(summons_xpath)
            ee = e.find_element_by_xpath(summon_xpath)
        return ee

    def use(self):
        if self.state == summon_state.available:
            try:
                self.element.click()
            except ElementNotInteractableException:
                self.chm.execute_script(
                    '$(arguments[0]).click()', self.element)
            time.sleep(1)
            elf = elefinder(
                By.XPATH, self.summon_okbt_dialog_xpath, 3, self.chm)
            if elf.is_element_presence():
                dialog_ele = self.chm.find_element_by_xpath(
                    self.summon_okbt_dialog_xpath)
                try:
                    ok_ele = dialog_ele.find_element_by_xpath(
                        './div[3]/div[2]')
                    ok_ele.click()
                except ElementNotInteractableException:
                    self.chm.execute_script("$(arguments[0]).click()", ok_ele)
                except NoSuchElementException:
                    print('NoSuchElementException')
                    pass
            print('summon ' + str(self.index) + self.name + ' used')
        pass

    def get_state(self):
        if self.element:
            class_name = self.element.get_attribute('class')
            if not re.search('unavailable', class_name):
                s = summon_state.available
            else:
                s = summon_state.unavailable
        return s


class summon_state(Enum):
    available = 1
    unavailable = 0


class battle_summons:

    extend_summon_panel_xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[11]/div[2]/div/div[1]'
    close_summon_panel_xpath = '//*[@id="cnt-raid-information"]/div[1]'
    brief_summons_xpath = '//*[@id="wrapper"]/div[3]/div[2]/div[11]/div[2]/div'

    def use_all_summon(self):
        flag = False
        for s in self.summon_group:
            if s.state == summon_state.available:
                self.open_summon_panel()
                s.use()
                flag = True
                break
        if not flag:
            print('summons are not available')

    def use_summon(self, index):
        if index > 0 and index < 7:
            self.open_summon_panel()
            self.summon_group[index].use()
        pass

    def close_summon_panel(self):
        selector = {
            'by': By.XPATH,
            'element': self.close_summon_panel
        }
        elf = elefinder(selector['by'], selector['element'], 3, self.chm)
        if elf.is_element_clickable():
            self.mouse.click_by_element(selector, 3)
            print('summon panel closed')

    def open_summon_panel(self):
        selector = {
            'by': By.XPATH,
            'element': self.extend_summon_panel_xpath
        }
        elf = elefinder(selector['by'], selector['element'], 3, self.chm)
        if elf.is_element_clickable():
            self.mouse.click_by_element(selector, 3)
            time.sleep(0.5)
            print('summon panel opened')

    def __init__(self, chm: webdriver.Chrome, mouse: Mouse):
        self.chm = chm
        self.mouse = mouse
        self.summon_group = list()
        pass

    def update(self):
        xpath = self.brief_summons_xpath
        elf = elefinder(By.XPATH, xpath, 3, self.chm)
        if elf.is_element_presence():
            self.brief_summons_element = self.chm.find_element_by_xpath(xpath)
            self.summon_group = list()
            for i in range(1, 6):
                s = summon(i, self.chm, self.mouse)
                self.summon_group.append(s)
        print('summons updated ')
