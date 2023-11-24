from event import event_select 
from arcumgame import arcum_select
from shiny_slime_weekend import slime_select
from rise_of_the_beasts import btb_select
from HL2 import hl_select
from unite_and_fight import unite_and_fight_select
from reserve_crate import reserve_select 

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
'''
        index_max = 7
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

