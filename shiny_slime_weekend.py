from stage import checker
from game import game
from util import util
from alert import alert


class slime_select:

    def exit(self):
        pass

    def __init__(self):
        string_hint = '''
       请选择：
       0. exit
       1. shiny_slime_weekend
       2. shiny_slime_week 
        '''
        index_max = 2
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
        if index == 0:
            self.exit()
        elif index == 1:
            shiny_slime_weekend().play()
        elif index == 2:
            shiny_slime_week().play()


class shiny_slime_weekend(game):

    def __init__(self):
        game_data = util.shiny_slime_weekend
        self.url = game_data['url']
        time_limit = game_data['time_limit']
        super().__init__(time_limit)

    def play(self):
        super().play()
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print('left times : ', repeat_times)
            self.stage.goto(self.url, util.screen_label_friend_summmon_page)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
            self.ck.is_goal_page(180)
            self.ck.check_exp_gained_info()
        alert().run()


class shiny_slime_week(game):
    def __init__(self):
        game_data = util.shiny_slime_week
        self.url = game_data['url']
        time_limit = game_data['time_limit']
        super().__init__(time_limit)

    def play(self):
        super().play()
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print('left times : ', repeat_times)
            self.stage.goto(self.url, util.screen_label_friend_summmon_page)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
            self.ck.is_goal_page(180)
            self.ck.check_exp_gained_info()
        alert().run()
