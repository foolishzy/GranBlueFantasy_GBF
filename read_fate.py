from game import game
from selenium.webdriver.common.by import By
from alert import alert


class fate_select():
    def __init__(self):
        read_fate().play()


class read_fate(game):

    def __init__(self):
        super().__init__(1)
        self.url = "https://game.granbluefantasy.jp/#quest/fate"
        self.alert = alert()

    def play(self):
        times = int(input('input times :'))
        while times > 0:
            times = times - 1
            self.stage.goto(self.url)
            e = {
                'element': '//*[@id="cnt-quest"]/div[4]/div[1]/div[2]/div[1]/div[1]/div[3]',
                'by': By.XPATH
            }
            self.mouse.click_by_element(e, 10)
            e = {
                'element': '//*[@id="wrapper"]/div[3]/div[4]/div[8]',
                'by': By.XPATH
            }
            self.mouse.click_by_element(e, 10)
            e = {
                'element': '//*[@id="pop"]/div/div[3]/div[2]',
                'by': By.XPATH
            }
            self.mouse.click_by_element(e, 10)
            self.ck.is_goal_page(10)
        self.alert.run()
