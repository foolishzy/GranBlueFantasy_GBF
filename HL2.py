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
        """
        pass
        flag = False
        index_range = [[0, 7]]
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


class HL2(game):

    def __init__(self, data={'url': "", 'time_limit': 10, }):
        self.url = data['url']
        super().__init__(data['time_limit'])

    def play(self):
        super().play()
        flag = True
        repeat_times = 0
        while flag and (repeat_times <= 0 or repeat_times > 3):
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
                self.mouse.click_request_backup()
                self.mouse.click_full()
                self.auto_refresh()
        alert().run()


class shiva_impossible(HL2):
    data = util.hl2_shiva_impossible

    def __init__(self):
        super().__init__(self.data)
        pass


class europa_impossible(HL2):
    data = util.hl2_europa_impossible

    def __init__(self):
        super().__init__(self.data)
        pass


class godsworn_alexiel_impossible(HL2):
    data = util.hl2_godsworn_alexxiel_impossible

    def __init__(self):
        super().__init__(self.data)
        pass


class grimnir_impossible(HL2):
    data = util.hl2_grimnir_impossible

    def __init__(self):
        super().__init__(self.data)
        pass


class metatron_impossible(HL2):
    data = util.hl2_metatron_impossible

    def __init__(self):
        super().__init__(self.data)
        pass


class avatar_impossible(HL2):
    data = util.hl2_avatar_impossible

    def __init__(self):
        super().__init__(self.data)
        pass


class rose_queen_impossible(HL2):
    data = util.hl2_rose_queen_impossible

    def __init__(self):
        super().__init__(self.data)
        pass
