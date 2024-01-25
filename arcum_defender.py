from arcum_replicard import replicard_common
from selenium.webdriver.common.by import By


class arcum_defender(replicard_common):
    '''
    阿卡姆defender
    '''

    def play(self):
        if self.check_opportunities():
            super().play()

    def check_opportunities(self):
        '''
        检查是否还有次数
        '''
        by = By.XPATH
        ele_path = '//*[@id="wrapper"]/div[3]/div[3]/div[1]/div[3]'
        return self.stage.loader(self.url, by, ele_path, 1)
