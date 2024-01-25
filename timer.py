import time


class timer:
    def __init__(self, name=None):
        self.end_time = None
        self.start_time = None
        self.name = name
        pass

    def start(self):
        self.start_time = time.time()
        pass

    def end(self):
        self.end_time = time.time()
        if self.name:
            print(self.name, "计时结束")
        t = self.end_time - self.start_time
        print("执行时间:", "%.2f" % t, "s")
        pass

    def reset(self):
        self.end_time = None
        self.start()
        pass

    def clear(self):
        pass
