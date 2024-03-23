from arcum_defender import arcum_defender
from arcum_replicard import replicard_common
from util import util
from mouse import Mouse
from game import game


class arcum_select:

    def exit(self):
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
       117. mundus_water_v2de_ca_ong_militis
       118. mundus_fire_v2de_plus_promatheus_militis
       201. joculator_dark_ve_jurassic_dino
       202. joculator_dark_3_Dreadful_scourge
       203. joculator_dark_5_bloody_soothsayer
       204. joculator_dark_5_nebulous_one
       205. joculator_water_5_giant_sea_plant
       206. joculator_water_5_glacial_hellbeast
       207. joculator_water_3_maiden_of_the_depiths
       208. joculator_de_water_lady_of_redemption
       209. joculator_water_xeno_cocytus_militis
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
       401. zone_faym_water_de_creeping_seashadow
       402. zone_faym_water_de_lilywhite_paragon 
       403. zone_faym_water_5_trident_grandmaster
       404. zone_faym_water_5_farsea_predator 
       405. zone_faym_water_5_azureflame_dragon
       406. zone_faym_water_5_eyes_of_sorrow 
       407. zone_faym_water_3_hoarfrost_icequeen
       408. zone_faym_water_3_faymian_fortress 
       409. zone_faym_dark_de_iceberg_champion
       410. zone_faym_dark_5_draconic_simulacrum
       411. zone_faym_dark_5_oceanic_archon
       412. zone_faym_dark_3_mad_shearwielder
       501. zone_goliath_vestige_of_truth
       601. zone_harbinger_wind_5_dirgesinger
       602. zone_harbinger_wind_5_vengeful_demigod
       603. zone_harbinger_wind_de+_majestic_goldenwing
       604. zone_harbinger_wind_de_majestic_goldenwing
       605. zone_harbinger_wind_3_wildwind_conjurer/fullthunde_conjurer
       606. zone_harbinger_wind_3_harbinger_simurgh
       607. zone_harbinger_wind_5_harbinger_hardwood
       608. zone_harbinger_wind_de_tempestuous_beauty
       609. zone_harbinger_wind_de+_tempestuous_beauty
       610. zone_harbinger_wind_5_demanding_stormgod
       611. zone_harbinger_v2_wind_harbinger_stormer
       612. zone_harbinger_light_3_dimensional_riftwalker
       613. zone_harbinger_light_5_phantasmagoric_aberration
       614. zone_harbinger_light_de_jadegleam_dragonkin
       615. zone_harbinger_light_5_harbinger_tyrant
       616. zone_harbinget_light_de_plus_jadegleam_dragonkin
       801. zone_kalendae_xneo_vohu_manah_militis
    '''
        flag = False
        while not flag:
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                index = 0
                break
            index_range = [[0, 0], [601, 616], [101, 118], [201, 209], [
                301, 313], [401, 412], [501, 501], [801, 801]]
            for i in index_range:
                if index >= i[0] and index <= i[1]:
                    flag = True
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
        elif index == 108:
            arcumgame().mundus_fire_3_earth_shattering_fire_demon().play()
        elif index == 109:
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
        elif index == 117:
            arcumgame().mundus_water_v2de_ca_ong_militis().play()
        elif index == 118:
            arcumgame().mundus_fire_v2de_plus_prometheus_militis().play()
        elif index == 201:
            arcumgame().joculator_dark_ve_jurassic_dino().play()
        elif index == 202:
            arcumgame().joculator_dark_3_Dreadful_scourge().play()
        elif index == 203:
            arcumgame().joculator_dark_5_bloody_soothsayer().play()
        elif index == 204:
            arcumgame().joculator_dark_5_nebulous_one().play()
        elif index == 205:
            arcumgame().joculator_water_5_giant_sea_plant().play()
        elif index == 206:
            arcumgame().joculator_water_5_glacial_hellbeast().play()
        elif index == 207:
            arcumgame().joculator_water_3_maiden_of_the_depiths().play()
        elif index == 208:
            arcumgame().joculator_de_water_lady_of_redemption().play()
        elif index == 209:
            arcumgame().joculator_water_xeno_cocytus_militis
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
        elif index == 401:
            arcumgame().zone_faym_water_de_creeping_seashadow().play()
        elif index == 402:
            arcumgame().zone_faym_water_de_lilywhite_paragon().play()
        elif index == 403:
            arcumgame().zone_faym_water_5_trident_grandmaster().play()
        elif index == 404:
            arcumgame().zone_faym_water_5_farsea_predator().play()
        elif index == 405:
            arcumgame().zone_faym_water_5_azureflame_dragon().play()
        elif index == 406:
            arcumgame().zone_faym_water_5_eyes_of_sorrow().play()
        elif index == 407:
            arcumgame().zone_faym_water_3_hoarfrost_icequeen().play()
        elif index == 408:
            arcumgame().zone_faym_water_3_faymian_fortress().play()
        elif index == 409:
            arcumgame().zone_faym_dark_de_iceberg_champion().play()
        elif index == 410:
            arcumgame().zone_faym_dark_5_draconic_simulacrum().play()
        elif index == 411:
            arcumgame().zone_faym_dark_5_oceanic_archon().play()
        elif index == 412:
            arcumgame().zone_faym_dark_3_mad_shearwielder().play()
        elif index == 501:
            arcumgame().zone_goliath_vestige_of_truth().play()
        elif index == 601:
            arcumgame().zone_harbinger_wind_5_dirgesinger().play()
        elif index == 602:
            arcumgame().zone_harbinger_wind_5_vengful_demigod().play()
        elif index == 603:
            arcumgame().zone_harbinger_wind_de_plus_majestic_goldenwing().play()
        elif index == 604:
            arcumgame().zone_harbinger_wind_de_majestic_goldenwing().play()
        elif index == 605:
            arcumgame().zone_harbinger_wind_3_wildwind_conjurer().play()
        elif index == 606:
            arcumgame().zone_harbinger_wind_3_harbinger_simurgh()
        elif index == 607:
            arcumgame().zone_harbinger_wind_5_harbinger_hardwood().play()
        elif index == 608:
            arcumgame().zone_harbinger_wind_de_tempestuous_beauty().play()
        elif index == 609:
            arcumgame().zone_harbinger_wind_de_plus_tempestuous_beauty().play()
        elif index == 610:
            arcumgame().zone_harbinger_wind_5_demanding_stormgod().play()
        elif index == 611:
            arcumgame().zone_harbinger_v2_wind_harbinger_stormer().play()
        elif index == 612:
            arcumgame().zone_harbinger_light_3_dimensional_riftwalker().play()
        elif index == 613:
            arcumgame().zone_harbinger_light_5_phantasmagoric_aberration().play()
        elif index == 614:
            arcumgame().zone_harbinger_light_de_jadegleam_dragonkin().play()
        elif index == 615:
            arcumgame().zone_harbinger_light_5_harbinger_tyrant().play()
        elif index == 616:
            arcumgame().zone_harbinger_light_de_plus_jadegleam_dragonkin().play()
        elif index == 801:
            arcumgame().zone_kalendae_xeno_vohu_manah_militis().play()


class zone_harbinger_common(replicard_common):
    def __init__(self, data):
        gb_data = util.arcum_zone_harbinger_gauge_box_data
        super().__init__(data, gb_data)


class arcumgame:
    def __init__(self):
        pass

    class zone_harbinger_wind_5_harbinger_hardwood(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_5_harbinger_hardwood
            super().__init__(data)

    class zone_harbinger_wind_de_plus_tempestuous_beauty(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_de_plus_tempestuous_beauty
            super().__init__(data)

    class zone_harbinger_wind_de_tempestuous_beauty(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_de_tempestuous_beauty
            super().__init__(data)

    class zone_harbinger_wind_5_demanding_stormgod(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_5_demanding_stormgod
            super().__init__(data)

    class zone_harbinger_light_5_phantasmagoric_aberration(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_light_5_phantasmagoric_aberration
            super().__init__(data)

    class zone_harbinger_light_de_plus_jadegleam_dragonkin(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_light_de_plus_jadegleam_dragonkin
            super().__init__(data)

    class zone_harbinger_light_de_jadegleam_dragonkin(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_light_de_jadegleam_dragonkin
            super().__init__(data)

    class zone_harbinger_light_5_harbinger_tyrant(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_light_5_harbinger_tyrant
            super().__init__(data)

    class zone_harbinger_wind_3_harbinger_simurgh(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_3_harbinger_simurgh
            super().__init__(data)

    class zone_harbinger_wind_3_wildwind_conjurer(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_3_wildwind_conjurer
            super().__init__(data)

    class zone_harbinger_wind_de_majestic_goldenwing(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_de_majestic_goldenwing
            #  super().__init__(data)
            print('correct url pls')

    class zone_harbinger_wind_de_plus_majestic_goldenwing(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_wind_de_plus_majestic_goldenwing
            super().__init__(data)

    class zone_harbinger_light_3_dimensional_riftwalker(zone_harbinger_common):
        def __init__(self):
            data = util.zone_harbinger_light_3_dimensional_riftwalker
            super().__init__(data)

    class zone_harbinger_v2_wind_harbinger_stormer(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_harbinger_gauge_box_data
            data = util.zone_harbinger_v2_wind_harbinger_stormer
            super().__init__(data, gb_data)

    class zone_harbinger_wind_5_vengful_demigod(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_harbinger_gauge_box_data
            data = util.zone_harbinger_wind_5_vengeful_demigod
            super().__init__(data, gb_data)

    class zone_harbinger_wind_5_dirgesinger(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_harbinger_gauge_box_data
            data = util.zone_harbinger_wind_5_dirgesing
            super().__init__(data, gb_data)

    class zone_goliath_vestige_of_truth(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_goliath_gauge_box_data
            data = util.arcum_vestige_of_truth
            super().__init__(data, gb_data)

    class zone_kalendae_xeno_vohu_manah_militis(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_kalendae_gauge_box_data
            data = util.zone_kalendae_xeno_vohu_manah_militis
            super().__init__(data, gb_data)

    class mundus_earth_5_princess_of_the_horde(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_earth_5_princess_of_the_horde
            super().__init__(data, gb_data)

    class mundus_fire_v2de_plus_prometheus_militis(arcum_defender):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_fire_v2de_plus_prometheus_militis
            super().__init__(data, gb_data)

    class mundus_fire_v2de_prometheus_militis(arcum_defender):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_fire_v2de_prometheus_militis
            super().__init__(data, gb_data)

    class mundus_fire_5_hotheaded_pincers(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_fire_5_hotheaded_pincers
            super().__init__(data, gb_data)

    class mundus_water_5_parasite_steve(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_water_5_parasite_steve
            super().__init__(data, gb_data)

    class mundus_wind_5_winged_demin_cat(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_wind_5_winged_demon_cat
            super().__init__(data, gb_data)

    class mundus_water_3_tide_caller(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_water_3_tide_caller
            super().__init__(data, gb_data)

    class mundus_wind_v2de_morrigna_militis(arcum_defender):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_wind_v2de_morrigna_militis
            super().__init__(data, gb_data)

    class mundus_wind_3_dragon_in_glittering_green(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_wind_3_dragon_glittering_green
            super().__init__(data, gb_data)

    class mundus_light_3_goddess_of_the_wild_hunt(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_light_3_goddess_of_the_wild_hunt
            super().__init__(data, gb_data)

    class mundus_earth_3_elephant_stomping_ground(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_earth_3_elephant_stormping_ground
            super().__init__(data, gb_data)

    class mundus_fire_3_earth_shattering_fire_demon(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_fire_3_earthshattering_fire_demon
            super().__init__(data, gb_data)

    class mundus_light_5_high_voltage_rock(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_light_5_high_voltage_rock
            super().__init__(data, gb_data)

    class mundus_earth_v2de_gilgamesh_militis(arcum_defender):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_earth_v2de_gilgamesh_militis
            super().__init__(data, gb_data)

    class mundus_dark_3_proud_war_princess_of_dragons(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_dark_3_proud_war_princess_of_dragons
            super().__init__(data, gb_data)

    class mundus_dark_5_love_meeee(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_dark_5_love_meeee
            super().__init__(data, gb_data)

    class mundus_water_v2de_ca_ong_militis(replicard_common):
        def __init__(self):
            gb_data = util.arcum_mundus_gauge_box_data
            data = util.mundus_water_v2de_ca_ong_militis
            super().__init__(data, gb_data)

    class joculator_dark_ve_jurassic_dino(replicard_common):
        def __init__(self):
            data = util.joculator_dark_ve_jurassic_dino
            gb_data = util.arcum_joculator_gauge_box_data
            super().__init__(data, gb_data)

    class joculator_dark_3_Dreadful_scourge(replicard_common):
        def __init__(self):
            gb_data = util.arcum_joculator_gauge_box_data
            data = util.joculator_dark_3_Dreadful_scourge
            super().__init__(data, gb_data)

    class joculator_water_5_glacial_hellbeast(replicard_common):
        def __init__(self):
            gb_data = util.arcum_joculator_gauge_box_data
            data = util.joculator_water_5_glacial_hellbeast
            super().__init__(data, gb_data)

    class joculator_water_3_maiden_of_the_depiths(replicard_common):
        def __init__(self):
            gb_data = util.arcum_joculator_gauge_box_data
            data = util.joculator_water_3_maiden_of_the_depiths
            super().__init__(data, gb_data)

    class joculator_de_water_lady_of_redemption(replicard_common):
        def __init__(self):
            data = util.joculator_de_water_lady_of_the_redemption
            gb_data = util.arcum_joculator_gauge_box_data
            super().__init__(data, gb_data)

    class joculator_dark_5_bloody_soothsayer(replicard_common):
        def __init__(self):
            data = util.joculator_dark_5_bloody_soothsayer
            gb_data = util.arcum_joculator_gauge_box_data
            super().__init__(data, gb_data)

    class joculator_water_5_giant_sea_plant(replicard_common):
        def __init__(self):
            data = util.joculator_water_5_giant_sea_plant
            gb_data = util.arcum_joculator_gauge_box_data
            super().__init__(data, gb_data)

    class joculator_dark_5_nebulous_one(replicard_common):
        def __init__(self):
            data = util.joculator_dark_5_nebulous_one
            gb_data = util.arcum_joculator_gauge_box_data
            super().__init__(data, gb_data)

    class joculator_water_xeno_cocytus_militis(replicard_common):
        def __init__(self):
            data = util.joculator_water_xeno_cocytus_militis
            gb_data = util.arcum_joculator_gauge_box_data
            super().__init__(data, gb_data)

    class zoneeletio_fire_de_cleansing_wyrmgod(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_de_cleansing_wyrmgod
            super().__init__(data, gb_data)

    class zoneeletio_fire_5_slithering_seductress(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_5_slithering_seductress
            super().__init__(data, gb_data)

    class zoneeletio_fire_5_eletion_drake(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_5_eletion_drake
            super().__init__(data, gb_data)

    class zoneeletio_fire_de_usurper_of_the_throne(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_de_usurper_of_the_throne
            super().__init__(data, gb_data)

    class zoneeletio_fire_5_paradoxical_gate(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_5_paradoxical_gate
            super().__init__(data, gb_data)

    class zoneeletio_fire_3_blazing_everwing(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_3_blazing_everwing
            super().__init__(data, gb_data)

    class zoneeletio_fire_3_rageborn_one(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_3_rageborn_one
            super().__init__(data, gb_data)

    class zoneeletio_fire_5_terror_trifecta(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_5_terror_trifecta
            super().__init__(data, gb_data)

    class zoneeletio_light_3_living_lighting_rod(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_light_3_living_lighting_rod
            super().__init__(data, gb_data)

    class zoneeletio_light_5_death_seer(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_light_5_death_seer
            super().__init__(data, gb_data)

    class zoneeletio_light_de_violetflash_sovereign(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_light_de_violetflash_sovereign
            super().__init__(data, gb_data)

    class zoneeletio_light_3_hundred_armed_hulk(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_light_3_hundred_armed_hulk
            super().__init__(data, gb_data)

    class zoneeletio_fire_boss_eletion_glider(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_eletio_gauge_box_data
            data = util.zoneeletio_fire_boss_eletion_glider
            super().__init__(data, gb_data)

        def play(self):
            print('waitting for compeleting...!')

    class zone_faym_water_de_creeping_seashadow(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_de_creeping_seashadow
            super().__init__(data, gb_data)

    class zone_faym_water_de_lilywhite_paragon(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_de_lilywhite_paragon
            super().__init__(data, gb_data)

    class zone_faym_water_5_trident_grandmaster(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_5_trident_grandmaster
            super().__init__(data, gb_data)

    class zone_faym_water_5_farsea_predator(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_5_farsea_predator
            super().__init__(data, gb_data)

    class zone_faym_water_5_azureflame_dragon(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_5_azureflame_dragon
            super().__init__(data, gb_data)

    class zone_faym_water_5_eyes_of_sorrow(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_5_eyes_of_sorrow
            super().__init__(data, gb_data)

    class zone_faym_water_3_hoarfrost_icequeen(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_3_hoarfrost_icequeen
            super().__init__(data, gb_data)

    class zone_faym_water_3_faymian_fortress(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_water_3_faymian_fortress
            super().__init__(data, gb_data)

    class zone_faym_dark_de_iceberg_champion(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_dark_de_iceberg_champion
            super().__init__(data, gb_data)

    class zone_faym_dark_5_draconic_simulacrum(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_dark_5_draconic_simulacrum
            super().__init__(data, gb_data)

    class zone_faym_dark_5_oceanic_archon(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_dark_5_oceanic_archon
            super().__init__(data, gb_data)

    class zone_faym_dark_3_mad_shearwielder(replicard_common):
        def __init__(self):
            gb_data = util.arcum_zone_faym_gauge_box_data
            data = util.zone_faym_dark_3_mad_shearwielder
            super().__init__(data, gb_data)
