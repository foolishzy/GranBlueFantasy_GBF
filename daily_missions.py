from HL2 import play_all as hl2_play_all
from primarch_trials import extreme_all as prt_exa
from primarch_trials import extreme_plus_all as prt_expa
from primarch_trials import standard_all as prt_sta
from six_dragon import all_play as six_dragon_all_play
from lindwurm import all_play as lind_all_play
from six_start_liejin import all_play as liejin_all_Play


class daily_missions:
    def _exit(self):
        pass

    def __init__(self):
        pass

    def play(self):
        #  hl2_play_all().play()
        prt_exa().play()
        # 天司ex难度
        prt_sta().play()
        # 天司标准难度
        prt_expa().play()
        # 天司explus
        six_dragon_all_play().play()
        # 六龙
        lind_all_play().play()
        # 林德龙
        liejin_all_Play().play()
        # 猎金 大巴 阿卡夏 大公
