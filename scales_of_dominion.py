from alert import alert
from game import game
from util import util


class scales_of_dominion_select:
    def __init__(self):
        scales_of_dominion().play()


class scales_of_dominion(game):
    # https://game.granbluefantasy.jp/#quest/supporter/103901/3
    def __init__(self):
        time = util.anubis_showdown_data['time_limit']
        self.url = util.anubis_showdown_data['url']
        super().__init__(time)

    def play(self):
        print('play scales of dominion ')
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            repeat_times = repeat_times - 1
            print('left times : ' + str(repeat_times))
            self.stage.goto(self.url)
            super().play()
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            self.party.update()
            self.party.player_one.use_skill(2)
            self.summons.update()
            self.summons.use_all_summon()
            self.mouse.click_full()
            self.auto_refresh()
        alert().run()
