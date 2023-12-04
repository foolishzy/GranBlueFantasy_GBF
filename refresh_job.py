
from game import game


class refresh_job_select:

    def __init__(self):
        btl = (int(input('pls input max time limit for this battle : ')))
        if not (btl > 0):
            btl = 10
        self.game = game(btl)
        self.start()
        pass

    def start(self):
        #  self.game.party.manual_skill_list =
        flag = int(input('''
        use all summons ?
        1. yes
        2. no
        '''))
        if flag == 1:
            self.game.summons.use_all_summon_flag = True
        else:
            self.game.summons.use_all_summon_flag = None
        self.game.auto_refresh()
