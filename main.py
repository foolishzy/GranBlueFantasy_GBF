from arcum_replicard import replicard_common
from util import util
from mouse import Mouse
from game import game
from jobselect import jobselect
from event import hope_from_a_snow_drop 
import threading 
from stage import checker 
from arcumgame import arcumgame
def printstate():
    g = game(10)
    chm =g.get_chm()
    g.auto_refresh() 
    #  while True:
        #  print(chm.execute_script('return document.readyState'))
#
def run():
    jobselect()    


    #  arcumgame.mundus_dark_5_love_meeee().play()
    #  arcumgame.jurassic_dino.play()
    #  vestige_of_truth_data = util.arcum_vestige_of_truth
    #  vestige_of_truth = replicard_common(vestige_of_truth_data)
    #  vestige_of_truth.play()
    #  jurassic_dino_data = util.arcum_jurassic_dino
    #  jurassic_dino = replicard_common(jurassic_dino_data)
    #  jurassic_dino.play()
#


def test():
#    hope_from_a_snow_drop().play_impossible()
    g = game(10)
    c = checker(g.get_chm(),10)
    c.check_gauge("https://game.granbluefantasy.jp/#replicard/stage/10")


if __name__ == '__main__':
    print("cao")
    #  test()
    run()
    #  t1 = threading.Thread(target = test)
    #  t2 = threading.Thread(target = printstate)
    #  t1.start()
    #  t2.start()
    #  t1.join()
    #  t2.join()
    #  arcumgame().joculator_dark_3_Dreadful_scourge().play()


