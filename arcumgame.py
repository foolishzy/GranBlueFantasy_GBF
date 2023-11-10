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
       101. mundus_dark_3_proud_war_princess_of_dragons
       102. mundus_dark_5_love_meeee
       103. mundus_dark_3_proud_war_princess_of_dragons
       104. mundus_light_3_goddess_of_the_wild_hunt
       105. mundus_light_5_high_voltage_rock
       106. mundus_fire_v2de_prometheus_militis       
       107. mundus_fire_5_hotheaded_pincers
       108. mundus_fire_3_earth_shattering_fire_demon
       109. mundus_water_5_parasite_steve
       110. mundus_water_3_tide_caller
       111. mundus_earth_5_princess_of_the_horde
       112. mundus_earth_3_elephant_stomping_ground
       113. mundus_earth_v2de_gilgamesh_militis
       114. mundus_wind_5_winged_demin_cat
       115. mundus_wind_v2de_morrigna_militis
       116. mundus_wind_3_dragon_in_glittering_green
       201. joculator_dark_ve_jurassic_dino
       202. joculator_dark_3_Dreadful_scourge
       301. zoneeletio_fire_de_cleansing_wyrmgod
       302. zoneeletio_fire_5_slithering_seductress
       303. zoneeletio_fire_5_eletion_drake
       304. zoneeletio_fire_de_usurper_of_the_throne
       305. zoneeletio_fire_5_paradoxical_gate
       306. zoneeletio_fire_3_blazing_everwing
       307. zoneeletio_fire_3_rageborn_one
       308. zoneeletio_fire_5_terror_trifecta
       309. zoneeletio_light_3_living_lighting_rod 
       310. zoneeletio_light_5_death_seer
       311. zoneeletio_light_de_violetflash_sovereign
       312. zoneeletio_light_3_hundred_armed_hulk
       313. zoneeletio_fire_boss_eletion_glider
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
        elif index == 101:
            arcumgame().mundus_dark_3_proud_war_princess_of_dragons().play()
        elif index == 102:
            arcumgame().mundus_dark_5_love_meeee().play()
        elif index == 103:
            arcumgame().mundus_dark_3_proud_war_princess_of_dragons().play()
        elif index == 104:
            arcumgame().mundus_light_3_goddess_of_the_wild_hunt().play()
        elif index == 105:
            arcumgame().mundus_light_5_high_voltage_rock().play()
        elif index == 106:
            arcumgame().mundus_fire_v2de_prometheus_militis().play()
        elif index == 107:
            arcumgame().mundus_fire_5_hotheaded_pincers().play()
        elif arcumgame == 108:
            arcumgame().mundus_fire_3_earth_shattering_fire_demon().play()
        elif index == 109 :
            arcumgame().mundus_water_5_parasite_steve().play()
        elif index == 110:
            arcumgame().mundus_water_3_tide_caller().play()
        elif index == 111:
            arcumgame().mundus_earth_5_princess_of_the_horde().play()
        elif index == 112:
            arcumgame().mundus_earth_3_elephant_stomping_ground().play()
        elif index == 113:
            arcumgame().mundus_earth_v2de_gilgamesh_militis().play()
        elif index == 114:
            arcumgame().mundus_wind_5_winged_demin_cat().play()
        elif index == 115:
            arcumgame().mundus_wind_v2de_morrigna_militis().play()
        elif index == 116:
            arcumgame().mundus_wind_3_dragon_in_glittering_green().play()
        elif index == 201:
            arcumgame().joculator_dark_ve_jurassic_dino().play()
        elif index == 202:
            arcumgame().joculator_dark_3_Dreadful_scourge().play()
        elif index == 301:
            arcumgame().zoneeletio_fire_de_cleansing_wyrmgod().play()
        elif index == 302:
            arcumgame().zoneeletio_fire_5_slithering_seductress().play()
        elif index == 303:
            arcumgame().zoneeletio_fire_5_eletion_drake().play()
        elif index == 304:
            arcumgame().zoneeletio_fire_de_usurper_of_the_throne().play()
        elif index == 305:
            arcumgame().zoneeletio_fire_5_paradoxical_gate().play()
        elif index == 306:
            arcumgame().zoneeletio_fire_3_blazing_everwing().play()
        elif index == 307:
            arcumgame().zoneeletio_fire_3_rageborn_one().play()
        elif index == 308:
            arcumgame().zoneeletio_fire_5_terror_trifecta().play()
        elif index == 309:
            arcumgame().zoneeletio_light_3_living_lighting_rod().play()
        elif index == 310:
            arcumgame().zoneeletio_light_5_death_seer().play()
        elif index == 311:
            arcumgame().zoneeletio_light_de_violetflash_sovereign().play()
        elif index == 312:
            arcumgame().zoneeletio_light_3_hundred_armed_hulk().play()
        elif index == 313:
            arcumgame().zoneeletio_fire_boss_eletion_glider().play()

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

    class zoneeletio_fire_de_cleansing_wyrmgod(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_de_cleansing_wyrmgod 
            super().__init__(data)
 
    class zoneeletio_fire_5_slithering_seductress(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_5_slithering_seductress 
            super().__init__(data)
   
    class zoneeletio_fire_5_eletion_drake(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_5_eletion_drake 
            super().__init__(data)
  
    class zoneeletio_fire_de_usurper_of_the_throne(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_de_usurper_of_the_throne
            super().__init__(data)
 
    class zoneeletio_fire_5_paradoxical_gate(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_5_paradoxical_gate
            super().__init__(data)
   
    class zoneeletio_fire_3_blazing_everwing(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_3_blazing_everwing
            super().__init__(data)
 
    class zoneeletio_fire_3_rageborn_one(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_3_rageborn_one
            super().__init__(data)
 
    class zoneeletio_fire_5_terror_trifecta(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_5_terror_trifecta
            super().__init__(data)
   
    class zoneeletio_light_3_living_lighting_rod(replicard_common):
        def __init__(self):
            data = util.zoneeletio_light_3_living_lighting_rod
            super().__init__(data)
 
    class zoneeletio_light_5_death_seer(replicard_common):
        def __init__(self):
            data = util.zoneeletio_light_5_death_seer
            super().__init__(data)
 
    class zoneeletio_light_de_violetflash_sovereign(replicard_common):
        def __init__(self):
            data = util.zoneeletio_light_de_violetflash_sovereign 
            super().__init__(data)
   
    class zoneeletio_light_3_hundred_armed_hulk(replicard_common):
        def __init__(self):
            data = util.zoneeletio_light_3_hundred_armed_hulk
            super().__init__(data)
    
    class zoneeletio_fire_boss_eletion_glider(replicard_common):
        def __init__(self):
            data = util.zoneeletio_fire_boss_eletion_glider
            super().__init__(data)
        def play(self):
            print('waitting for compeleting...!')
