import pyautogui 

class alert:

    def __init__(self):

        pass

    def run(self):
        end_box()
        sound()


    def sound(self):
        print("\a")

    def end_box(self,
            msg = '打完了'，
            title = "gbf script",
            bt = 'ok'):
        pyautogui.alert(msg, titile, bt)
