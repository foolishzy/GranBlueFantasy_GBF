from selenium.webdriver.common.by import By
from game import game
from util import util
from elementfinder import elefinder 
from alert import alert 

class uf_game(game):
    def __init__(self, data = {
        'url' : '',
        'time_limit' : 1
        }):
        time_limit = data['time_limit']
        self.url = data['url']
        super().__init__(time_limit)
    
    def play(self):
        # one turn 
        i = int(input("""
        100% chargebar and one turn?
        pls selcet:
        1. yes
        2. no
        """
        ))
        if i == 1:
            self.oneturn = True
        else:
            self.oneturn = False
        # end one turn
        super().play()
        by = self.util.screen_label_auto_refresh['by']
        ele = self.util.screen_label_auto_refresh['element']
        repeat_times = int(input('pls input repeat times: '))
        while repeat_times > 0 :
            print('while loop start')
            repeat_times = repeat_times - 1
            self.stage.goto(self.url)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page(10):
                if elefinder(By.CLASS_NAME, 'btn-usual-cancel', 5, self.chm):
                    self.mouse.click_request_cancel()
                if self.oneturn:
                    self.mouse.click_full()
                    if  elefinder(by, ele, 30, self.chm).is_element_presence():
                        self.stage.refresh()
                else:
                    self.mouse.click_full()
                    self.auto_refresh()
        alert().run()

class solo_battle_normal(uf_game):
    def __init__(self):
        data = util.uf_solo_normal
        super().__init__(data)

class solo_battle_hard(uf_game):
    def __init__(self):
        data = util.uf_solo_hard
        super().__init__(data)

class solo_battle_veryhard(uf_game):
    def __init__(self):
        data = util.uf_solo_veryhard
        super().__init__(data)

class rapid_extreme(uf_game):
    def __init__(self):
        data = util.uf_rapid_extreme
        super().__init__(data)

class rapid_extreme_plus(uf_game):
    def __init__(self):
        data = util.uf_rapid_extreme_plus
        super().__init__(data)

class rapid_nightmare(uf_game):
    def __init__(self):
        data = util.uf_rapid_nightmare
        super().__init__(data)

class unite_and_fight_select:
    def __exit(self):
        pass
    
    def __init__(self):
        string_hint = """
        请选择：
        0.退出
        1.solo_battle_normal
        2.solo_battle_hard
        3.solo_battle_veryhard
        4.rapid_battle_extreme
        5.rapid_battle_extremeplus
        6.rapid_battle_nightmare_diffculty
        """
        flag = False
        while not flag:
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
            index_range = [[0, 6]]
            for i in index_range:
                if index >= i[0] and index <= i[1]:
                    flag = True
        if index == 0:
            self.exit()
        elif index == 1:
            solo_battle_normal().play()
        elif index == 2:
            solo_battle_hard().play()
        elif index == 3:
            solo_battle_veryhard().play()
        elif index == 4:
            rapid_extreme().play()
        elif index == 5:
            rapid_extreme_plus().play()
        elif index == 6:
            rapid_nightmare().play()





