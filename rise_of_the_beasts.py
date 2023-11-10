from game import game
from alert import alert
from util import util 
from elementfinder import elefinder 
class btb_select:

    def __exit():
        pass

    def __init__(self):
        string_hint = '''
       请选择：
       0. exit
       1. extreme_xuanwu 
       2. extreme_zhuque
       3. extreme_baihu
       4. extreme_qinglong
        '''
        index_max = 18 
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            extreme_xuanwu().play()
        elif index == 2:
            extreme_zhuque().play()
        elif index == 3:
            extreme_baihu().play()
        elif index == 4:
            extreme_qinglong().play()

class extreme_battle_of_the_beasts(game):

# 四象降临活动
    def __init__(self, game_data = {
        'url' : "",
        'time_limit' : ""
        }):
        btl = game_data['time_limit']
        self.url = game_data['url']
        super().__init__(btl)
   
    def play(self):
        super().play()
        repeat_times = int(input('pls input repeat times: '))
        while repeat_times > 0 :
            repeat_times = repeat_times - 1
            print('left times: ', repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()
            if self.find_extreme_plus():
                self.play_extreme_plus()
            elif self.find_impossible():
                self.play_impossible()
        alert().run()
    
    def find_impossible(self):
        data = util.btb_impossible
        url = util.btb_event_main_url
        self.stage.goto(url)
        elf = elefinder(data['by'], data['element'], 3, self.chm)
        if elf.is_element_presence():
            if not ( '' == self.chm.find_element(data['by'], data['element']).text) :
                return True
        else:
            return False

    def play_impossible(self):
        data = util.btb_impossible
        ele = self.chm.find_element(data['by'], data['element'])
        ele.click()
        ipg = game(data['time_limit'])
        ipg.mouse.click_friend_summon()
        ipg.mouse.click_party_ok()
        if ipg.ck.is_battle_page():
            ipg.mouse.click_full()
            ipg.auto_refresh()

    def play_extreme_plus(self):
        data = util.btb_extreme_plus 
        ele = self.chm.find_element(data['by'], data['element'])
        ele.click()
        exg = game(data['time_limit'])
        exg.mouse.click_friend_summon()
        exg.mouse.click_party_ok()
        if exg.ck.is_battle_page():
            exg.mouse.click_full()
            exg.auto_refresh()


    def find_extreme_plus(self):
        url = util.btb_event_main_url
        self.stage.goto(url)
        data = util.btb_extreme_plus 
        elf = elefinder(data['by'], data['element'], 3, self.chm)
        if elf.is_element_presence():
            return True
        else:
            return False





class extreme_xuanwu(extreme_battle_of_the_beasts):
    data = util.btb_extreme_xuanwu
    
    def __init__(self):
        super().__init__(self.data)

class extreme_qinglong(extreme_battle_of_the_beasts):
    data = util.btb_extreme_qinglong
    
    def __init__(self):
        super().__init__(self.data)

class extreme_baihu(extreme_battle_of_the_beasts):
    data = util.btb_extreme_baihu
    
    def __init__(self):
        super().__init__(self.data)

class extreme_zhuque(extreme_battle_of_the_beasts):
    data = util.btb_extreme_zhuque
    
    def __init__(self):
        super().__init__(self.data)

