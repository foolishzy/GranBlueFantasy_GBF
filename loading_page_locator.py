from threading import Event
from elementfinder import elefinder 
from util import util
from mouse import Mouse
import re 
import time
from selenium import webdriver
from threading import Thread
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import  StaleElementReferenceException
class lpl:
    
    ele = util.loading_page_element['element']
    by = util.loading_page_element['by']

    def __init__(self, chm : webdriver.Chrome, refreshtime = 10):
        self.chm =chm
        self.time = refreshtime
      # 超过五秒刷新
        pass

    def is_loading_page(self):
        flag = False
        try:
            WebDriverWait(self.chm, 0.5).until(
                EC.visibility_of_element_located(
                (self.by, self.ele)
            )
                )
            flag = True
        except StaleElementReferenceException:
            pass
        except TimeoutException:
            pass
        except  WebDriverException:
            pass
        return flag

    def start(self):
        while True:
            start_time = 0
            end_time = 0
            if self.is_loading_page():
                start_time = time.time()
                while self.is_loading_page():
                    end_time = time.time()
            if end_time - start_time > self.time :
                self.chm.refresh()

class last_turn_locator:

    ele_lt = util.screen_label_battle_lastturn_processing['element']
    by_lt = util.screen_label_battle_lastturn_processing['by']
    
    def __init__(self, chm : webdriver.Chrome, event : Event, mouse : Mouse):
        self.eve = event
        self.chm = chm
        self.mouse = mouse
        pass

    def start(self):
        string_lt = util.screen_label_battle_lastturn_processing['text']
        elf = elefinder(self.by_lt, self.ele_lt, 2,self.chm )
        while self.eve.is_set():
            if elf.is_element_visibility():
                text = elf.get_element_text()
                if re.match(text, string_lt) and re.match(text, string_lt).span()[1] > 0:
                    self.chm.refresh()
                    self.mouse.click_full()
            time.sleep(1)    

class goal_page_locator:
    by = util.screen_label_battle_goal_exp['by']
    ele = util.screen_label_battle_goal_exp['element']

    def __init__(self, chm : webdriver.Chrome, event : Event, ctrl_event : Event):
        self.eve = event
        self.chm = chm
        self.ctrl_event = ctrl_event
        pass

    def start(self):
        flag = False
        elf = elefinder(self.by, self.ele, 2, self.chm)
        while self.eve.is_set():
            if elf.is_element_visibility():
                flag = True
            else:
                current_url = self.chm.current_url
                if (re.match(current_url, 'result') and re.match(current_url, 'result').span()[1] > 0) or (re.match(current_url, 'quest') and re.Match(current_url, 'quest').span()[1] > 0):
                    flag = True
            if flag :
                self.ctrl_event.clear()
            #  print('ctrl_event: ',self.ctrl_event.is_set())
            time.sleep(1)    
