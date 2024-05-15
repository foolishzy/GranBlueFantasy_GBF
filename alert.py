import pyautogui
from threading import Thread


class alert:

    def __init__(self, string=""):
        self.string = string
        pass

    def run(self, msg=None, title=None):
        self.sound()

        # 有些问题 先注释掉 没想好怎么写
        #  if msg and title:
        #  self.end_box(msg=msg, title=title)
        #  else:
        #  self.end_box()

    def sound(self):
        print("\a")

    def end_box(self, msg="打完", title="gbf script", bt='ok'):
        pa = pyautogui.alert(self.string + msg, title, bt)
        t1 = Thread(target=pa)
        t1.start()


if __name__ == "__main__":
    a = alert("test")
    a.run("run", "title")
