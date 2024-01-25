import pyautogui


class alert:

    def __init__(self):

        pass

    def run(self, msg=None, title=None):
        self.sound()
        if msg and title:
            self.end_box(msg=msg, title=title)
        else:
            self.end_box()

    def sound(self):
        print("\a")

    def end_box(self, msg="打完", title="gbf script", bt='ok'):
        pyautogui.alert(msg, title, bt)
