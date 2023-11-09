from stage import checker
import time
from mouse import Mouse
from util import util
from stage import checker
from stage import stage
from selenium import webdriver
from elementfinder import elefinder
class game:



    def __init__(self, battle_time_limit ):
        # 单场战斗预计最长时间 单位分钟
        self.chm = None
        self.btl = battle_time_limit
        self.util = util
        self.connect_chrome()
        self.stage = stage(self.chm)
        self.mouse = Mouse(self.chm)
        self.ck = checker(self.chm)

    def connect_chrome(self):
        #连接到打开远程调试模式的chrome浏览器
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = self.util.chrome_remote_host
        self.chm = webdriver.Chrome(options=chrome_options)




    def auto_refresh(self):
        """
            战斗页面攻击后自动刷新
        """
        by = self.util.screen_label_auto_refresh['by']
        ele = self.util.screen_label_auto_refresh['element']
        start_time = time.time()
        end_time = time.time()
        ck = checker(self.chm, 2)
        while (not ck.is_goal_page(5)) and end_time - start_time < self.btl * 60 :
            i = 0
            while i < 3:
                i = i + 1
                end_time = time.time()
                flag = False
                if elefinder(by, ele, 2, self.chm).is_element_presence():
                    flag = True
                    break
            if flag:
                self.stage.refresh()
                self.mouse.click_full()
            
    def get_chm(self):
        return self.chm


    def play(self):
        pass
