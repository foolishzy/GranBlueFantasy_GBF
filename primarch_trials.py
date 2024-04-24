from game import game
from util import util
import time
from alert import alert


class primarch_select:
    def __exit(self):
        pass

    def __init__(self):
        string_hint = '''
       请选择：
       0. exit
       1. extreme_fire
       2. extreme_water
       3. extreme_wind
       4. extreme_earth
       5. extreme_plus_fire
       6. extreme_plus_wind
       7. extreme_plus_earth
       8. extreme_plus_water
       9. standard_fire
       10. standard_water
       11. standard_wind
       12. standard_earth
       13. extreme_all
       14. extreme_plus_all
       15. standard_all
       '''
        index_max = 15
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
            extreme_fire().play()
        elif index == 2:
            extreme_water().play()
        elif index == 3:
            extreme_wind().play()
        elif index == 4:
            extreme_earth().play()
        elif index == 5:
            extreme_plus_fire().play()
        elif index == 6:
            extreme_plus_wind().play()
        elif index == 7:
            extreme_plus_earth().play()
        elif index == 8:
            extreme_plus_water().play()
        elif index == 9:
            standard_fire().play()
        elif index == 10:
            standard_water().play()
        elif index == 11:
            standard_wind().play()
        elif index == 12:
            standard_earth().play()
        elif index == 13:
            extreme_all().play()
        elif index == 14:
            extreme_plus_all().play()
        elif index == 15:
            standard_all().play()


class game_all:
    game_list = []

    def __init__(self):
        times = int(input('pls input repeat times: '))
        for g in self.game_list:
            g.init_repeat_times(times)
            g.set_play_all_flag()

    def play(self):
        for g in self.game_list:
            g.play()
        alert().run()


class extreme_all(game_all):
    def __init__(self):

        self.game_list = [
            extreme_fire(),
            extreme_wind(),
            extreme_water(),
            extreme_earth()
        ]
        super().__init__()


class extreme_plus_all(game_all):
    def __init__(self):
        self.game_list = [
            extreme_plus_fire(),
            extreme_plus_wind(),
            extreme_plus_earth(),
            extreme_plus_wind()
        ]
        super().__init__()


class standard_all(game_all):
    def __init__(self):
        self.game_list = [
            standard_fire(),
            standard_water(),
            standard_earth(),
            standard_wind()
        ]
        super().__init__()


class primarch_common(game):
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


class standard_game(primarch_common):
    def __init__(self):
        super().__init__()


class extreme_game(primarch_common):
    def __init__(self):
        super().__init__()


class extreme_plus_game(primarch_common):
    def __init__(self):
        super().__init__()


class extreme_plus_fire(extreme_plus_game):
    game_data = util.primarch_trials_extreme_plus_fire


class extreme_plus_water(extreme_plus_game):
    game_data = util.primarch_trials_extreme_plus_water


class extreme_plus_wind(extreme_plus_game):
    game_data = util.primarch_trials_extreme_plus_wind


class extreme_plus_earth(extreme_plus_game):
    game_data = util.primarch_trials_extreme_plus_earth


class extreme_fire(extreme_game):
    game_data = util.primarch_trials_extreme_fire


class extreme_water(extreme_game):
    game_data = util.primarch_trials_extreme_water


class extreme_wind(extreme_game):
    game_data = util.primarch_trials_extreme_wind


class extreme_earth(extreme_game):
    game_data = util.primarch_trials_extreme_earth


class standard_fire(standard_game):
    game_data = util.standard_trials_fire


class standard_water(standard_game):
    game_data = util.standard_trials_water


class standard_earth(standard_game):
    game_data = util.standard_trials_earth


class standard_wind(standard_game):
    game_data = util.standard_trials_wind
