from selenium.webdriver.common.by import By
from alert import alert
from elementfinder import elefinder
import time
from game import game
from stage import stage
from mouse import Mouse
from timer import timer


class replicard_common(game):

    def __init__(
            self,
            game_data={
                'url': "",
                'gauge_url': "",
                'time_limit': 3
            },
            gauge_box_data={
                'box_ele': 'txt-chest-name',
                'box_txt': "Splendid Chest",
                'gauge_ele': 'txt-quest-name',
                'gauge_txt': ['Herald of The Moon', 'Herald of Death', 'Herald of Justice'],
                'box_enemy_ele': 'txt-quest-name',
                'box_enemy_txt': ['Mimic', 'Obsidian Machina']
            }

    ):
        battle_time_limit = game_data['time_limit']
        url = game_data['url']
        gauge_url = game_data['gauge_url']
        super().__init__(battle_time_limit)
        self.url = url
        self.gauge_url = gauge_url
        self.gauge_box_data = gauge_box_data
        self.timer = timer(self.__delattr__)

    def play(self):

        # one turn
        i = int(input("""
        100% chargebar and one turn?
        pls selcet:
        1. yes
        2. no
        """
                      ))
        if i == 1:
            self.oneturn = True
        else:
            self.oneturn = False
        # one turn
        by = self.util.screen_label_auto_refresh['by']
        ele = self.util.screen_label_auto_refresh['element']
        super().play()
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            self.timer.start()
            print("while loop start")
            repeat_times = repeat_times - 1
            print("left times : ", repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_arcum_part_ok()
            if self.ck.is_battle_page(10):
                if self.oneturn:
                    self.mouse.click_full()
                    if elefinder(by, ele, 30, self.chm).is_element_presence():
                        self.stage.refresh()
                else:
                    self.mouse.click_full()
                    self.auto_refresh()
            self.stage.goto(self.gauge_url, {
                            'element': 'prt-division-list', 'by': By.CLASS_NAME})
            if self.ck.check_box(self.gauge_box_data):
                self.play_box()
            elif self.ck.check_gauge(self.gauge_box_data):
                self.play_gauge()
            elif self.ck.check_gauge_enemy(self.gauge_box_data):
                self.play_gauge_enemy()
            self.timer.end()
        alert().run()

    def play_box(self):
        self.mouse.click_box()
        self.mouse.click_gauge_ok()
        if self.ck.check_gauge_enemy(self.gauge_box_data):
            self.play_gauge_enemy()
        else:
            time.sleep(0.5)

    def play_gauge(self):
        self.mouse.click_gauge()
        self.mouse.click_arcum_part_ok()
        self.mouse.click_full()
        self.ck.is_goal_page(300)

    def play_gauge_enemy(self):
        self.mouse.click_gauge_enemy()
        self.mouse.click_arcum_part_ok()
        self.mouse.click_full()
        self.ck.is_goal_page(300)
