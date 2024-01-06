from game import game
from util import util
from alert import alert


class materials_select():
    def __init__(self):
        string_hint = """
        0. exit
        1. zephyr feather
        2. ...
        """
        flag = False
        index_range = [[0, 2]]
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
            self.__exit()
        elif index == 1:
            scattered_cargo().play()

    def __exit(self):
        pass


class scattered_cargo(game):

    def __init__(self):
        data = util.scattered_cargo
        self.btl = data['time_limit']
        self.url = data['url']
        super().__init__(self.btl)

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
            self.mouse.click_skip()
            self.mouse.click_items_picked_up_ok()

            if self.ck.is_battle_page():
                self.mouse.click_attack()
                self.mouse.click_semi()
            self.ck.is_goal_page(self.btl * 60)
        alert().run()
