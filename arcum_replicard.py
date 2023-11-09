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
                }
            ):
        battle_time_limit = game_data['time_limit']
        url = game_data['url']
        gauge_url = game_data['gauge_url']
        super().__init__(battle_time_limit)
        self.url = url
        self.gauge_url = gauge_url

    def play(self):
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
            if self.ck.check_gauge(self.gauge_url):
                self.play_gauge()

    def play_gauge(self):
        if self.ck.check_gauge(self.gauge_url):
            # 宝箱 逻辑上必须是判断宝箱在前 宝箱怪在后
            self.mouse.click_gauge()
            self.mouse.click_gague_ok()
            self.mouse.click_gague_ok()
            self.stage.refresh()
            if self.ck.check_gauge_mimic():
                # 宝箱怪
                time.sleep(1.5)
                self.mouse.click_mimic()
                self.mouse.click_arcum_part_ok()
                self.mouse.click_full()
                self.ck.is_goal_page()
               
        else:
            if  self.ck.check_gauge_mimic():
                # 宝箱怪
                time.sleep(1.5)
                self.mouse.click_mimic()
                self.mouse.click_arcum_part_ok()
                self.mouse.click_full()
                self.ck.is_goal_page()
               





