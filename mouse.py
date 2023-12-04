import re
import pyautogui
from util import util
import time
import random
from elementfinder import elefinder
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException


class Mouse:

    def __init__(self, chm: webdriver.Chrome):
        self.util = util
        self.chm = chm
        pass

    def move_to(self, x, y):
        pyautogui.moveTo(x, y)

    def click(self, x, y):
        pyautogui.click(x, y, interval=0.2)

    def click_by_positon(
            self,
            position_data={'x': 0, 'y': 0},
            dert={'x': 0, 'y': 0}
    ):
        x = positions_data['x']
        y = positions_data['y']
        dert_x = dert['x']
        dert_y = dert['y']
        x = self.selfrandom(x, dert_x)
        y = self.selfrandom(y, dert_y)
        self.click(x, y)

    def right_click(self, x, y):
        pyautogui.rightClick(x, y)

    def click_friend_summon(self):
        #  data = util.screen_lable_friend_summon
        #  self.click_by_element(data)
        position = util.mouse_position_friend_summon
        dert = util.mouse_position_friend_summon_dert
        selector = util.screen_label_friend_summmon_page
        self.click_check_by_sel_and_click_by_pos(selector, position, dert, 10)

    def click_arcum_part_ok(self):
        #  selector_data = self.util.screen_label_arcum_part_ok
        #  position_data = self.util.mouse_position_arcum_party_ok
        #  dert_data = self.util.mouse_position_party_ok_dert
        #  self.click_check_by_sel_and_click_by_pos(selector_data, position_data, dert_data, 10)
        data = util.screen_label_arcum_part_ok
        self.click_by_element(data, 3)

    def click_party_ok(self):
        data = util.screen_label_party_ok
        self.click_by_element(data, 2)
        #  self.click_check_by_sel_and_click_by_pos(
        #  self.util.screen_label_party_ok,
        #  self.util.mouse_position_party_ok,
        #  self.util.mouse_position_party_ok_dert
        #  )

    def click_request_cancel(self):
        self.click_by_element(
            {'by': By.CLASS_NAME,
             'element': "btn-usual-cancel"},
            5)

    def click_request_backup(self):
        time.sleep(3)
        data = util.screen_lable_battle_request_backup
        self.click_by_element(data, waittime=5)
        data = util.screen_lable_battle_request_backup_dialog_backup
        self.click_by_element(data,  waittime=5)
        data = util.screen_lable_battle_request_backup_dialog_ok
        self.click_by_element(data,  waittime=5)
        time.sleep(1)

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
                time.sleep(3 + random.random())
                pyautogui.click(x, y)
                break
            else:
                print('click erro , can not find element')

    def click_gauge_ok(self):
        data = util.screen_label_arcum_gauge_ok
        self.click_by_element(data)
        time.sleep(1)

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
            time.sleep(3 + 2 * random.random())
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

    def click_box(self,
                  gauge_and_box_data={
                      'box_ele': 'txt-chest-name',
                      'box_txt': "Splendid Chest",
                      'gauge_ele': 'txt-quest-name',
                      'gauge_txt': ['Herald of The Moon', 'Herald of Death', 'Herald of Justice'],
                      'enemy_ele': 'txt-quest-name',
                      'enemy_txt': ['Mimic', 'Obsidian Machina']
                  }):
        select_data = {
            'by': By.CLASS_NAME,
            'element': gauge_and_box_data['box_ele']
        }
        self.click_by_element(select_data)
        time.sleep(5)

    def click_gauge_enemy(self,
                          gauge_and_box_data={
                              'box_ele': 'txt-chest-name',
                              'box_txt': "Splendid Chest",
                              'gauge_ele': 'txt-quest-name',
                              'gauge_txt': ['Herald of The Moon', 'Herald of Death', 'Herald of Justice'],
                              'enemy_ele': 'txt-quest-name',
                              'enemy_txt': ['Mimic', 'Obsidian Machina']
                          }):
        select_data = {
            'by': By.CLASS_NAME,
            'element': gauge_and_box_data['enemy_ele']
        }
        self.click_by_element(select_data)
        time.sleep(1)

    def click_gauge(self,
                    gauge_and_box_data={
                        'box_ele': 'txt-chest-name',
                        'box_txt': "Splendid Chest",
                        'gauge_ele': 'txt-quest-name',
                        'gauge_txt': ['Herald of The Moon', 'Herald of Death', 'Herald of Justice'],
                        'enemy_ele': 'txt-quest-name',
                        'enemy_txt': ['Mimic', 'Obsidian Machina']
                    }):
        select_data = {
            'by': By.CLASS_NAME,
            'element': gauge_and_box_data['gauge_ele']
        }
        self.click_by_element(select_data)
        time.sleep(1)

    def click_attack(self):
        select_data = self.util.screen_label_battle_attack
        positon = self.util.mouse_position_battle_attack
        dert = self.util.mouse_position_battle_attack_dert
        self.click_check_by_sel_and_click_by_pos(select_data, positon, dert)

    def click_full(self, waittime=10):
        ele_full = self.util.screen_label_battle_full['element']
        by_full = self.util.screen_label_battle_full['by']
        x = self.util.mouse_position_battle_full['x']
        y = self.util.mouse_position_battle_full['y']
        dert_x = self.util.mouse_position_battle_full_dert['x']
        dert_y = self.util.mouse_position_battle_full_dert['y']
        x = x + int(random.random() * dert_x)
        y = y + int(random.random() * dert_y)
        elf = elefinder(by_full, ele_full, waittime, self.chm)
        if elf.is_element_clickable():
            time.sleep(1 + 2 * random.random())
            self.click(x, y)
            print('full btn clicked by posittion')
        else:
            print('full btn cannot be clicked')
        #  selector_data = self.util.screen_label_arcum_gauge_ok
        #  self.click_by_element(selector_data, 5)

    def selfrandom(self, value, dert):
        return int(random.random() * dert) + value

    def click_rapid_filter_frist(self):
        position = self.util.mouse_position_rapid_filter_frist
        dert = self.util.mouse_position_rapid_filter_frist_dert
        if True:
            #
            # 判断是否在多人救援页面 判断第一条救援是否存在
            #
            #self.click(x, y)
            pass
