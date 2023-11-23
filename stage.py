from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
from util import util
from elementfinder import elefinder
from selenium.webdriver.common.by import By
import re
import time
from selenium.webdriver.support import expected_conditions as EC


class stage:


    def homepage(self):
        """
        打开首页
        """
        by = self.util.screen_label_home['by']
        ele = self.util.screen_label_home['element']
        url = self.util.url_home
        self.goto(url)
        return elefinder(by, ele, 10, self.chm).is_element_visibility()

    def loader(self, url : str, flag_by : By, flag_ele : str, retry_times = 3  ):
        """
        打开给定url的网页，指定该页面上的一个element，如果该element存在返回True，默认重试3次，每次寻找指定的element等待10s
        """
        times = 0 
        while times < retry_times:
            times = times + 1
            self.goto(url)
            if elefinder(flag_by, flag_ele, 10, self.chm).is_element_visibility():
                flag = True
                break
            else:
                flag = False
        return flag

    def __init__(self, chm : webdriver.Chrome):
        self.chm = chm
        self.util = util
    
    def loading_page_refresh(self, waittime = 10):
        ele = util.loading_page_element['element']
        by = util.loading_page_element['by']
        ck = checker(self.chm, waittime)
        if ck.is_loading_page():
            i = 0 
            while i < 3:
                i = i + 1
                try:
                    WebDriverWait(self.chm, waittime).until_not(
                             EC.visibility_of_element_located((by, ele))
                            )
                    break
                except TimeoutException:
                    refresh()
                except WebDriverException:
                    pass


    def goto(self, url, tagetpage_selector = {'element' : "", 'by': ""}):
        # tagetpage_selector判断页面是否成功打开,如果这个参数没有被传进来，那么默认不进行判断
        by = tagetpage_selector['by']
        ele = tagetpage_selector['element']
        while True:
            try:
                self.chm.get(url)
                if (not by == ""):
                    if elefinder(by,ele,10,self.chm).is_element_visibility():                 
                        break
                else:
                    break
                    # 这里loading_page_refresh判断的逻辑有问题，不知道该抓哪个元素，要是按照loading哪个图片的标签进行对比，好像很多webwait的判断都要重新写，麻烦。
                    #  不加的话也可以，就是网速不好卡住的时候要等很久
                    # 在game的play方法中加一个线程专门判断是否卡在刷新界面
                    # self.loading_page_refresh()
                    # 成功打开则跳出while
            except UnexpectedAlertPresentException:
            # 解决那个app更新的对话框
                alert = self.chm.switch_to.alert
                print('alert  txt : ', alert.text)
                alert.accept()
            except WebDriverException:
                print('webDriverException')
                time.sleep(1)
                

    def refresh(self):
        url = self.chm.current_url
        by =  '//div[@class="prt-command"]'
        ele = By.XPATH
        self.loader(url, by, ele, 3)
    

class checker:

    def __init__(self, chm : webdriver.Chrome, waittime = 10 ):
        self.chm = chm
        self.util = util
        self.waittime = waittime 
        self.stage = stage(self.chm)
  
    def check_box(self,
            gauge_box_data ={
                'box_ele' : 'txt-chest-name',
                'box_txt' : "Splendid Chest",
                'gauge_ele' : 'txt-quest-name',
                'gauge_name' : ['Herald of The Moon','Herald of Death','Herald of Justice' ] ,
                'box_enemy_ele' : 'txt-quest-name',
                'box_enemy_name' : ['Mimic', 'Obsidian Machina']
                }    ):
        txt = gauge_box_data['box_txt']
        by = By.CLASS_NAME
        ele = gauge_box_data['box_ele']
        elf = elefinder(by, ele, 1, self.chm)
        if elf.is_element_visibility():
            if elf.get_element_text() == txt:
                return True
            else:
                return False
    
    def check_gauge(self,
                    gauge_box_data ={
                    'box_ele' : 'txt-chest-name',
                    'box_txt' : "Splendid Chest",
                    'gauge_ele' : 'txt-quest-name',
                    'gauge_name' : ['Herald of The Moon','Herald of Death','Herald of Justice' ] ,
                    'box_enemy_ele' : 'txt-quest-name',
                    'box_enemy_name' : ['Mimic', 'Obsidian Machina']
                    }    ):
        txt = gauge_box_data['gauge_name']
        by = By.CLASS_NAME
        ele = gauge_box_data['gauge_ele']
        elf = elefinder(by, ele, 1, self.chm)
        if elf.is_element_visibility():
            for t in txt:
                if elf.get_element_text() == t:
                    return True
                else:
                    return False


    def check_gauge_enemy(self,
                gauge_box_data ={
                    'box_ele' : 'txt-chest-name',
                    'box_txt' : "Splendid Chest",
                    'gauge_ele' : 'txt-quest-name',
                    'gauge_name' : ['Herald of The Moon','Herald of Death','Herald of Justice' ] ,
                    'box_enemy_ele' : 'txt-quest-name',
                    'box_enemy_name' : ['Mimic', 'Obsidian Machina']
                    }    ):
        txt = gauge_box_data['box_enemy_name']
        by = By.CLASS_NAME
        ele = gauge_box_data['box_enemy_ele']
        elf = elefinder(by, ele, 1, self.chm)
        if elf.is_element_visibility():
            for t in txt:
                if elf.get_element_text() == t:
                    return True
                else:
                    return False

    def is_goal_page(self, waittime = 5):
        """
        默认waittime = 5 单位秒
        """
        # 判断是否为战斗结算后的exp gain page
        by = self.util.screen_label_battle_goal_exp['by']
        ele = self.util.screen_label_battle_goal_exp['element']
        flag = False 
        elf = elefinder(by, ele, waittime, self.chm)
        if elf.is_element_visibility():
            flag = True
        else:
            if re.match(self.chm.current_url, 'result'):
                flag = True
        return flag
        
    def is_battle_page(self, waittime = 5):
        by = self.util.screen_label_battle_page['by']
        ele = self.util.screen_label_battle_page['element']
        flag = False 
        elf = elefinder(by, ele, waittime, self.chm)
        if elf.is_element_visibility():
            flag = True
        return flag
        

    def is_party_all_dead(self):
        """
        自己的小队全灭，提示提升能力
        """
        flag = False
        by = self.util.screen_label_battle_alldead['by']
        text =  self.util.screen_label_battle_alldead['text']
        ele =  self.util.screen_label_battle_alldead['element']
        elf = elefinder(by, ele, 10, self.chm)
        if elf.is_element_visibility():
            if text ==  elf.get_element_text():
                flag = True
        return flag

    def is_loading_page(self):
        ele = util.loading_page_element['element']
        by = util.loading_page_element['by']
        elf = elefinder(by, ele, 10, self.chm)
        return elf.is_element_visibility()      








