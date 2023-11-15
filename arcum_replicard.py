from alert import alert
import time
from game import game
from stage import stage
from mouse import Mouse
class replicard_common(game):

    
    def __init__(
            self,
            game_data = {
                'url' : "",
                'gauge_url' : "",
                'time_limit' : 3
                },
            gauge_box_data = {
                'box_ele' : 'txt-chest-name',
                'box_txt' : "Splendid Chest",
                'gauge_ele' : 'txt-quest-name',
                'gauge_txt' : ['Herald of The Moon','Herald of Death','Herald of Justice' ] ,
                'enemy_ele' : 'txt-quest-name',
                'enemy_txt' : ['Mimic', 'Obsidian Machina']
                }
                
            ):
        battle_time_limit = game_data['time_limit']
        url = game_data['url']
        gauge_url = game_data['gauge_url']
        super().__init__(battle_time_limit)
        self.url = url
        self.gauge_url = gauge_url
        self.gauge_box_data = gauge_box_data

    def play(self):
        super().play()
        repeat_times = int(input("pls input repeat times :"))
        while repeat_times > 0:
            print("while loop start")
            repeat_times = repeat_times - 1
            print("left times : ", repeat_times)
            self.stage.goto(self.url)
            self.mouse.click_arcum_part_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()
            if self.ck.check_box(self.gauge_box_data):
                pass
            elif self.ck.check_gauge(self.gauge_box_data):
                pass
            elif self.ck.check_gauge_enemy(self.gauge_box_data):
                pass
        alert().run()
    
    def play_box(self):
        self.mouse.click_box()
        self.mouse.click_gague_ok()
        if self.ck.check_gauge_enemy(self.gauge_box_data):
            self.play_gauge_enemy()
        else:
            time.sleep(0.5)

    def play_gauge(self):
        self.mouse.click_gauge()
        self.mouse.click_arcum_part_ok()
        self.mouse.click_full()
        self.ck.is_goal_page(30)

    def play_gauge_enemy(self):
        self.mouse.click_gauge_enemy()
        self.mouse.click_arcum_part_ok()
        self.mouse.click_full()
        self.ck.is_goal_page(30)





