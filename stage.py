from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import UnexpectedAlertPresentException
from util import util
from elementfinder import elefinder
from selenium.webdriver.common.by import By
import re
import time

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

    def check_gauge(self, gauge_url):
# 这里的判断好像没有能够通用的 不同线路出现的宝箱怪和宝箱是不一样的text element 要针对不同的怪物分布写 下面的mimic也是 不是所有的宝箱怪都叫做micmic
        selector = util.screen_label_arcum_gauge_goto_url
        self.stage.goto(gauge_url, selector)
        by = self.util.screen_label_arcum_gauge['by']
        ele = self.util.screen_label_arcum_gauge['element']
        elf = elefinder(by, ele, 2, self.chm)
        if elf.is_element_visibility():
            return True
        else:
            return False

    def check_gauge_mimic(self):
        text = self.util.screen_label_arcum_gauge_mimic['text']
        by = self.util.screen_label_arcum_gauge_mimic['by']
        ele = self.util.screen_label_arcum_gauge_mimic['element']
        elf = elefinder(by, ele, 2, self.chm)
        if elf.is_element_visibility():
            if elf.get_element_text() == text : 
                return True
            else:
                return False


    def is_goal_page(self, waittime = 10):
        """
        默认waittime = 10 单位秒
        """
        # 判断是否为战斗结算后的exp gain page
        by = self.util.screen_label_battle_goal_exp['by']
        ele = self.util.screen_label_battle_goal_exp['element']
        flag = False 
        elf = elefinder(by, ele, 10, self.chm)
        if elf.is_element_visibility():
            flag = True
        else:
            if re.match(self.chm.current_url, 'result'):
                flag = True
        return flag
        
    def is_battle_page(self):
        by = self.util.screen_label_battle_page['by']
        ele = self.util.screen_label_battle_page['element']
        flag = False 
        elf = elefinder(by, ele, 10, self.chm)
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


