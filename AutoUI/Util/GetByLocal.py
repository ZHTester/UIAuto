# encoding: utf-8
"""
# @Time    : 2019-08-20 18:24
# @Author  : Function
# @FileName    : GetByLocal.py
# @Software: PyCharm

获取元素定位方式  封装
"""
from selenium.common.exceptions import NoSuchElementException

from AutoUI.KeyWord.GetData import Getda
from AutoUI.Config.aibet_setting import *

class GetByLo:
    def __init__(self, driver,filepath):
        self.driver = driver
        self.getE = Getda(filepath)

    def ScreenShotError(self,row):
        imageName = str(self.getE.get_caseName(row))
        self.driver.get_screenshot_as_file('ID' + str(row) +screen_images_error + imageName + 'error.png')

    def get_element(self, row = None):
        """
        查找元素封装
        :return:
        """
        global by, by_local
        try:
            local = self.getE.get_element_key(row)
            by =  local.split(">")[0]
            by_local = local.split('>')[1]
            print(by_local)
        except IndexError:
            print('------------下标越界错误用例行数--%s------' %row)
            self.ScreenShotError(row)  # 错误截图

        try:
            if by == 'xpath':
                return self.driver.find_element_by_xpath(by_local)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(by_local)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(by_local)
            elif by == 'id':
                return self.driver.find_element_by_accessibility_id(by_local)
            elif by == 'aid':
                return self.driver.find_element_by_id(by_local)
            else:
                return None
        except NoSuchElementException:
            print('------------找不到元素错误用例行数--%s------' %row)
            self.ScreenShotError(row)  # 错误截图

    def get_lun_element(self,row = None):
        """
        轮播图获取元素形式  element1>element2
        :param row:
        :return:
        """
        local = self.getE.get_element_key(row)
        element1 = local.split(">")[0]
        element2 = local.split(">")[1]
        return element1,element2


if __name__ == '__main__':
    pass