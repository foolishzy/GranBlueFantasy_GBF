import time
import re
import pyautogui
import random
from elementfinder import elefinder
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from util import util
from mouse import Mouse
from timer import timer
from game import game


class struct_timer_record:
    def __init__(self):
        self.total_time = 0
        self.total_counts = 1
        self.average = 0

    def get_average(self):
        self.average = self.total_time / self.total_counts
        print("平均用时:", "%.2f" % self.average, "s,共", self.total_counts,
              "次\n")
        return self.average

    def reset(self):
        self.__init__()


class mymouse(Mouse):
    def click_check_by_sel_and_click_by_pos(
            self,
            selector_data={'by': By.CLASS_NAME, 'element': 'prt-btn-deck'},
            positions_data={'x': 0, 'y': 0},
            dert_data={'x': 0, 'y': 0},
            waittime=10
    ):
        # 这里参数的默认值是乱写的，传入参数满足这个数据格式要求
        x = positions_data['x']
        y = positions_data['y']
        dert_x = dert_data['x']
        dert_y = dert_data['y']
        x = self.selfrandom(x, dert_x)
        y = self.selfrandom(y, dert_y)
        by = selector_data['by']
        ele = selector_data['element']
        times = 0
        while times < 3:
            times = times + 1
            if elefinder(by, ele,  waittime, self.chm).is_element_visibility():
                time.sleep(0.5 + random.random())
                pyautogui.click(x, y)
                break
            else:
                print('click erro , can not find element')

    def click_by_element(
            self,
            selector_data={'by': By.CLASS_NAME, 'element': 'prt-btn-deck'},
            waittime=2):
        # 这里参数的默认值是乱写的，传入参数满足这个数据格式要求
        flag = True
        by = selector_data['by']
        ele = selector_data['element']
        elf = elefinder(by, ele, waittime, self.chm)
        if elf.is_element_clickable():
            e = self.chm.find_element(by, ele)
            time.sleep(0.5 + 1 * random.random())
            index = 0
            while index < 2:
                try:
                    e.click()
                    index = 2
                except StaleElementReferenceException:
                    print(' StaleElementReferenceException')
                    print(' can not ensure element have been clicked ')
                    index = index + 1
                except ElementClickInterceptedException:
                    self.chm.execute_script("$(arguments[0]).click()", e)
                    index = 2
                except ElementNotInteractableException:
                    self.chm.execute_script("$(arguments[0]).click()", e)
                    index = 2
        else:
            flag = False
            print('element ', ele, " can not be clicked")
        return flag


class dark_trial_normal(game):

    url = 'https://game.granbluefantasy.jp/#quest/supporter/400481/5'
    timer = timer()

    def __init__(self):
        super().__init__(2)
        self.mouse = mymouse(self.chm)
        self.str = struct_timer_record()

    def play(self):
        self.str.total_counts = 0
        j = 5
        while (j > 0):
            j = j-1
            if j == 5:
                time.sleep(60)
            i = 50
            while(i > 0):
                self.str.total_counts = self.str.total_counts+1
                i = i - 1
                self.timer.start()
                self.stage.goto(self.url)
                self.mouse.click_friend_summon()
                self.mouse.click_party_ok()
                self.mouse.click_attack()
                time.sleep(0.3)
                self.stage.goto(self.url)
                self.mouse.click_attack()
                time.sleep(0.3)
                self.stage.goto(self.url)
                time.sleep(0.5)
                self.timer.end()
                self.str.total_time = self.str.total_time + \
                    self.timer.end_time - self.timer.start_time
                self.str.get_average()


dtn = dark_trial_normal()
dtn.play()
