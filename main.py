from arcum_replicard import replicard_common
from util import util
from mouse import Mouse
from game import game
from jobselect import jobselect
from event import hope_from_a_snow_drop 
import threading 
from stage import checker 
from arcumgame import arcumgame
from selenium.webdriver.support import expected_conditions as EC
def printstate():
    g = game(10)
    chm =g.get_chm()
    g.auto_refresh() 
    #  while True:
        #  print(chm.execute_script('return document.readyState'))
#
def run():
    jobselect()    



def test():
#    hope_from_a_snow_drop().play_impossible()
    g = game(10)
    ele = util.loading_page_element['element']
    by = util.loading_page_element['by']
    a =EC.visibility_of_element_located((by, ele))
    print(a)

if __name__ == '__main__':
    print("cao")
    #  test()
    run()


