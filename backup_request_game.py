from alert import alert
from selenium.webdriver.common.by import By
from elementfinder import elefinder
from game import game
import time
from loading_page_locator import rapid_end_locator
from threading import Event
from threading import Thread
from selenium.common.exceptions import NoSuchAttributeException


class select:
    def __init__(self):
        backup_request_game().play()


class backup_request_game(game):

    def __init__(self):
        time_limit = 10
        super().__init__(time_limit)

    def goto_backup_page(self):
        self.url = 'https://game.granbluefantasy.jp/#quest/assist'
        self.stage.goto(self.url)
        # 下面这个xpath是pendinggame的路径，现在不需要判断了，游戏页面调整了
        #  elf = elefinder(
        #  By.XPATH, '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div/div[2]', 5, self.chm)
        #  while True:
        #  if elf.is_element_clickable():
        #  self.chm.find_element_by_xpath(
        #  '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div/div[2]').click()
        #  break
        # 下面这个是救援页面上的刷新按钮
        by = By.XPATH
        element = '//*[@id="prt-assist-search"]/div[2]/div[2]'
        while(self.if_no_target()):
            if elefinder(by, element, 3, self.chm).is_element_clickable():
                self.chm.find_element_by_xpath(element).click()
                time.sleep(1)

            # 判断是否有救援没有就刷新

    def click_max_progress(self):
        elf = elefinder(By.CLASS_NAME, 'prt-raid-gauge-inner', 5,  self.chm)
        result = None
        if elf.is_element_presence():
            e = self.chm.find_elements_by_class_name('prt-raid-gauge-inner')
            temp = 0
            index = -1
            for ee in e:
                index = index + 1
                wide = float(ee.value_of_css_property(
                    "width").replace("px", "").replace("%", ""))
                if wide > temp:
                    result = ee
                    temp = wide
                    result_index = index
            flag = True
            while flag:
                try:
                    xpath = ".//*[@class='" + \
                            result.get_attribute('class') + "']/.."
                    result = self.chm.find_elements_by_xpath(xpath)[
                        result_index]
                    flag = not (result.get_attribute('class') ==
                                'btn-multi-raid lis-raid search')
                except NoSuchAttributeException:
                    result = None
                    break
        return result

    def play(self):
        repeat_times = int(input("pls input repeat times :"))
# 监视进程
        rapid_end_start_event = Event()
        rapid_end_ctrl_event = Event()
        rapid_end_thread = Thread(
            target=rapid_end_locator, args=(
                self.mouse, self.chm, rapid_end_ctrl_event,
                rapid_end_start_event
            )
        )
        rapid_end_thread.start()
        while repeat_times > 0:
            print("while loop start")
            repeat_times = repeat_times - 1
            print("left times : ", repeat_times)
            self.goto_backup_page()
            while True:
                elf = elefinder(By.CLASS_NAME, 'txt-popup-body', 5, self.chm)
                e = self.click_max_progress()
                if e:
                    e.click()
                else:
                    break
                if not elf.is_element_presence():
                    break
                else:
                    self.stage.refresh()
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            rapid_end_start_event.set()
            print('rapid_end_ctrl_event = ', rapid_end_ctrl_event)
            print('not rapid_end_ctrl_event.is_set() = ',
                  (not rapid_end_ctrl_event.is_set()))
            if (not rapid_end_ctrl_event.is_set()):
                self.mouse.click_full()
                self.auto_refresh()
                super().play()
            rapid_end_ctrl_event.clear()
            rapid_end_start_event.clear()
        alert().run()

    def if_no_target(self):
        notarget = self.util.screen_label_rapid_assit_no_target
        elf = elefinder(notarget['by'], notarget['element'], 2, self.chm)
        if elf.is_element_presence():
            print("no target, refreshing...")
            return True
        else:
            print("find target")
            return False
