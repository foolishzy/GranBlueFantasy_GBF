from game import game
from util import util 

class event_select:

    def __exit(self):

        pass


    def __init__(self):
        string_hint = '''
        请选择：
        0.退出
        1.hope_from_a_snow_drop
        2....
        '''
        index_max = 2
        index_min = 0
        index = -1
        while not (index >= index_min and index <= index_max):
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            hope_from_a_snow_drop().play()            


class event_common(game):
    def __init__(self, 
            game_data = {'url' : "", 'time_limit' : 10
                }
            ):
        self.url = game_data['url']
        super().__init__(
                game_data['time_limit']
                )
        pass


class hope_from_a_snow_drop(event_common):
    '''
    20231104测试可以跑通
    '''
    veryhard_data = util.hope_from_a_snow_drop_veryhard 
    impossible_data = util.hope_from_a_snow_drop_impossible
    extreme_data = util.hope_from_a_snow_drop_extreme
    game_data = impossible_data
    
    def __exit(self):
        pass

    def play(self):
        string_hint = '''
        \n
        0.exit
        1.veryhard
        2.extreme
        3.impossible
        '''
        index = -1
        index_max = 3
        index_min = 0
        while (not (index >= index_min and index <= index_max)):
            
            try:
                index = int(input(string_hint))
            except KeyboardInterrupt:
                self.__exit()
                break
        if index == 0:
            self.__exit()
        elif index == 1:
            self.play_veryhard()
        elif index == 2:
            self.play_extreme()
        elif index == 3:
            self.play_impossible()


    def __init__(self):
        super().__init__(self.game_data)

    def play_veryhard(self):
        self.game_data = self.veryhard_data
        self.__init__()
        self.__play()
    
    def play_extreme(self):
        self.game_data = self.extreme_data
        self.__init__()
        self.__play()

    def play_impossible(self):
        self.game_data = self.impossible_data
        self.__init__()
        self.__play()

    def __play(self):
        # 私有方法，实例中不要直接调用，会出错
        times = int(input('please input times to repeat : '))
        while times > 0:
            times = times - 1
            print("left times :", times)
            self.stage.goto(self.url)
            #打开网页
            self.mouse.click_friend_summon()
            self.mouse.click_party_ok()
            if self.ck.is_battle_page():
                self.mouse.click_full()
                self.auto_refresh()


