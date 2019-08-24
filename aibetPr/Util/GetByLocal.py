# encoding: utf-8

"""
# @Time    : 2019-08-20 18:24
# @Author  : Function
# @FileName    : GetByLocal.py
# @Software: PyCharm

获取元素定位方式  封装
"""
from aibetPr.Util.OperaExcel import OpExcel
from aibetPr.KeyWord.GetData import Getda

class GetByLo:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self,row = None):
        """
        查找元素封装
        :return:
        """
        getE = Getda()
        local = getE.get_element_key(row)
        by =  local.split(">")[0]
        by_local = local.split('>')[1]
        if by == 'xpath':
            return self.driver.find_element_by_xpath(by_local)
        elif by == 'classname':
            self.driver.find_element_by_class_name(by_local)
        elif by == 'css':
            self.driver.find_element_by_css_selector(by_local)
        elif by == 'id':
            self.driver.find_element_by_id(by_local)
        else:
            return None,"元素未找到"

if __name__ == '__main__':
    pass
