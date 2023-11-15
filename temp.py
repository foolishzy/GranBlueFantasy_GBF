

from HL2 import HL2

class temp(HL2):
    def __init__(self):
        time = 10
        url = "https://game.granbluefantasy.jp/#quest/supporter/shop_treasure/103801/3/0/arcarum2!enhancement!detail!18/60/10/30"
        data = {"url" : url,
                "time_limit" : time}
        super().__init__(data)
        pass

t = temp()
t.play()
