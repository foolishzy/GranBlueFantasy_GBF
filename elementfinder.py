from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class elefinder:


    def __init__(self, by : By, element, waittime  : int, chm_webdriver : webdriver.chrome):
        self.element = element
        self.chm = chm_webdriver
        self.by = by
        self.waittime = waittime
        pass

    def get_element_text(self):
        text = ''
        if self.is_element_visibility():
            text = self.chm.find_element(self.by, self.element).text
        return text

    def is_element_clickable(self):
        flag = False
        while True :
            try:
                WebDriverWait(self.chm, self.waittime).until(
                        EC.element_to_be_clickable(
                            (self.by, self.element)
                        )
                        )
                flag = True
                break
            except TimeoutException:
                flag = False 
                break
            except WebDriverException:
                pass
        return flag

    def is_element_presence(self):
        flag = False
        waittime = self.waittime
        while True:
            try:
                WebDriverWait(self.chm, waittime).until(
                        EC.presence_of_element_located(
                            (self.by, self.element)
                            )
                        )
                flag = True
                break
             
            except TimeoutException:
                break
            except  WebDriverException:
                break
            except UnexpectedAlertPresentException:
                alert = chm_webdrive.switch_to.alert
                print("alert txt is :", alert)
                alert.accept()
        return flag

    def is_element_visibility(self):
        flag = False
        waittime = self.waittime
        while True:
            try:
                WebDriverWait(self.chm, waittime).until(
                        EC.presence_of_element_located(
                            (self.by, self.element)
                            )
                        )
                WebDriverWait(self.chm, waittime).until(
                        EC.visibility_of_element_located(
                            (self.by, self.element)
                            )
                        )
                flag = True
                break
             
            except TimeoutException:
                break
            except  WebDriverException:
                break
            except UnexpectedAlertPresentException:
                alert = chm_webdrive.switch_to.alert
                print("alert txt is :", alert)
                alert.accept()
        return flag

