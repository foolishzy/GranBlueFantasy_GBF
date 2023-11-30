from threading import Event
from stage import checker
import time
from loading_page_locator import request_dialog_locator
from loading_page_locator import goal_page_locator
from loading_page_locator import last_turn_locator
from loading_page_locator import lpl 
from mouse import Mouse
from util import util
from stage import checker
from stage import stage
from selenium import webdriver
from elementfinder import elefinder
from threading import Thread
from skill_clicker import party
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
        self.lpl = lpl(self.chm)
        self.party = party(self.chm, self.mouse)
        #在战斗页面初始化party

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
        play_event = Event()
        lst_turn_event = Event()
        goal_page_event = Event()
        request_locator_ctrl_event = Event()
        lst_turn_thread = Thread(
                target = last_turn_locator(self.chm, lst_turn_event, self.mouse).start
                )
        goal_page_thread = Thread(
                target = goal_page_locator(self.chm, goal_page_event,play_event).start
                )
        play_event.set()
        goal_page_event.set()
        lst_turn_event.set()
        lst_turn_thread.start()
        goal_page_thread.start()
        request_locator_ctrl_event.clear()
        while play_event.is_set()  and end_time - start_time < self.btl * 60 :
            end_time = time.time()
            flag = False
            if elefinder(by, ele, 2, self.chm).is_element_presence():
                flag = True
                #  break
            if flag:
                self.stage.refresh()
                req_thread = Thread(
                target = request_dialog_locator(self.mouse, self.chm, request_locator_ctrl_event).start
                )    
                req_thread.start()
                if request_locator_ctrl_event.is_set():
                    req_thread.join()
                print('play_event_set, ', play_event.is_set() )
                if play_event.is_set():
                    self.party.update()
                    self.mouse.click_full()
                else:
                    break
        lst_turn_event.clear()    
        goal_page_event.clear()

    def get_chm(self):
        return self.chm

    def play(self):
        t1 = Thread(target = self.lpl.start )
        t1.start()
        #  t1.join()
                    
