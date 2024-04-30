from game import game
from util import util
from alert import alert


class common_game(game):
    def __init__(self, name="", game_data={"url": "", "time_limit": 0}):
        data = game_data
        self.url = data['url']
        self.name = name
        self.three_times_flag = False
        super().__init__(data['time_limit'])

    def play(self):
        super().play()
        self.stage.goto(self.url)
        self.mouse.click_friend_summon()
        self.mouse.click_party_ok()
        if not self.ck.check_net_work_error():
            if self.ck.is_battle_page():
                self.mouse.click_request_backup()
                self.mouse.click_full()
                self.auto_refresh()
        else:
            pass
        alert().run()


class liejin_select:
    def exit(self):
        pass

    def __init__(self):
        string_hint = """
        请选择
        0. exit
        1. wings_of_terror_impossible 
        2. omen_of_the_broken_skies
        3. the_peacemakers_wings
        4. all_play
        """
        pass
        flag = False
        index_range = [[0, 4]]
        while not flag:
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
            for i in index_range:
                if index >= i[0] and index <= i[1]:
                    flag = True

        if index == 0:
            self.exit()
        elif index == 1:
            wings_of_terror_impossible().play()
        elif index == 2:
            omen_of_the_broken_skies().play()
        elif index == 3:
            the_peacemakers_wings().play()
        elif index == 4:
            all_play().play()


class wings_of_terror_impossible(common_game):
    def __init__(self):
        super().__init__("wings_of_terror_impossible",
                         util.wings_of_terror_data)


class omen_of_the_broken_skies(common_game):
    def __init__(self):
        super().__init__("omen_of_the_broken_skies",
                         util.omen_of_the_broken_skies)


class the_peacemakers_wings(common_game):
    def __init__(self):
        super().__init__("the_peacemakers_wings",
                         util.the_peacemakers_wings)


class all_play:
    def play(self):
        wings_of_terror_impossible().play()
        omen_of_the_broken_skies().play()
        the_peacemakers_wings().play()
