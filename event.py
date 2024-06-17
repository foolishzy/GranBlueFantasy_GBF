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
        6.tyras bizarre misadventure
        7.dreamer's miracle
        8.dread barrage
        9.exo_corow crucible
        10.heart of the sun
        11.paliuli
        12.our style and our substance
        13.falseto_in_the_autumn_gray
        14.exo_diablo_crucible
        15.samurai_trials
        16.and you
        '''

        index_max = 16
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
        elif index == 6:
            tyras_bizarre_misadventure().play()
        elif index == 7:
            dreamers_mirecle().play()
        elif index == 8:
            dread_barrage().play()
        elif index == 9:
            exo_corow_crucible().play()
        elif index == 10:
            heart_of_the_sun().play()
        elif index == 11:
            paliuli().play()
        elif index == 12:
            our_style_our_substance().play()
        elif index == 13:
            event_falseto_in_the_autumn_gray().play()
        elif index == 14:
            exo_diablo_crucible().play()
        elif index == 15:
            samurai_trials().play()
        elif index == 16:
            andyou().play()


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


class andyou(event_common):
    """20240617"""
    "这里每次and you 活动复刻的时候url可能会不一样"
    game_data = util.event_and_you_girl_in_the_sea_of_tears_impossible

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

    def play(self):
        string_hint = """
        0.exit
        1.girl in the sea of tears
        2.sword saint in the sea of stars
        3.orologia
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
            self.play_girl()
        elif index == 2:
            self.play_sword()
        elif index == 3:
            self.play_orologia()

    def play_girl(self):
        self.game_data = util.event_and_you_girl_in_the_sea_of_tears_impossible
        self.__init__()
        self.__play()

    def play_sword(self):
        self.game_data = util.event_and_you_sword_saint_in_the_sea_of_tears_impossible
        self.__init__()
        self.__play()

    def play_orologia(self):
        self.game_data = util.event_and_you_orologia_impossible
        self.__init__()
        self.__play()


class samurai_trials(event_common):
    """
    20240530
    """
    game_data = util.event_samurai_trials_impossible

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

    def play_impossible(self):
        self.game_data = util.event_samurai_trials_impossible
        self.__init__()
        self.__play()

    def play_raid_extreme(self):
        pass
        #  self.game_data = self.raid_extreme_data
        #  self.__init__()
        #  self.__play()

    def play_solo_extreme(self):
        pass
        #  self.game_data = self.solo_extreme_data
        #  self.__init__()
        #  self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.impossible
        """
        index = -1
        index_max = 1
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
            self.play_impossible()


class our_style_our_substance(event_common):
    """
    20240430
    """
    game_data = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/918141/1/0/10536",
        "time_limit": 1
    }

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

    def play_impossible(self):
        self.game_data = {
            'url': "https://game.granbluefantasy.jp/#quest/supporter/918141/1/0/10536",
            "time_limit": 1
        }
        self.__init__()
        self.__play()

    def play_raid_extreme(self):
        pass
        #  self.game_data = self.raid_extreme_data
        #  self.__init__()
        #  self.__play()

    def play_solo_extreme(self):
        pass
        #  self.game_data = self.solo_extreme_data
        #  self.__init__()
        #  self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.impossible
        """
        index = -1
        index_max = 1
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
            self.play_impossible()


class event_falseto_in_the_autumn_gray(event_common):
    """20240515"""
    solo_veryhard_data = util.event_falseto_in_the_autumn_gray_solo_very_hard
    solo_extreme_data = util.event_falseto_in_the_autumn_gray_solo_extreme
    solo_mannic = util.event_falseto_in_the_autumn_gray_solo_mannic

    rapid_veryhard = util.event_falseto_in_the_autumn_gray_rapid_veryhard
    rapid_ex = util.event_falseto_in_the_autumn_gray_rapid_ex

    game_data = rapid_ex

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

    def play_rapid_veryhard(self):
        self.game_data = self.rapid_veryhard
        self.__init__()
        self.__play()

    def play_rapid_ex(self):
        self.game_data = self.rapid_ex
        self.__init__()
        #  self.__play()
        # 直接扔召唤石然后刷新
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
                time.sleep(0.5)
                self.stage.goto(self.url)
            time.sleep(1)

            my_timer.end()

    def play_solo_mannic(self):
        self.game_data = self.solo_mannic
        self.__init__()
        self.__play()

    def play_solo_veryhard(self):
        self.game_data = self.solo_veryhard_data
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
        2.solo_veryhard
        3.solo_mannic
        4.rapid_veryhard
        5.rapid_ex
        """
        index = -1
        index_max = 5
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
            self.play_solo_veryhard()
        elif index == 3:
            self.play_solo_mannic()
        elif index == 4:
            self.play_rapid_veryhard()
        elif index == 5:
            self.play_rapid_ex()


class paliuli(event_common):
    """
    20240416
    """
    solo_extreme_data = util.event_paliulipararaiha_solo_extreme_data
    raid_extreme_data = util.event_paliulipararaiha_raid_extreme_data
    game_data = raid_extreme_data

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

    def play_raid_extreme(self):
        self.game_data = self.raid_extreme_data
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
        2.raid_extreme
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
            self.play_raid_extreme()


class dreamers_mirecle(event_common):
    """
    20240130
    """
    solo_veryhard_data = util.dreamers_mirecle_solo_very_hard
    solo_extreme_data = util.dreamers_mirecle_solo_extreme
    solo_impossible_data = util.dreamers_mirecle_solo_impossible

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

    def play_solo_impossible(self):
        self.game_data = self.solo_impossible_data
        self.__init__()
        self.__play()

    def play_solo_extreme(self):
        self.game_data = self.solo_extreme_data
        self.__init__()
        self.__play()

    def play_solo_veryhard(self):
        self.game_data = self.solo_veryhard_data
        self.__init__()
        self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.solo_extreme
        2.solo_veryhard
        3.solo_impossible
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
            self.play_solo_extreme()
        elif index == 2:
            self.play_solo_veryhard()
        elif index == 3:
            self.play_solo_impossible()


class tyras_bizarre_misadventure(event_common):
    """
    20231228
    """
    impossible_data = util.tyras_blizza_misadventure_impossible
    game_data = impossible_data

    def __init__(self):
        super().__init__(self.game_data)

    def __exit(self):
        pass

    def play(self):
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


class dread_barrage(event_common):
    """
    20240217
    """
    data_one = util.dread_barrage_one_star_data
    data_two = util.dread_barrage_two_star_data
    data_three = util.dread_barrage_three_star_data
    data_four = util.dread_barrage_four_star_data
    data_five = util.dread_barrage_five_star_data
    data_six = util.dread_barrage_six_star_data
    data_fluke_skywalker = util.dread_barrage_fluke_skywalker_data
    game_data = data_four

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

    def one_star(self):
        self.game_data = self.data_one
        self.__init__()
        self.__play()

    def two_start(self):
        self.game_data = self.data_two
        self.__init__()
        self.__play()

    def three_start(self):
        self.game_data = self.data_two
        self.__init__()
        self.__play()

    def four_start(self):
        self.game_data = self.data_two
        self.__init__()
        self.__play()

    def five_start(self):
        self.game_data = self.data_two
        self.__init__()
        self.__play()

    def six_start(self):
        self.game_data = self.data_two
        self.__init__()
        self.__play()

    def skywalker(self):
        self.game_data = self.data_fluke_skywalker
        self.__init__()
        self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.one
        2.two
        3.three
        4.four
        5.five
        6.six
        7.skywalker
        """
        index = -1
        index_max = 7
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
            self.one_star()
        elif index == 2:
            self.two_start()
        elif index == 3:
            self.three_start()
        elif index == 4:
            self.four_start()
        elif index == 5:
            self.five_start()
        elif index == 6:
            self.six_start()
        elif index == 7:
            self.skywalker()


class heart_of_the_sun(event_common):
    """
    20240318
    """
    pround_turbulent_skies = util.heart_of_the_sun_turbulent_skies
    pround_cycle_of_torment = util.heart_of_the_sun_cycle_of_torment_data
    raids_abramelin_impossible_data = util.heart_of_the_sun_raids_abramelin_impossible_data
    raids_tiamat_aura_omega_data = util.heart_of_the_sun_raids_timat_aura_omega_impossible_data
    raids_phoniex_data = util.heart_of_the_sun_raids_phoniex_impossible_data
    game_data = raids_abramelin_impossible_data

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

    def play_pround_cycle(self):
        self.game_data = self.play_pround_cycle
        self.__init__()
        self.__play()

    def play_pround_turbulent(self):
        self.game_data = self.pround_turbulent_skies
        self.__init__()
        self.__play()

    def play_impossible_phoniex(self):
        self.game_data = self.raids_phoniex_data
        self.__init__()
        self.__play()

    def play_impossible_tiamat(self):
        self.game_data = self.raids_tiamat_aura_omega_data
        self.__init__()
        self.__play()

    def play_impossible_abramelin(self):
        self.game_data = self.raids_abramelin_impossible_data
        self.__init__()
        self.__play()

    def play_pround_cycle(self):
        self.game_data = self.pround_cycle_of_torment
        self.__init__()
        self.__play()

    def play_pround_turbulent(self):
        self.game_data = self.pround_turbulent_skies
        self.__init__()
        self.__play()

    def play(self):
        string_hint = """
        0.exit
        1.impossible_tiamat
        2.impossible_abramelin
        3.pround_cycle
        4.pround_torment
        5.impossible_phoniex
        """
        index = -1
        index_max = 5
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
            self.play_impossible_tiamat()
        elif index == 2:
            self.play_impossible_abramelin()
        elif index == 5:
            self.play_impossible_phoniex()


class exo_diablo_crucible(event_common):
    """
    20240522
    """
    veryhard_data = util.exo_diablo_veryhard
    extreme_data = util.exo_diablo_extreme
    game_data = extreme_data
    crucible_data_120 = util.exo_diablo_crucible_120
    crucible_data_150 = util.exo_diablo_crucible_150

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

    def play_crucible_150(self):
        self.game_data = self.crucible_data_150
        self.__init__()
        self.__play()

    def play_crucible_120(self):
        self.game_data = self.crucible_data_120
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
        3.crucible_120
        4.crucible_150
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
            self.play_veryhard()
        elif index == 2:
            self.play_extreme()
        elif index == 3:
            self.play_crucible_120()
        elif index == 4:
            self.play_crucible_150()


class exo_corow_crucible(event_common):
    """
    20240223
    """
    veryhard_data = util.exo_corow_veryhard
    extreme_data = util.exo_corow_extreme
    game_data = extreme_data
    crucible_data_120 = util.exo_corow_crucible_120
    crucible_data_150 = util.exo_corow_crucible_150

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

    def play_crucible_150(self):
        self.game_data = self.crucible_data_150
        self.__init__()
        self.__play()

    def play_crucible_120(self):
        self.game_data = self.crucible_data_120
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
        3.crucible_120
        4.crucible_150
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
            self.play_veryhard()
        elif index == 2:
            self.play_extreme()
        elif index == 3:
            self.play_crucible_120()
        elif index == 4:
            self.play_crucible_150()


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
