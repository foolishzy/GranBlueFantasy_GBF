from game import game
from timer import timer
from util import util
import time


class event_select:
    """event_select."""

    def __exit(self):

        pass

    def __init__(self):
        string_hint = '''
        请选择：
        0.退出
        1.hope_from_a_snow_drop
        2.Detective Barawa...
        3.exo_ifrit_crucible...
        4.the divine generals...
        5.ultimate showndown
        '''

        index_max = 5
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            hope_from_a_snow_drop().play()
        elif index == 2:
            detective_barawa().play()
        elif index == 3:
            exo_ifrit_crucible().play()
        elif index == 4:
            divine_generals().play()
        elif index == 5:
            ultimate_showndowns().play()


class event_common(game):

    def __init__(self,
                 game_data={'url': "", 'time_limit': 10
                            }
                 ):
        self.url = game_data['url']
        super().__init__(
            game_data['time_limit']
        )
        pass


class ultimate_showndowns(event_common):
    """
    20231225
    """
    tuna_lover_extreme_data = util.tuna_lover_extreme_data
    salmun_lover_extreme_data = util.salmun_lover_extreme_data

    tuna_golem_data = util.tuna_golem_data
    salmun_golem_data = util.salmun_golem_data

    game_data = tuna_lover_extreme_data

    def __exit(self):
        pass

    def __init__(self):
        super().__init__(self.game_data)

    def __play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        my_timer = timer()
        while times > 0:
            my_timer.start()
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            # 打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.mouse.click_attack()
                time.sleep(5)
                self.chm.refresh()
                time.sleep(8)
            my_timer.end()

    def golem_play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        my_timer = timer()
        while times > 0:
            my_timer.start()
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            # 打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()
            my_timer.end()

    def play_tuna_golem(self):
        self.game_data = self.tuna_golem_data
        self.__init__()
        self.golem_play()

    def play_salmun_golem(self):
        self.game_data = self.salmun_golem_data
        self.__init__()
        self.golem_play()

    def play_tuna_extreme(self):
        self.game_data = self.tuna_lover_extreme_data
        self.__init__()
        self.__play()

    def play_salmun_extreme(self):
        self.game_data = self.salmun_lover_extreme_data
        self.__init__()
        self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.tuna_extreme
        2.salmun_extreme
        3.tuna_golem
        4.salmun_golem
        """

        index = -1
        index_max = 4
        index_min = 0
        while (not (index >= index_min and index <= index_max)):

            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            self.play_tuna_extreme()
        elif index == 2:
            self.play_salmun_extreme()
        elif index == 3:
            self.play_tuna_golem()
        elif index == 4:
            self.play_salmun_golem()


class divine_generals(event_common):
    """
    20231220
    """
    solo_extreme_data = util.divine_generals_solo_extreme
    rapid_extreme_data = util.divine_generals_rapid_extreme
    game_data = solo_extreme_data

    def __exit(self):
        pass

    def __init__(self):
        super().__init__(self.game_data)

    def __play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        my_timer = timer()
        while times > 0:
            my_timer.start()
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            # 打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()
            my_timer.end()

    def play_rapid_extreme(self):
        self.game_data = self.rapid_extreme_data
        self.__init__()
        self.__play()

    def play_solo_extreme(self):
        self.game_data = self.solo_extreme_data
        self.__init__()
        self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.solo_extreme
        2.rapid_extreme
        """
        index = -1
        index_max = 2
        index_min = 0
        while (not (index >= index_min and index <= index_max)):

            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            self.play_solo_extreme()
        elif index == 2:
            self.play_rapid_extreme()


class exo_ifrit_crucible(event_common):
    """
    20231207
    """
    veryhard_data = util.exo_ifrit_veryhard
    extreme_data = util.exo_ifrit_extreme
    game_data = extreme_data
    crucible_data = util.exo_ifrit_crucible

    def __exit(self):
        pass

    def __init__(self):
        super().__init__(self.game_data)

    def __play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        while times > 0:
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            # 打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()

    def play_crucible(self):
        self.game_data = self.crucible_data
        self.__init__()
        self.__play()

    def play_veryhard(self):
        self.game_data = self.veryhard_data
        self.__init__()
        self.__play()

    def play_extreme(self):
        self.game_data = self.extreme_data
        self.__init__()
        self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.veryhard
        2.extrem
        3.crucible
        """
        index = -1
        index_max = 3
        index_min = 0
        while (not (index >= index_min and index <= index_max)):

            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            self.play_veryhard()
        elif index == 2:
            self.play_extreme()
        elif index == 3:
            self.play_crucible()


class detective_barawa(event_common):
    '''
    20231128
    '''
    veryhard_data = util.Detective_Barawa_very_hard
    impossible_data = util.Detective_Barawa_impossible
    extreme_data = util.Detective_Barawa_extreme
    game_data = impossible_data
    nightmare_data = util.Detective_solo_Nightmare

    def __exit(self):
        pass

    def play(self):
        string_hint = '''
        \n
        0.exit
        1.veryhard
        2.extreme
        3.impossible
        4.solo night mare
        '''
        index = -1
        index_max = 4
        index_min = 0
        while (not (index >= index_min and index <= index_max)):

            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            self.play_veryhard()
        elif index == 2:
            self.play_extreme()
        elif index == 3:
            self.play_impossible()
        elif index == 4:
            self.play_nightmare()

    def __init__(self):
        super().__init__(self.game_data)

    def play_veryhard(self):
        self.game_data = self.veryhard_data
        self.__init__()
        self.__play()

    def play_nightmare(self):
        self.game_data = self.nightmare_data
        self.__init__()
        self.__play()

    def play_extreme(self):
        self.game_data = self.extreme_data
        self.__init__()
        self.__play()

    def play_impossible(self):
        self.game_data = self.impossible_data
        self.__init__()
        self.__play()

    def __play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        while times > 0:
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            # 打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()


class hope_from_a_snow_drop(event_common):
    '''
    20231104测试可以跑通
    '''
    veryhard_data = util.hope_from_a_snow_drop_veryhard
    impossible_data = util.hope_from_a_snow_drop_impossible
    extreme_data = util.hope_from_a_snow_drop_extreme
    game_data = impossible_data

    def __exit(self):
        pass

    def play(self):
        string_hint = '''
        \n
        0.exit
        1.veryhard
        2.extreme
        3.impossible
        '''
        index = -1
        index_max = 3
        index_min = 0
        while (not (index >= index_min and index <= index_max)):

            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            self.play_veryhard()
        elif index == 2:
            self.play_extreme()
        elif index == 3:
            self.play_impossible()

    def __init__(self):
        super().__init__(self.game_data)

    def play_veryhard(self):
        self.game_data = self.veryhard_data
        self.__init__()
        self.__play()

    def play_extreme(self):
        self.game_data = self.extreme_data
        self.__init__()
        self.__play()

    def play_impossible(self):
        self.game_data = self.impossible_data
        self.__init__()
        self.__play()

    def __play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        while times > 0:
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            # 打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()
