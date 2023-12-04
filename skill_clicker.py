from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from enum import Enum
from selenium import webdriver
import time
import re
from mouse import Mouse
from stage import checker
from elementfinder import elefinder
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class party:
    def __init__(self, chm: webdriver.Chrome, mouse: Mouse):
        self.chm = chm
        self.mouse = mouse
        self.manual_skill_list = [[0, [0]]]

    def update(self):
        if (not self.manual_skill_list == [[0, [0]]]) and checker(self.chm, 15).is_battle_page(15):
            self.player_one = character(1, self.chm, self.mouse)
            print('player 1 updated ' + self.player_one.state.name)
            self.player_two = character(2, self.chm, self.mouse)
            print('player 2 updated ' + self.player_two.state.name)
            self.player_three = character(3, self.chm, self.mouse)
            print('player 3 updated ' + self.player_three.state.name)
            self.player_four = character(4, self.chm, self.mouse)
            print('player 4 updated ' + self.player_four.state.name)
            self.players = [self.player_one, self.player_two,
                            self.player_three, self.player_four]
        else:
            self.player_one = None
            self.player_two = None
            self.player_three = None
            self.player_four = None
            self.players = [self.player_one, self.player_two,
                            self.player_three, self.player_four]

    def print_info(self):
        pass

    def use_skill(self, player_num: int, skill_num: int):
        if checker(self.chm, 10).is_battle_page(10) and player_num > 0 and player_num < 5 and skill_num > 0 and skill_num < 5:
            p = self.players[player_num - 1]
            if p:
                p.use_skill(skill_num)
        else:
            print('get wrong num')

    def set_manual_skill_list(self,  lst=[[0, [0, 0, 0]], [0, [0]]]):
        '''
    #自动刷新之后使用的技能列表[[a,[b,c,d...] ], ...], a 队员index [b, c, d...] 技能index
    主要是针对一些没法自动释放的技能
        '''
        if lst:
            self.manual_skill_list = lst

    def use_manual_skill(self):
        if self.manual_skill_list:
            for l in self.manual_skill_list:
                player_index = l[0]
                skill_index = l[1]
                for si in skill_index:
                    if player_index > 0 and player_index < 5 and si > 0 and si < 5:
                        self.use_skill(player_index, si)
        else:
            print('manual skill list must be init')


class character:
    # each palyer have four skill
    # briefly element
    # extend element
    def __init__(self, index: int, chm: webdriver.Chrome, mouse: Mouse):
        self.chm = chm
        self.mouse = mouse
        if index < 5 and index > 0:

            self.brief_element_xpath = '//*[@id="prt-command-top"]/div/div/div[' + str(
                index) + ']'
            self.extend_element_xpath = '//div[@class="prt-command-chara chara' + str(
                index) + '"]'
            self.state = self.check_character_state()
            self.index = index
            self.brief_element = self.get_brief_element()
            self.extend_element = self.get_extend_element()

            if self.brief_element and self.extend_element and self.state == character_state.exist:
                skill_brief_element = self.brief_element.find_element_by_xpath(
                    './div[6]')
                skill_extend_element = self.extend_element.find_element_by_xpath(
                    './div[3]')

                self.skill_one = skill(
                    1, skill_brief_element, skill_extend_element, self.chm)
                self.skill_two = skill(
                    2, skill_brief_element, skill_extend_element, self.chm)
                self.skill_three = skill(
                    3, skill_brief_element, skill_extend_element, self.chm)
                self.skill_four = skill(
                    4, skill_brief_element, skill_extend_element, self.chm)

            self.hp = self.get_hp()
            self.gauge_hp = self.get_gauge_attack()
            print("player ", self.index, "hp: ", self.hp,
                  'ca_hp: ', self.gauge_hp, self.state.name)
        else:
            print('input wrong!')

    def get_hp(self):
        if self.state == character_state.exist and self.brief_element:
            xpath = './div[3]/div[2]'
            try:
                txt = self.brief_element.find_element_by_xpath(xpath).text
            except StaleElementReferenceException:
                txt = ""
                pass
            if txt == "":
                txt = "0"
            return int(txt)
        else:
            return 0

    def get_gauge_attack(self):
        if self.state == character_state.exist:
            xpath = './div[4]/div[3]'
            try:
                txt = self.brief_element.find_element_by_xpath(xpath).text
            except StaleElementReferenceException:
                txt = ""
                pass
            if txt == "":
                txt = "0"
            else:
                txt = txt.replace('%', "")
            return int(txt)

    def get_buff(self):
        pass

    def get_brief_element(self):
        elf = elefinder(By.XPATH,
                        self.brief_element_xpath,
                        10,
                        self.chm)
        if elf.is_element_presence():
            return self.chm.find_element_by_xpath(self.brief_element_xpath)
        else:
            return None

    def get_extend_element(self):
        elf = elefinder(By.XPATH,
                        self.extend_element_xpath,
                        10,
                        self.chm)
        if elf.is_element_presence():
            return self.chm.find_element_by_xpath(self.extend_element_xpath)
        else:
            return None

    def check_character_state(self):
        elf = elefinder(By.XPATH, self.brief_element_xpath, 5, self.chm)
        if elf.is_element_presence():
            try:
                e = self.chm.find_element_by_xpath(self.brief_element_xpath)
                class_name = e.get_attribute('class')
                if re.search('blank', class_name):
                    state = character_state.dead
                else:
                    state = character_state.exist
            except StaleElementReferenceException:
                state = character_state.dead
                pass
            if state:
                return state
        else:
            return character_state.dead

    def open_skill_panel(self):
        selector_data = {
            'element': self.brief_element_xpath,
            'by': By.XPATH
        }
        self.mouse.click_by_element(selector_data, 3)

    def close_skill_panel(self):
        xpath = '//*[@id="cnt-raid-information"]/div[1]'
        selector_data = {
            'element': xpath,
            'by': By.XPATH
        }
        self.mouse.click_by_element(selector_data, 3)

    def use_skill(self, index: int):
        if self.state == character_state.exist:
            if index == 1:
                if self.skill_one.state == skill_state.ready:
                    self.open_skill_panel()
                    self.skill_one.use()
            elif index == 2:
                if self.skill_two.state == skill_state.ready:
                    self.open_skill_panel()
                    self.skill_two.use()
            elif index == 3:
                if self.skill_three.state == skill_stae.ready:
                    self.open_skill_panel()
                    self.skill_three.use()
            elif index == 4:
                if self.skill_four.state == skill_stae.ready:
                    self.open_skill_panel()
                    self.skill_four.use()
            self.close_skill_panel()


class skill:
    # state
    # cd
    # element
    def __init__(self,
                 index: int,
                 group_brife_element: WebElement,
                 group_extend_element: WebElement,
                 chm: webdriver.Chrome):
        self.group_brife_ele = group_brife_element
        self.group_extend_ele = group_extend_element
        self.index = index
        self.chm = chm
        self.ex_e = self.get_extend_element()
        self.br_e = self.get_brief_element()
        self.update_state()
        print('skill ' + str(self.index) + ' updated ' + self.state.name)

    def use(self):
        #  class_name = self.ex_e.get_attribute('class')
        #  l1 = re.search('disable', class_name) or re.search(
        #  'unavailable', class_name)
        l2 = self.state == skill_state.ready
        if l2:
            try:
                print('use skill', self.index,  self.state.name)
                self.ex_e.click()
                time.sleep(0.5)
            except NoSuchElementException:
                print('NoSuchElementException')
            except ElementNotInteractableException:
                self.chm.execute_script(
                    '$(arguments[0]).click()', self.ex_e)
                time.sleep(0.5)
        else:
            print('skill', self.index, 'can not be used')

    def get_extend_element(self):
        ele = './div[' + str(self.index) + ']'
        i = 0
        result = None
        while i < 5:
            try:
                result = self.group_extend_ele.find_element_by_xpath(ele)
                break
            except NoSuchElementException:
                i = i + 1
                time.sleep(1)
                result = None
            except StaleElementReferenceException:
                i = i + 1
                time.sleep(1)
        return result

    def get_brief_element(self):
        ele = './div[' + str(self.index) + ']'
        i = 0
        while i < 5:
            try:
                result = self.group_brife_ele.find_element_by_xpath(ele)
                break
            except NoSuchElementException:
                i = i + 1
                time.sleep(1)
                result = None
            except StaleElementReferenceException:
                i = i + 1
                time.sleep(1)
                result = None
        return result

    def update_state(self):
        if self.ex_e:
            class_name = self.ex_e.get_attribute('class')
            l1 = re.search('disable', class_name) or re.search(
                'unavailable', class_name)
        else:
            l1 = None
        xpath = './div[' + \
            str(self.index) + ']'
        #  if elefinder(By.XPATH, xpath, 5, self.chm).is_element_presence():
        state = None
        if self.group_brife_ele:
            try:
                e = self.group_brife_ele.find_element_by_xpath(xpath)
                state = e.get_attribute('state')
            except StaleElementReferenceException:
                pass

        if l1 and (state == "1" or state == "2"):
            self.state = skill_state.forbidden
        elif (state == "2") and (not l1):
            self.state = skill_state.ready
        elif (state == "1") and (not l1):
            self.state = skill_state.used
        elif state == '0':
            self.state = skill_state.empty
        else:
            self.state = skill_state.empty


class skill_state(Enum):
    used = 1
    # used
    ready = 2
    # ready to use
    empty = 0
    # doesn't exist
    forbidden = 3
    # can't be used


class character_state(Enum):
    exist = 1
    dead = 2
