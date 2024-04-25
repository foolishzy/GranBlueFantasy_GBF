from game import game
import time
from alert import alert
from util import util
from elementfinder import elefinder


class btb_select:

    def __exit(self):
        pass

    def __init__(self):
        string_hint = '''
       请选择：
       0. exit
       1. extreme_xuanwu
       2. extreme_zhuque
       3. extreme_baihu
       4. extreme_qinglong
       5. impossible
       6. manic_xuanwu
       7. manic_zhuque
       8. manic_baihu
       9. manic_qinglong
       10. manic_all
       11. extreme_all
       12. extreme_plus_fire
       13. extreme_plus_water
       14. extreme_plus_earth
       15. extreme_plus_wind
       16. extreme_plus_all
       '''
        index_max = 16
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
        elif index == 5:
            impossible().play()
        elif index == 6:
            manic_xuanwu().play()
        elif index == 7:
            manic_zhuque().play()
        elif index == 8:
            manic_baihu().play()
        elif index == 9:
            manic_qinglong().play()
        elif index == 10:
            btb_manic_all().play()
        elif index == 11:
            btb_extreme_all().play()
        elif index == 12:
            btb_extreme_plus_fire().play()
        elif index == 13:
            btb_extreme_plus_water().play()
        elif index == 14:
            btb_extreme_plus_earth().play()
        elif index == 15:
            btb_extreme_plus_wind().play()
        elif index == 16:
            btb_extreme_all().play()


class extreme_battle_of_the_beasts(game):

    # 四象降临活动
    def __init__(self, game_data={
        'url': "",
        'time_limit': ""
    }):
        self.oneturn = False
        btl = game_data['time_limit']
        self.url = game_data['url']
        self.repeat_times = 0
        self.play_all_flag = False
        super().__init__(btl)

    def set_play_all_flag(self):
        self.play_all_flag = True

    def init_repeat_times(self, times=0):
        self.repeat_times = times

    def play(self):
        if not self.play_all_flag:
            i = int(input("""
            100% chargebar and one turn?
            pls selcet:
            1. yes
            2. no
            """
                          ))
        else:
            i = 2
        if i == 1:
            self.oneturn = True
        else:
            self.oneturn = False

        super().play()
        if self.repeat_times == 0:
            repeat_times = int(input('pls input repeat times: '))
        else:
            repeat_times = self.repeat_times

        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print('left times: ', repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                if self.oneturn:
                    self.mouse.click_attack()
                    time.sleep(1)
                    self.chm.refresh()
                else:
                    self.mouse.click_full()
                    self.auto_refresh()
            if self.find_extreme_plus():
                self.play_extreme_plus()
            #  elif self.find_impossible():
                #  self.play_impossible()

        if not self.play_all_flag:
            alert().run()

    def find_impossible(self):
        data = util.btb_impossible
        url = util.btb_event_main_url
        self.stage.goto(url)
        elf = elefinder(data['by'], data['element'], 3, self.chm)
        if elf.is_element_presence():
            if not ('' == self.chm.find_element(
                    data['by'], data['element']).text):
                flag = True
            else:
                flag = False
        return flag

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
            flag = True
        else:
            flag = False
        return flag


class btb_extreme_plus(game):
    game_data = {
        "url": "",
        'time_limit': ""
    }
    # 在实例中初始化game_data

    def __init__(self):
        self.play_all_flag = False
        self.repeat_times = 0
        self.oneturn = False
        btl = self.game_data['time_limit']
        self.url = self.game_data['url']
        super().__init__(btl)

    def init_repeat_times(self, times):
        self.repeat_times = times

    def set_play_all_flag(self):
        self.play_all_flag = True

    def play(self):

        if not self.play_all_flag:
            i = int(input('''100% chargebar and one turn?
                pls select:
                1. yes
                2. no
                '''))
        else:
            i = 2
        if i == 1:
            self.oneturn = True
        else:
            self.oneturn = False

        super().play()
        if self.repeat_times == 0:
            repeat_times = int(input("pls input repeat times: "))
        else:
            repeat_times = self.repeat_times

        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print("left times :", repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                if self.oneturn:
                    self.mouse.click_attack()
                    time.sleep(1)
                    self.chm.refresh()
                else:
                    self.mouse.click_full()
                    self.auto_refresh()
        if not self.play_all_flag:
            alert().run()


class btb_extreme_plus_fire(btb_extreme_plus):
    game_data = util.btb_extreme_plus_fire


class btb_extreme_plus_water(btb_extreme_plus):
    game_data = util.btb_extreme_plus_water


class btb_extreme_plus_earth(btb_extreme_plus):
    game_data = util.btb_extreme_plus_earth


class btb_extreme_plus_wind(btb_extreme_plus):
    game_data = util.btb_extreme_plus_wind


class btb_extreme_plus_all:

    def __init__(self):
        times = int(input('pls input repeat times :'))
        self.play_list = [
            btb_extreme_plus_fire(),
            btb_extreme_plus_water(),
            btb_extreme_plus_earth(),
            btb_extreme_plus_wind()
        ]
        for p in self.play_list:
            p.init_repeat_times(times)
            p.set_play_all_flag()

    def play(self):
        for p in self.play_list:
            p.play()
        alert().run()


class btb_extreme_all:
    def __init__(self):
        times = int(input('pls input repeat times :'))
        self.play_list = [
            extreme_xuanwu(),
            extreme_zhuque(),
            extreme_baihu(),
            extreme_qinglong()
        ]
        for p in self.play_list:
            p.init_repeat_times(times)
            p.set_play_all_flag()

    def play(self):
        for p in self.play_list:
            p.play()
        alert().run()


class btb_manic_all:
    def __init__(self):
        times = int(input('pls input repeat times max 2 :'))
        self.play_list = [manic_xuanwu(),
                          manic_zhuque(),
                          manic_qinglong(),
                          manic_baihu()]
        for p in self.play_list:
            p.init_repeat_times(times)

    def play(self):
        for p in self.play_list:
            p.play()
            p.set_play_all_flag()
        alert().run()


class btb_manic(game):
    game_data = {
        'url': "",
        'time_limit': ""
    }
    # 在实例中初始化game_gata

    def __init__(self):
        print('manic cannot be defeated in one turn/n')
        self.play_all_flag = False
        self.repeat_times = 0
        self.oneturn = False
        btl = self.game_data['time_limit']
        self.url = self.game_data['url']
        super().__init__(btl)

    def init_repeat_times(self, times=0):
        self.repeat_times = times

    def set_play_all_flag(self):
        self.play_all_flag = True

    def play(self):
        if not self.play_all_flag:
            i = int(input("""
            100% chargebar and one turn?
            pls selcet:
            1. yes
            2. no
            """
                          ))
        else:
            i = 2
        if i == 1:
            self.oneturn = True
        else:
            self.oneturn = False

        super().play()
        if self.repeat_times == 0:
            repeat_times = int(input('pls input repeat times (1, 2): '))
        else:
            repeat_times = self.repeat_times
        if repeat_times > 2:
            print('beyond the max times, repeat_times will be set as 2!')
            repeat_times = 2
        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print('left times: ', repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                if self.oneturn:
                    self.mouse.click_attack()
                    time.sleep(1)
                    self.chm.refresh()
                else:
                    self.mouse.click_full()
                    self.auto_refresh()
        if not self.play_all_flag:
            alert().run()


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


class manic_xuanwu(btb_manic):
    game_data = util.btb_manic_xuanwu


class manic_zhuque(btb_manic):
    game_data = util.btb_manic_zhuque


class manic_baihu(btb_manic):
    game_data = util.btb_manic_baihu


class manic_qinglong(btb_manic):
    game_data = util.btb_manic_qinglong


class impossible(extreme_battle_of_the_beasts):
    data = util.btb_impossible

    def __init__(self):
        super().__init__(self.data)
