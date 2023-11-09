from elementfinder import elefinder 
from util import util
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


