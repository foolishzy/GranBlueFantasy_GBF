from event import event_select 
from arcumgame import arcum_select
from shiny_slime_weekend import slime_select



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
        '''
        index_max = 3
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

