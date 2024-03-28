from util import util
from game import game
from alert import alert


class hl_select:

    def exit(self):
        pass

    def __init__(self):

        string_hint = """
        请选择
        0. exit
        1. shiva impossible
        2. europa impossible
        3. godsworn alexiel impossible
        4. grimnir impossible
        5. metatron impossible
        6. avatar impossible
        7. rose queen impossible
        8. all_hl3.0
        """
        pass
        flag = False
        index_range = [[0, 8]]
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
            shiva_impossible().play()
        elif index == 2:
            europa_impossible().play()
        elif index == 3:
            godsworn_alexiel_impossible().play()
        elif index == 4:
            grimnir_impossible().play()
        elif index == 5:
            metatron_impossible().play()
        elif index == 6:
            avatar_impossible().play()
        elif index == 7:
            rose_queen_impossible().play()
        elif index == 8:
            for e in [shiva_impossible(),
                      europa_impossible(),
                      godsworn_alexiel_impossible(),
                      grimnir_impossible(),
                      metatron_impossible(),
                      avatar_impossible(),
                      rose_queen_impossible()]:
                e.three_times_play()
            alert().run()


class hl3(game):

    def __init__(self, data={'url': "", 'time_limit': 10, }):
        self.url = data['url']
        self.name = None
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


class shiva_impossible(hl3):
    data = util.hl3_shiva_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'shiva impossible'
        pass


class europa_impossible(hl3):
    data = util.hl3_europa_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'europa_impossible'
        pass


class godsworn_alexiel_impossible(hl3):
    data = util.hl3_godsworn_alexxiel_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'godsworn_alexiel_imposibble'
        pass


class grimnir_impossible(hl3):
    data = util.hl3_grimnir_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'grimnir_impossible'
        pass


class metatron_impossible(hl3):
    data = util.hl3_metatron_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'metatron_impossible'
        pass


class avatar_impossible(hl3):
    data = util.hl3_avatar_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'avatar_impossible'
        pass


class rose_queen_impossible(hl3):
    data = util.hl3_rose_queen_impossible

    def __init__(self):
        super().__init__(self.data)
        self.name = 'rose_queen_impossible'
        pass
