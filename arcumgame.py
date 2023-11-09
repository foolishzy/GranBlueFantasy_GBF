from arcum_defender import  arcum_defender
from arcum_replicard import replicard_common
from util import util
from mouse import Mouse
from game import game

class arcum_select:

    def exit():
        pass

    def __init__(self):
        string_hint = '''
       请选择：
       0. exit
       1. mundus_dark_3_proud_war_princess_of_dragons
       2. mundus_dark_5_love_meeee
       3. mundus_dark_3_proud_war_princess_of_dragons
       4. mundus_light_3_goddess_of_the_wild_hunt
       5. mundus_light_5_high_voltage_rock
       6. mundus_fire_v2de_prometheus_militis       
       7. mundus_fire_5_hotheaded_pincers
       8. mundus_fire_3_earth_shattering_fire_demon
       9. mundus_water_5_parasite_steve
       10. mundus_water_3_tide_caller
       11. mundus_earth_5_princess_of_the_horde
       12. mundus_earth_3_elephant_stomping_ground
       13. mundus_earth_v2de_gilgamesh_militis
       14. mundus_wind_5_winged_demin_cat
       15. mundus_wind_v2de_morrigna_militis
       16. mundus_wind_3_dragon_in_glittering_green
       17. joculator_dark_ve_jurassic_dino
       18. joculator_dark_3_Dreadful_scourge
        '''
        index_max = 18 
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
        if index == 0:
            self.exit()
        elif index == 1:
            arcumgame().mundus_dark_3_proud_war_princess_of_dragons().play()
        elif index == 2:
            arcumgame().mundus_dark_5_love_meeee().play()
        elif index == 3:
            arcumgame().mundus_dark_3_proud_war_princess_of_dragons().play()
        elif index == 4:
            arcumgame().mundus_light_3_goddess_of_the_wild_hunt().play()
        elif index == 5:
            arcumgame().mundus_light_5_high_voltage_rock().play()
        elif index == 6:
            arcumgame().mundus_fire_v2de_prometheus_militis().play()
        elif index == 7:
            arcumgame().mundus_fire_5_hotheaded_pincers().play()
        elif arcumgame == 8:
            arcumgame().mundus_fire_3_earth_shattering_fire_demon().play()
        elif index == 9 :
            arcumgame().mundus_water_5_parasite_steve().play()
        elif index == 10:
            arcumgame().mundus_water_3_tide_caller().play()
        elif index == 11:
            arcumgame().mundus_earth_5_princess_of_the_horde().play()
        elif index == 12:
            arcumgame().mundus_earth_3_elephant_stomping_ground().play()
        elif index == 13:
            arcumgame().mundus_earth_v2de_gilgamesh_militis().play()
        elif index == 14:
            arcumgame().mundus_wind_5_winged_demin_cat().play()
        elif index == 15:
            arcumgame().mundus_wind_v2de_morrigna_militis().play()
        elif index == 16:
            arcumgame().mundus_wind_3_dragon_in_glittering_green().play()
        elif index == 17:
            arcumgame().joculator_dark_ve_jurassic_dino().play()
        elif index == 18:
            arcumgame().joculator_dark_3_Dreadful_scourge().play()


class arcumgame:
    def __init__(self):
        pass

    class mundus_earth_5_princess_of_the_horde(replicard_common):
        def __init__(self):
            data = util.mundus_earth_5_princess_of_the_horde
            super().__init__(data)

    class mundus_fire_v2de_prometheus_militis(arcum_defender):
        def __init__(self):
            data = util.mundus_fire_v2de_prometheus_militis 
            super().__init__(data)

    class mundus_fire_5_hotheaded_pincers(replicard_common):
        def __init__(self):
            data =  util.mundus_fire_5_hotheaded_pincers
            super().__init__(data)

    class mundus_water_5_parasite_steve(replicard_common):
        def __init__(self):
            data =  util.mundus_water_5_parasite_steve
            super().__init__(data)

    class mundus_wind_5_winged_demin_cat(replicard_common):
        def __init__(self):
            data =  util.mundus_wind_5_winged_demon_cat
            super().__init__(data)

    class mundus_water_3_tide_caller(replicard_common):
        def __init__(self):
            data =  util.mundus_water_3_tide_callers
            super().__init__(data)

    class mundus_wind_v2de_morrigna_militis(arcum_defender):
        def __init__(self):
            data =  util.mundus_wind_v2de_morrigna_militis
            super().__init__(data)

    class mundus_wind_3_dragon_in_glittering_green(replicard_common):
        def __init__(self):
            data =  util.mundus_wind_3_dragon_glittering_green
            super().__init__(data)

    class mundus_light_3_goddess_of_the_wild_hunt(replicard_common):
        def __init__(self):
            data =  util.mundus_light_3_goddess_of_the_wild_hunt
            super().__init__(data)

    class mundus_earth_3_elephant_stomping_ground(replicard_common):
        def __init__(self):
            data = util.mundus_earth_3_elephant_stormping_ground
            super().__init__(data)

    class mundus_fire_3_earth_shattering_fire_demon(replicard_common):
        def __init__(self):
            data = util.mundus_fire_3_earthshattering_fire_demon
            super().__init__(data)

    class mundus_light_5_high_voltage_rock(replicard_common):
        def __init__(self):
            data = util.mundus_light_5_high_voltage_rock
            super().__init__(data)

    class mundus_earth_v2de_gilgamesh_militis(arcum_defender):
        def __init__(self):
            data = util.mundus_earth_v2de_gilgamesh_militis
            super().__init__(data)

    class mundus_dark_3_proud_war_princess_of_dragons(replicard_common):
        def __init__(self):
            data = util.mundus_dark_3_proud_war_princess_of_dragons
            super().__init__(data)

    class mundus_dark_5_love_meeee(replicard_common):
        def __init__(self):
            data = util.mundus_dark_5_love_meeee
            super().__init__(data)

    class joculator_dark_ve_jurassic_dino(replicard_common):
        def __init__(self):
            data = util.joculator_dark_ve_jurassic_dinol
            super().__init__(data)

    class joculator_dark_3_Dreadful_scourge(replicard_common):
        def __init__(self):
            data = util.joculator_dark_3_Dreadful_scourge
            super().__init__(data)


