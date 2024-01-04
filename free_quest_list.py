from game import game
from alert import alert

from util import util


class free_quest_list_select:
    def exit(self):
        pass

    def __init__(self):

        string_hint = """
        请选择
        0. exit
        1. two_star_twin_elements_showdowns 
        """
        pass
        flag = False
        index_range = [[0, 1]]
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
            two_star_twin_elements_showdowns().play()


class world_treasure_quest(game):
    def __init__(self, game_data={'utl': "", "time_limit": 1}):
        btl = game_data['time_limit']
        self.url = game_data['url']
        super().__init__(btl)

    def play(self):
        super().play()
        flag = True
        repeat_times = 0
        while flag and (repeat_times <= 0):
            try:
                repeat_times = int(input("pls input repeat times :"))
            except KeyboardInterrupt:
                repeat_times = 0
                flag = False
                break
        while repeat_times > 0:
            print("while loop start")
            repeat_times = repeat_times - 1
            print("left times : ", repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()
        alert().run()


class two_star_twin_elements_showdowns(world_treasure_quest):
    def __init__(self):
        self.game_data = util.free_quest_list_twin_element_showndowns
        super().__init__(self.game_data)

    def play(self):
        super().play()


class pride_of_the_ascendant(game):
    def __init__(self):
        pass
