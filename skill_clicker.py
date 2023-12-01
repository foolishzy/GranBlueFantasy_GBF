from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from enum import Enum
from selenium import webdriver
import time
import re
from mouse import Mouse
from stage import checker  
from elementfinder import elefinder
from selenium.common.exceptions import  NoSuchElementException
class party:
    def __init__(self, chm : webdriver.Chrome, mouse : Mouse):
        self.chm = chm
        self.mouse = mouse
   
    def update(self):
        if checker(self.chm, 15).is_battle_page(15):
            self.player_one = character(1, self.chm, self.mouse)
            print('player 1 updated ' + self.player_one.state.name)
            self.player_two = character(2, self.chm, self.mouse)
            print('player 2 updated ' + self.player_two.state.name)
            self.player_three = character(3, self.chm, self.mouse)
            print('player 3 updated ' + self.player_three.state.name)
            self.player_four = character(4, self.chm, self.mouse)
            print('player 4 updated ' + self.player_four.state.name)
            self.players = [self.player_one, self.player_two, self.player_three, self.player_four]
        else:
            self.player_one = None
            self.player_two = None
            self.player_three = None
            self.player_four = None
            self.players = [self.player_one, self.player_two, self.player_three, self.player_four]

    def print_info(self):
        pass
    
    def use_skill(self, player_num : int, skill_num : int):
        if player_num > 0 and player_num < 5 and skill_num > 0 and skill_num < 5:
            for p in self.players:
                if p.index == player_num:
                    p.use_skill(skill_num)
        else:
            print('get wrong num')


class character:
    #each palyer have four skill
    #briefly element
    #extend element
    def __init__(self, index : int, chm : webdriver.Chrome, mouse : Mouse):
        self.chm = chm
        self.mouse = mouse
        if index < 5 and index > 0:
                    
            self.brief_element_xpath = '//*[@id="prt-command-top"]/div/div/div[' + str(index) +  ']'
            self.extend_element_xpath = '//div[@class="prt-command-chara chara' + str(index) + '"]' 
            self.state = self.check_character_state()         
            self.index = index    
            brief_element = self.get_brief_element()
            extend_element = self.get_extend_element()

            if brief_element and extend_element and self.state == character_state.exist  :
                skill_brief_element = brief_element.find_element_by_class_name('prt-ability-state')
                skill_extend_element = extend_element.find_element_by_class_name('prt-ability-list')
                
                self.skill_one = skill(1, skill_brief_element, skill_extend_element, self.chm  )
                self.skill_two = skill(2, skill_brief_element, skill_extend_element, self.chm ) 
                self.skill_three = skill(3, skill_brief_element, skill_extend_element, self.chm )
                self.skill_four = skill(4, skill_brief_element, skill_extend_element, self.chm )

        else:
            print('input wrong!')
    

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
            e = self.chm.find_element_by_xpath(self.brief_element_xpath)
            class_name = e.get_attribute('class')
            if re.search('blank', class_name):
                return character_state.dead
            else:
                return character_state.exist

    def open_skill_panel(self):
        selector_data  = {
                'element' : self.brief_element_xpath,
                'by' : By.XPATH
                } 
        self.mouse.click_by_element(selector_data, 3)
    
    def close_skill_panel(self):
        xpath = '//*[@id="cnt-raid-information"]/div[1]'
        selector_data  = {
                'element' : xpath,
                'by' : By.XPATH
                } 
        self.mouse.click_by_element(selector_data, 3)
    

    def use_skill(self, index : int):
        self.open_skill_panel()
        if index == 1:
            self.skill_one.use()
        elif index == 2:
            self.skill_two.use()
        elif index == 3:
            self.skill_three.use()
        elif index == 4:
            self.skill_four.use()
        self.close_skill_panel()

class skill:
    #state
    #cd
    #element
    def __init__(self, 
            index : int,
            group_brife_element : WebElement ,
            group_extend_element : WebElement ,
            chm : webdriver.Chrome ):
        self.group_brife_ele = group_brife_element
        self.group_extend_ele = group_extend_element
        self.index = index 
        self.chm = chm
        self.update_state()
        self.ex_e = self.get_extend_element()
        self.br_e = self.get_brief_element()
        print('skill ' + str(self.index) + ' updated') 

    def use(self):
        l1 = re.search('disable', self.ex_e.get_attribute('class'))
        l2 = self.state == skill_state.ready
        if (not l1 ) and l2:
            try:
                self.ex_e.click()
            except NoSuchElementException:
                print('NoSuchElementException')
                pass
   
    def get_extend_element(self):
        ele = './div[' + str(self.index)  +']'
        i = 0
        while i < 5:
            try:
                result = self.group_extend_ele.find_element_by_xpath(ele)
                break
            except NoSuchElementException:
                i = i + 1
                time.sleep(1)
                result = None
        return result

    def get_brief_element(self):
        ele =  './div[' + str(self.index)  +']'
        i = 0
        while i < 5:
            try: 
                result = self.group_brife_ele.find_element_by_xpath(ele)       
                break
            except NoSuchElementException:
                i = i + 1
                time.sleep(1)
                result = None
        return result


    def update_state(self):
        xpath = '//div[@class="lis-ability-state ability' + str(self.index) + '"]'        
        #  if elefinder(By.XPATH, xpath, 5, self.chm).is_element_presence():
        e = self.group_brife_ele.find_element_by_xpath(xpath)
        state = e.get_attribute('state')
        #  skill_type = e.get_attribute('type')
        if state == "2":
            self.state = skill_state.ready
        elif state == "1":
            self.state = skill_state.used
        elif state == '0':
            self.state = skill_state.empty

class skill_state(Enum):
        used = 1
        #used
        ready = 2
        #ready to use
        empty = 3
        #doesn't exist

class character_state(Enum):
        exist = 1
        dead = 2

