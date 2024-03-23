from game import game
from util import util
from alert import alert


class campaign_select:
    def __exit(self):
        pass

    def __init__(self):
        campaign().play()
        pass


class campaign(game):

    def __init__(self):
        data = util.campaign_exclusive_quest_data
        self.url = data['url']
        btl = data['time_limit']
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
                #  self.mouse.click_full()
                self.mouse.click_attack()
                self.auto_refresh()
        alert().run()
