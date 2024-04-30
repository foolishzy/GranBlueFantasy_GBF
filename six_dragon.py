from util import util
from game import game
from alert import alert


class six_dragon_select:

    def exit(self):
        pass

    def __init__(self):

        string_hint = """
        请选择
        0. exit
        1. fire
        2. water
        3. earth
        4. wind
        5. light
        6. dark
        7. all_six
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
            six_dragon_fire().play()
        elif index == 2:
            six_dragon_water().play()
        elif index == 3:
            six_dragon_earth().play()
        elif index == 4:
            six_dragon_wind().play()
        elif index == 5:
            six_dragon_light().play()
        elif index == 6:
            six_dragon_dark().play()
        elif index == 7:
            all_play().play()


class all_play:
    def play(self):
        for e in [
            six_dragon_fire(),
            six_dragon_water(),
            six_dragon_earth(),
            six_dragon_wind(),
            six_dragon_light(),
            six_dragon_dark()
        ]:
            e.all_play()
        alert().run()


class six_dragon(game):

    def __init__(self, data={'url': "", 'time_limit': 10, }):
        self.url = data['url']
        self.name = None
        super().__init__(data['time_limit'])

    def all_play(self):
        self.all_play_flag = True
        self.play()

    def play(self):
        super().play()
        flag = True
        repeat_times = 1
        #  repeat_times = 0
        #  while flag and (repeat_times <= 0 or repeat_times > 3):
        #  try:
        #  repeat_times = int(input("pls input repeat times :"))
        #  except KeyboardInterrupt:
        #  repeat_times = 0
        #  flag = False
        #  break
        while repeat_times > 0:
            print("while loop start")
            print(self.name)
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
            if not self.all_play_flag:
                alert().run()


class six_dragon_fire(six_dragon):
    data = util.six_dragon_fire

    def __init__(self):
        super().__init__(self.data)
        self.name = 'six dragon fire'
        pass


class six_dragon_water(six_dragon):

    data = util.six_dragon_water

    def __init__(self):
        super().__init__(self.data)
        self.name = 'six dragon water'
        pass


class six_dragon_earth(six_dragon):

    data = util.six_dragon_earth

    def __init__(self):
        super().__init__(self.data)
        self.name = 'six dragon earth'
        pass


class six_dragon_wind(six_dragon):

    data = util.six_dragon_wind

    def __init__(self):
        super().__init__(self.data)
        self.name = 'six dragon wind'
        pass


class six_dragon_light(six_dragon):

    data = util.six_dragon_light

    def __init__(self):
        super().__init__(self.data)
        self.name = 'six dragon light'
        pass


class six_dragon_dark(six_dragon):

    data = util.six_dragon_dark

    def __init__(self):
        super().__init__(self.data)
        self.name = 'six dragon dark'
        pass
