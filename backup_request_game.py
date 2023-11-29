from alert import alert
from selenium.webdriver.common.by import By
from elementfinder import elefinder 
from game import game
class select:
    def __init__(self):
        backup_request_game().play()

class backup_request_game(game):

    def __init__(self):
        time_limit = 10
        super().__init__(time_limit)
    

    def goto_backup_page(self):
        self.url = 'https://game.granbluefantasy.jp/#quest/multi/0'
        self.stage.goto(self.url)
        elf = elefinder(By.XPATH, '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div/div[2]', 5, self.chm)
        while True:
            if elf.is_element_clickable():
                self.chm.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div/div[2]').click()
                break

    def click_max_progress(self):
        e = self.chm.find_elements_by_class_name('prt-raid-gauge-inner')
        temp = 0
        index = -1
        for ee in e:
            index = index + 1
            wide = float(ee.value_of_css_property("width").replace("px", ""))
            if wide > temp:
                result = ee
                temp = wide
                result_index  = index
        flag = True
        while flag : 
            xpath = ".//*[@class='" + result.get_attribute('class') + "']/.."
            result = self.chm.find_elements_by_xpath(xpath)[result_index]
            flag = not ( result.get_attribute('class') == 'btn-multi-raid lis-raid search')
        return result
    
    def play(self):
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            print("while loop start")
            repeat_times = repeat_times - 1
            print("left times : ", repeat_times)
            self.goto_backup_page()
            while True:
                elf = elefinder(By.CLASS_NAME, 'txt-popup-body', 5, self.chm)
                self.click_max_progress().click()
                if not elf.is_element_presence():
                    break
                else:
                    self.stage.refresh()
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            self.mouse.click_full()
            self.auto_refresh()
            super().play()
        alert.run()


