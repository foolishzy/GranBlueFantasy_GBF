from selenium.webdriver.common.by import By


class util:

    # tyras blizza misadventure
    tyras_blizza_misadventure_impossible = {
        "url": "https://game.granbluefantasy.jp/#quest/supporter/914541/1/0/10514",
        "time_limit": 3
    }
    # campaign exclusive quest
    campaign_exclusive_quest_data = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/800021/22",
        'time_limit': 1
    }
    # ultimate_showndowns 20231225
    tuna_lover_extreme_data = {
        "url": 'https://game.granbluefantasy.jp/#quest/supporter/915321/1',
        'time_limit': 1
    }
    tuna_golem_data = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/915331/1",
        "time_limit": 3
    }
    salmun_golem_data = {
        "url": "https://game.granbluefantasy.jp/#quest/supporter/915231/1",
        'time_limit': 3
    }
    salmun_lover_extreme_data = {
        "url": "https://game.granbluefantasy.jp/#quest/supporter/915221/1",
        "time_limit": 1
    }
    # divine generals
    divine_generals_rapid_extreme = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/913961/1",
        "time_limit": 5
    }
    divine_generals_solo_extreme = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/913921/5",
        'time_limit': 5
    }

    # exo ifrit

    exo_ifrit_crucible = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/913071/3",
        "time_limit": 5
    }
    exo_ifrit_veryhard = {

        'url': 'https://game.granbluefantasy.jp/#quest/supporter/913011/3',
        'time_limit': 3
    }
    exo_ifrit_extreme = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/913021/3",
        'time_limit': 3
    }
    # anubis showdown 大马

    anubis_showdown_data = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/103901/3',
        'time_limit': 10
    }
    # reserve
    reserve_weapon_bt_data = {
        'by': By.XPATH,
        'element': "/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[3]/div[3]/div"
    }
    reserve_summon_bt_data = {
        'by': By.XPATH,
        'element': '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[4]/div[4]/div'
    }
    reserve_bt_dialog_ok = {
        'by': By.XPATH,
        'element': '//div[@class="btn-usual-ok"]'
    }
    reserve_bt_dialog_use = {
        'by': By.XPATH,
        'element': '//div[@class="btn-usual-ok btn-usual-use btn-silent-se"]'
    }
    reserve_bt_dialog_reserve = {
        'by': By.XPATH,
        'element': '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[2]/div[6]/div/div[3]/div[2]'
    }
    reserve_bt_timelimit = {
        'by': By.XPATH,
        'element': '/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[1]/div[2]'
    }
    reserve_bt_nolimit = {
        'by': By.XPATH,
        'element': "/html/body/div/div[2]/div/div[3]/div[3]/div[2]/div[1]/div[1]"
    }
    reserve_page_url = "https://game.granbluefantasy.jp/#present"
    # unite and fight
    uf_solo_normal = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912611/3/0',
        'time_limit': 2
    }
    uf_solo_hard = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912621/3/0',
        'time_limit': 2
    }
    uf_solo_veryhard = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912631/3/0',
        'time_limit': 2
    }
    uf_rapid_extreme = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912641/1/0',
        'time_limit': 3
    }
    uf_rapid_extreme_plus = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912651/1/0',
        'time_limit': 3
    }
    uf_rapid_nightmare = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912661/1/0/10116',
        'time_limit': 5
    }
    uf_final_rally = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter_raid/35368078507/912771/1/0/0/2",
        'time_limit': 5
    }
    # 场景切换页面的loading元素
    loading_page_element = {
        'element': "img-load",
        'by': By.CLASS_NAME
    }
    # six dragon
    six_dragon_fire = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/305191/1/0/41',
        'time_limit': 10
    }
    six_dragon_water = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/305201/1/0/42",
        "time_limit": 10
    }
    six_dragon_earth = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/305211/1/0/43',
        'time_limit': 10
    }
    six_dragon_wind = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/305221/1/0/44",
        "time_limit": 10
    }
    six_dragon_dark = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/305241/1/0/46",
        "time_limit": 10
    }
    six_dragon_light = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/305231/1/0/45",
        "time_limit": 10
    }
    # HL2.0
    hl2_shiva_impossible = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/303151/1/0/522",
        'time_limit': 10
    }
    hl2_europa_impossible = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/303161/1/0/523',
        'time_limit': 10
    }
    hl2_godsworn_alexxiel_impossible = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/303171/1/0/524",
        "time_limit": 10
    }
    hl2_grimnir_impossible = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/303181/1/0/525",
        'time_limit': 10
    }
    hl2_metatron_impossible = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/303191/1/0/526',
        'time_limit': 10
    }
    hl2_avatar_impossible = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/303221/1/0/527",
        'time_limit': 10
    }
    hl2_rose_queen_impossible = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/300471/1/0/1204',
        'time_limit': 10
    }
    # 四象降临
    btb_event_main_url = "https://game.granbluefantasy.jp/#event/advent"
    btb_extreme_plus = {
        'by': By.CLASS_NAME,
        'element': "prt-raid-image",
        'time_limit': 10
    }
    btb_impossible = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/743451/1",
        'by': By.CLASS_NAME,
        'element': "prt-hl-count",
        'time_limit': 10
    }
    btb_extreme_xuanwu = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/711041/1",
        'time_limit': 5
    }
    btb_extreme_zhuque = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/711191/1",
        'time_limit': 5
    }
    btb_extreme_qinglong = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/711091/1",
        'time_limit': 5
    }
    btb_extreme_baihu = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/711141/1",
        'time_limit': 5
    }
    # 踢馆
    shiny_slime_week = {'url': 'https://game.granbluefantasy.jp/#quest/supporter/400181/4',
                        'time_limit': 2}

    shiny_slime_weekend = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/400151/4", 'time_limit': 2}
    chrome_remote_host = "127.0.0.1:9222"
    # 选择队伍界面的ok确认键
    screen_mouse_party_ok = {
        'by': By.XPATH, 'element': '//*[@id="wrapper"]/div[3]/div[3]/div[3]/div[2]'}
    mouse_position_party_ok = {'x': 250, 'y': 570}
    mouse_position_party_ok_dert = {'x': 100, 'y': 10}
    # 选择第一个好友的召唤石
    screen_lable_friend_summon = {
        'by': By.XPATH, 'element': '//*[@id="cnt-quest"]/div[2]/div[6]/div[1]/div[4]'}
    mouse_position_friend_summon = {'x': 100, 'y': 500}
    mouse_position_friend_summon_dert = {'x': 5, 'y': 5}
    screen_label_friend_summmon_page = {
        'text': 'Choose a Summon', 'by': By.CLASS_NAME, 'element': 'prt-supporter-title'}
    # arcum选择队伍界面的ok确认键
    screen_label_arcum_party_ok = {
        'by': By.XPATH, 'element': '//*[@id="wrapper"]/div[3]/div[3]/div[3]/div[2]'}
    mouse_position_arcum_party_ok = {'x': 300, 'y': 600}
    mouse_position_arcum_party_ok_dert = {'x': 50, 'y': 10}
    # 战斗界面的attack键坐标和偏移量
    mouse_position_battle_attack = {'x': 280, 'y': 380}
    mouse_position_battle_attack_dert = {'x': 70, 'y': 30}
    # 战斗界面的full键坐标和偏移量
    mouse_position_battle_full = {'x': 85, 'y': 410}
    mouse_position_battle_full_dert = {'x': 10, 'y': 10}
    # 多人列表最上面一场战斗
    mouse_position_rapid_filter_frist = {'x': 200, 'y': 400}
    mouse_position_rapid_filter_frist_dert = {'x': 50, 'y': 50}

    # 战斗界面显示last turn processing
    screen_label_battle_lastturn_processing = {
        'element': "prt-popup-header", 'by': By.CLASS_NAME, 'text': 'Processing'}
    screen_label_battle_full = {'element': 'btn-auto', 'by': By.CLASS_NAME}
    screen_label_party_ok = {
        'element':  '//div[@class="prt-btn-deck"]', 'by': By.XPATH}
    screen_label_arcum_part_ok = {'by': By.XPATH,
                                  'element': '//div[@class="prt-btn-deck"]'}
    screen_label_battle_attack = {
        'element': '//div[@class="btn-attack-start display-on"]', 'by': By.XPATH}
    screen_label_home = {'by':  By.ID, 'element': "btm-campaign-toggle"}
    screen_label_battle_alldead = {
        'text': "Use Auto Select", 'element': "txt-title", 'by': By.CLASS_NAME}
    screen_label_battle_goal_exp = {
        'by': By.CLASS_NAME, 'element': "cnt-get-experience"}
    screen_label_auto_refresh = {
        'by': By.XPATH, 'element': '//div[@class="btn-attack-start display-off"]'}
    screen_label_battle_page = {
        'element': "prt-gauge-area", 'by': By.CLASS_NAME}
    screen_label_arcum_gauge = {
        'element': "txt-chest-name", 'by': By.CLASS_NAME}
    screen_label_arcum_gauge_goto_url = {
        'element': 'prt-aap-num', "by": By.CLASS_NAME}
    screen_label_arcum_gauge_mimic = {
        'text': "Mimic", 'by': By.CLASS_NAME, 'element': "txt-quest-name"}
    screen_label_arcum_gauge_ok = {
        'element': 'btn-usual-ok', 'by': By.CLASS_NAME}
    screen_lable_battle_request_backup = {
        'element': 'btn-assist', "by": By.CLASS_NAME}
    screen_lable_battle_request_backup_dialog_ok = {
        'element': 'btn-usual-ok', 'by': By.CLASS_NAME}
    screen_lable_battle_request_backup_dialog_backup = {
        'element': "/html/body/div/div[2]/div/div[3]/div[3]/div[6]/div/div[3]/a", "by": By.XPATH}
    # url
    url_home = "https://game.granbluefantasy.jp/#mypage"
    # arcum
    arcum_zone_kalendae_gauge_box_data = {
        'box_ele': 'txt-chest-name',
        'box_txt': "Splendid Chest",
        'gauge_ele': 'txt-quest-name',
        'gauge_name': ['Herald of Earth', 'Herald of Dark'],
        'box_enemy_ele': 'txt-quest-name',
        'box_enemy_name': ['Mimic']
    }
    arcum_zone_faym_gauge_box_data = {
        'box_ele': 'txt-chest-name',
        'box_txt': "Splendid Chest",
        'gauge_ele': 'txt-quest-name',
        'gauge_name': ['Herald of The Moon', 'Herald of Death', 'Herald of Justice'],
        'box_enemy_ele': 'txt-quest-name',
        'box_enemy_name': ['Mimic', 'Obsidian Machina']
    }
    arcum_zone_eletio_gauge_box_data = {
        'box_ele': 'txt-chest-name',
        'box_txt': "Splendid Chest",
        'gauge_ele': 'txt-quest-name',
        'gauge_name': ['Herald of The Star', 'Herald of The Sun', 'Herald of The Devil'],
        'box_enemy_ele': 'txt-quest-name',
        'box_enemy_name': ['Mimic', 'Ruby Machina']
    }
    arcum_mundus_gauge_box_data = {
        'box_ele': 'txt-chest-name',
        'box_txt': "Splendid Chest",
        'gauge_ele': 'txt-quest-name',
        'gauge_name': ['Herald of Water', 'Herald of Fire', 'Herald of Earth', 'Herald of Wind', 'Herald of Light', 'Herald of Dark'],
        'box_enemy_ele': 'txt-quest-name',
        'box_enemy_name': ['Mimic']
    }
    arcum_joculator_gauge_box_data = {
        'box_ele': 'txt-chest-name',
        'box_txt': "Splendid Chest",
        'gauge_ele': 'txt-quest-name',
        'gauge_name': ['Herald of Water', 'Herald of Dark'],
        'box_enemy_ele': 'txt-quest-name',
        'box_enemy_name': ['Mimic']
    }
    # stage 9
    liber_boss_wind_garuda_militis = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/9/9/16/818091/25/0/25078"
    }
    # stage 8
    zone_kalendae_xeno_vohu_manah_militis = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/8/8/9/817131/25/0/25083",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/8",
        "time_limit": 10
    }
    # stage 2
    zoneeletio_fire_de_cleansing_wyrmgod = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/3/811101/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_5_slithering_seductress = {
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10,
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/3/811011/25"
    }
    zoneeletio_light_3_living_lighting_rod = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/5/811021/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_5_eletion_drake = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/6/811031/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_de_usurper_of_the_throne = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/8/811111/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_5_paradoxical_gate = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/8/811041/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_3_blazing_everwing = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/11/811061/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_light_5_death_seer = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/13/811051/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_light_de_violetflash_sovereign = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/13/811121/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_light_3_hundred_armed_hulk = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/15/811081/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_3_rageborn_one = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/17/811091/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_5_terror_trifecta = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/2/2/19/811071/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }
    zoneeletio_fire_boss_eletion_glider = {
        'url': "",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/2",
        "time_limit": 10
    }

    # stage 7
    joculator_dark_5_bloody_soothsayer = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/7/7/10/816041/25",
        'time_limit': 3,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'

    }
    joculator_dark_5_nebulous_one = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/7/7/12/816051/25",
        'time_limit': 3,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'
    }
    joculator_water_5_glacial_hellbeast = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/7/7/3/816011/25",
        'time_limit': 3,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'

    }
    joculator_water_3_maiden_of_the_depiths = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/7/7/7/816031/25",
        'time_limit': 3,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'

    }
    joculator_de_water_lady_of_the_redemption = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/7/7/3/816071/25",
        'time_limit': 10,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'

    }
    joculator_water_xeno_cocytus_militis = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/7/7/15/816131/25/0/25083",
        'time_limit': 15,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'

    }
    joculator_water_5_giant_sea_plant = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/5/816021/25',
        'time_limit': 3,
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/7'
    }

    joculator_dark_3_Dreadful_scourge = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/14/816061/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/7",
        "time_limit": 10

    }
    joculator_dark_ve_jurassic_dino = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/14/816081/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/7",
        "time_limit": 10
    }

    # stage 10
    mundus_wind_v2de_morrigna_militis = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/15/819171/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 10
    }
    mundus_light_3_goddess_of_the_wild_hunt = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/15/819121/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_dark_3_proud_war_princess_of_dragons = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/11/819091/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_wind_3_dragon_glittering_green = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/14/819111/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_water_3_tide_caller = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/10/819081/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_wind_5_winged_demon_cat = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/13/819101/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_water_5_parasite_steve = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/9/819071/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3,
        'box_xpath_element': '//*[@id="cnt-division"]/div/div[2]/div[1]/div'
    }
    mundus_water_v2de_ca_ong_militis = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/10/10/9/819151/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 10
    }
    mundus_fire_v2de_prometheus_militis = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/2/819141/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 10
    }
    mundus_fire_5_hotheaded_pincers = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/2/819011/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_earth_v2de_gilgamesh_militis = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/6/819161/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 15
    }
    mundus_earth_5_princess_of_the_horde = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/6/819041/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_fire_3_earthshattering_fire_demon = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/10/10/3/819021/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_earth_3_elephant_stormping_ground = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/10/10/7/819051/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_light_5_high_voltage_rock = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/10/10/4/819031/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    mundus_dark_5_love_meeee = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/10/10/8/819061/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/10",
        'time_limit': 3
    }
    # zone faym
    zone_faym_water_de_creeping_seashadow = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/4/812101/25',
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit':  10
    }
    zone_faym_water_5_trident_grandmaster = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/3/3/4/812011/25"
    }
    zone_faym_water_3_hoarfrost_icequeen = {
        "url": 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/3/812021/25',
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3

    }
    zone_faym_dark_5_oceanic_archon = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/3/3/6/812031/25"
    }
    zone_faym_water_5_farsea_predator = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/8/812041/25'
    }
    zone_faym_water_3_faymian_fortress = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/10/812051/25'

    }
    zone_faym_water_de_lilywhite_paragon = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 10,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/10/812111/25'

    }
    zone_faym_dark_de_iceberg_champion = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 10,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/11/812121/25'

    }
    zone_faym_dark_5_draconic_simulacrum = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/11/812061/25'

    }
    zone_faym_water_5_azureflame_dragon = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/14/812081/25'

    }
    zone_faym_water_5_eyes_of_sorrow = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/13/812071/25'

    }
    zone_faym_dark_3_mad_shearwielder = {
        'gauge_url': 'https://game.granbluefantasy.jp/#replicard/stage/3',
        'time_limit': 3,
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/3/3/16/812091/25'
    }
    arcum_jurassic_dino = {
        'url': 'https://game.granbluefantasy.jp/#replicard/supporter/7/7/14/816081/25',
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/7",
        'time_limit': 3
    }
    arcum_vestige_of_truth = {
        'url': "https://game.granbluefantasy.jp/#replicard/supporter/4/4/3/813011/25",
        'gauge_url': "https://game.granbluefantasy.jp/#replicard/stage/4",
        'time_limit': 3
    }

    # event
    Detective_Barawa_very_hard = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912921/1',
        'time_limit': 3
    }
    Detective_Barawa_extreme = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912931/1/0/10505',
        'time_limit': 3
    }
    Detective_Barawa_impossible = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912941/1/0/10505',
        'time_limit': 8
    }
    Detective_solo_Nightmare = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912911/3',
        'time_limit': 5
    }
    hope_from_a_snow_drop_impossible = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912341/1/0/10504',
        'time_limit': 10
    }
    hope_from_a_snow_drop_extreme = {
        'url': 'https://game.granbluefantasy.jp/#quest/supporter/912331/1/0/10504',
        'time_limit': 3
    }
    hope_from_a_snow_drop_veryhard = {
        'url': "https://game.granbluefantasy.jp/#quest/supporter/912321/1",
        'time_limit': 3
    }

    def __init__(self):
        pass
