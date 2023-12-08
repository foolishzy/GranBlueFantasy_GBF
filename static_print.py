import os
import time
from threading import Thread
"""
还没有调试

"""


class data:

    __name = None
    __data = None

    def __init__(self, name=None, data=None):
        self.__data = data
        self.__name = name
        pass

    def get_name(self):
        return self.__name

    def get_data(self):
        return self.__data

    def set_name(self, name):
        self.__name = name

    def set_data(self, data):
        self.__data = data


class data_manger:
    """data_manger."""

    data_dict = []

    def __init__(self):
        pass

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def my_print(self):
        """print."""
        while True:
            self.clear_screen()
            for d in self.data_dict:
                name = d.get_name()
                data = d.get_data()
                print(name, data)
                #  time.sleep(0.15)

    def add_data(self, Data: data):
        """add_data.

        :param Data:
        :type Data: data
        """
        if self.check_data_name_in_datadict(Data):
            self.updata_data(Data)
        else:
            self.data_dict.append(Data)

    def updata_data(self, Data: data):
        """updata_data.

        :param Data:
        :type Data: data
        """
        i = 0
        for d in self.data_dict:
            i = i + 1
            if d.get_name() == Data.get_name():
                #    self.data_dict.remove(d)
                #    self.data_dict.append(list(Data))
                self.data_dict[i] = Data
                break

    def remove_data(self, Data: data):
        """remove_data.

        :param Data:
        :type Data: data
        """
        i = 0
        for d in self.data_dict:
            i = i + 1
            if d.get_name() == Data.get_name():
                self.data_dict.remove(self.data_dict[i])
                break

    def check_data_name_in_datadict(self, Data: data):
        """check_data_name_in_datadict.

        :param Data:
        :type Data: data
        """
        flag = False
        for d in self.data_dict:
            if d.get_name() == Data.get_name():
                flag = True
                break
        return flag


class static_print:
    dm = data_manger()

    def __init__(self, dm: data_manger()):
        self.dm = dm
        pass

    def print(self):
        t1 = Thread(target=self.dm.my_print)
        t1.start()


dm = data_manger()
stp = static_print(dm)
stp.dm.add_data(data("nn", "dd"))
stp.print()
