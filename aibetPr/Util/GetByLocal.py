# encoding: utf-8

"""
# @Time    : 2019-08-20 18:24
# @Author  : Function
# @FileName    : GetByLocal.py
# @Software: PyCharm

获取元素定位方式  封装
"""
from aibetPr.KeyWord.GetData import Getda
from aibetPr.Config.setting import screen_images_error

class GetByLo:
    def __init__(self, driver):
        self.driver = driver
        self.getE = Getda()

    def ScreenShotError(self,row):
        imageName = str(self.getE.get_caseName(row))
        self.driver.get_screenshot_as_file(screen_images_error + imageName + 'error.png')

    def get_element(self, row = None):
        """
        查找元素封装
        :return:
        """

        local = self.getE.get_element_key(row)
        by =  local.split(">")[0]
        by_local = local.split('>')[1]
        try:
            if by == 'xpath':
                return self.driver.find_element_by_xpath(by_local)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(by_local)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(by_local)
            elif by == 'id':
                return self.driver.find_element_by_id(by_local)
            else:
                return None
        except:
            self.ScreenShotError(row)  # 错误截图


if __name__ == '__main__':
    pass
