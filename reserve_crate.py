from selenium.webdriver.common.keys import Keys
from util import util
from game import game

class reserve_select:
    def __exit(self):
        pass

    def __init__(self):
        string_hint = """
       请选择：
       0. exit
       1. reverse_timelimit_weapon
       2. reverse_timelimit_summon
       3. reverse_no_limit_weapon
       4. reverse_no_limit_summon
        """
        flag = False
        while not flag:
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
            index_range = [[0, 4]]
            for i in index_range:
                if index >= i[0] and index <= i[1]:
                    flag = True
        if index == 0:
            self.exit()
        elif index == 1:
            clear_timelimit_weapon().run()
        elif index == 2:
            clear_timelimit_summon().run()
        elif index == 3:
            clear_no_limit_weapon().run()
        elif index == 4:
            clear_no_limit_summon().run()


class auto_reserve:
    def __init__(self):
        self.weapon_bt_data = util.reserve_weapon_bt_data
        self.summon_bt_data = util.reserve_summon_bt_data
        self.url = util.reserve_page_url
        self.ok_bt = util.reserve_bt_dialog_ok
        self.reserve_bt = util.reserve_bt_dialog_reserve
        self.use_bt = util.reserve_bt_dialog_use
        self.nolimit_bt = util.reserve_bt_nolimit
        self.timelimit_bt = util.reserve_bt_timelimit
        self.game = game(0)
    
    def run(self):
        self.game.stage.goto(self.url, self.timelimit_bt)
        self.game.chm.find_element_by_tag_name('body').send_keys(Keys.HOME)
class clear_timelimit_summon(auto_reserve):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run()
        self.game.mouse.click_by_element(self.timelimit_bt, 5)
        while True:
            self.game.chm.find_element_by_tag_name('body').send_keys(Keys.END)
            self.game.mouse.click_by_element(self.summon_bt_data, 5)
            self.game.mouse.click_by_element(self.reserve_bt, 5)
            if self.game.mouse.click_by_element(self.use_bt, 5):
                self.game.mouse.click_by_element(self.ok_bt, 5)
            else:
                break

class clear_timelimit_weapon(auto_reserve):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run()
        self.game.mouse.click_by_element(self.timelimit_bt, 5)
        while True:
            self.game.chm.find_element_by_tag_name('body').send_keys(Keys.END)
            self.game.mouse.click_by_element(self.weapon_bt_data, 5)
            self.game.mouse.click_by_element(self.reserve_bt, 5)
            if self.game.mouse.click_by_element(self.use_bt, 5):
                self.game.mouse.click_by_element(self.ok_bt, 5)
            else:
                break
class clear_no_limit_summon(auto_reserve):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run()
        self.game.mouse.click_by_element(self.nolimit_bt, 5)
        while True:
            self.game.chm.find_element_by_tag_name('body').send_keys(Keys.END)
            self.game.mouse.click_by_element(self.summon_bt_data, 5)
            self.game.mouse.click_by_element(self.reserve_bt, 5)
            if self.game.mouse.click_by_element(self.use_bt, 5):
                self.game.mouse.click_by_element(self.ok_bt, 5)
            else:
                break

class clear_no_limit_weapon(auto_reserve):
    def __init__(self):
        super().__init__()

    def run(self):
        super().run()
        self.game.mouse.click_by_element(self.nolimit_btt, 5)
        while True:
            self.game.chm.find_element_by_tag_name('body').send_keys(Keys.END)
            self.game.mouse.click_by_element(self.weapon_bt_data, 5)
            self.game.mouse.click_by_element(self.reserve_bt, 5)
            if self.game.mouse.click_by_element(self.use_bt, 5):
                self.game.mouse.click_by_element(self.ok_bt, 5)
            else:
                break



