from event import event_select
from arcumgame import arcum_select
from shiny_slime_weekend import slime_select
from rise_of_the_beasts import btb_select
from HL2 import hl_select
from unite_and_fight import unite_and_fight_select
from reserve_crate import reserve_select
from backup_request_game import select
from scales_of_dominion import scales_of_dominion_select
from refresh_job import refresh_job_select
from six_dragon import six_dragon_select
from campaign_exclusive_quest import campaign_select
from read_fate import fate_select
from free_quest_list import free_quest_list_select
from revenant_weapons_materials import materials_select


class jobselect:

    def __exit(self):

        pass

    def __init__(self):
        string_hint = '''
        请选择：
        0.exit
        1.event
        2.arcum
        3.slime
        4.rise of the beast
        5.hl2.0
        6.unite and fight
        7.clear_crate
        8.backup
        9.anubis showdown 大马的天平
        10.auto refresh
        11.six_dragon
        12.campaign_exclusive_quest
        13.read fate
        14.free_quest_list 
        15.revenant_weapons_materials
'''
        index_max = 15
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            event_select()
        elif index == 2:
            arcum_select()
        elif index == 3:
            slime_select()
        elif index == 4:
            btb_select()
        elif index == 5:
            hl_select()
        elif index == 6:
            unite_and_fight_select()
        elif index == 7:
            reserve_select()
        elif index == 8:
            select()
        elif index == 9:
            scales_of_dominion_select()
        elif index == 10:
            refresh_job_select()
        elif index == 11:
            six_dragon_select()
        elif index == 12:
            campaign_select()
        elif index == 13:
            fate_select()
        elif index == 14:
            free_quest_list_select()
        elif index == 15:
            materials_select()
