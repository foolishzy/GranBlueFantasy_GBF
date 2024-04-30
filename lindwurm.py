from game import game
from util import util
from alert import alert


class all_play:
    def play(self):
        lindwurm_game().three_times_play()


class lindwurm_game(game):
    def __init__(self):
        data = util.lindwurm_data
        self.url = data['url']
        self.name = 'lindwurm_game'
        self.three_times_flag = False
        super().__init__(data['time_limit'])

    def three_times_play(self):
        self.three_times_flag = True
        self.play()
        pass

    def play(self):
        super().play()
        flag = True
        if not self.three_times_flag:
            repeat_times = 0
            while flag and (repeat_times <= 0 or repeat_times > 3):
                try:
                    repeat_times = int(input("pls input repeat times :"))
                except KeyboardInterrupt:
                    repeat_times = 0
                    flag = False
                    break
        else:
            repeat_times = 3
        while repeat_times > 0:
            print("while loop start", self.name)
            repeat_times = repeat_times - 1
            print("left times : ", repeat_times)
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

        if not self.three_times_flag:
            alert().run()
