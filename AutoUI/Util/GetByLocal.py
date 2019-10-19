# encoding: utf-8
"""
# @Time    : 2019-08-20 18:24
# @Author  : Function
# @FileName    : GetByLocal.py
# @Software: PyCharm

获取元素定位方式  封装
"""
import time

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from AutoUI.KeyWord.GetData import Getda
from AutoUI.KeyWord.GetData import Getda
from Util.OtherFunction import creatFile


class GetByLo:
    def __init__(self, driver, sheetN):
        self.driver = driver
        self.sheetN = sheetN
        self.data = Getda(sheetN)


    def ScreenShot(self, row, file_s=None):
        """
        截图方法
        :return:
        """
        imageName = str('ID' + str(row) + self.data.get_caseName(row))
        file_path = creatFile(file_s)
        self.driver.get_screenshot_as_file(file_path + imageName + '.png')

    def get_element(self,row=None):
        """
        查找元素封装
        :return:
        """
        global by, by_local
        try:
            local = self.data.get_element_key(row)
            by = local.split("<")[0]
            by_local = local.split('<')[1]
        except IndexError:
            print('------------下标越界错误用例行数--%s------' % row)
            self.ScreenShot(row, file_s='../Image/Error_Img/下标越界图片/')  # 错误截图
        try:
            if by == 'xpath':
                self.driver.find_element_by_xpath(by_local)
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
            self.ScreenShot(row, file_s='../Image/Error_Img/元素找不到图片/')  # 错误截图
            self.data.write_value(row, '测试失败')



    def get_lun_element(self, row=None):
        """
        轮播图获取元素形式  element1>nt2
        :param row:
        :return:
        """
        local = self.data.get_element_key(row)
        element1 = local.split("<")[0]
        element2 = local.split("<")[1]
        return element1, element2



if __name__ == '__main__':
    g = GetByLo(1,1)
